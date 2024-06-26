同学自由组队，每位同学任意选取彩色载体图像矩阵A(维度M*N*3），W(维度m*n*3）作为待嵌入水印的彩色图像矩阵，M>m，N>n，选择合适的水印强度参数a，通过SVD将w嵌入到A中，交给其他同学必须的数据进行水印的验证。











## 水印嵌入

###### 原图及水印原图

![image-20240407115458887](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240407115458887.png)

左为原图 右为水印



###### 思路

> ​	首先，对不起了老师，题目中说M>m，N>n，也就是水印比原图要小。但方便起见。我这个水印和原图大小是一样的，都是1078*1078。



​	把rgb三个通道都通过相同处理：



- 原图和水印都svd分解。用u,s,v分别代表**原图的**左奇异矩阵，对角矩阵，右奇异矩阵，

  u_w,s_w,v_w分别代表**水印的**左奇异矩阵，对角矩阵，右奇异矩阵

- s = s + a * s_w   其中a是水印强度。也就是原图的对角阵加上a倍的水印对角阵

- 新图层 = u * s *v转置



再合并三个图层，得到新图

###### MATLAB源代码

```matlab
watermark = imread("watermark.jpg");
photo = imread("test.jpg");
photo = double(photo);
watermark = double(watermark);


a = 0.1; %水印强度

%对原图和水印都进行三通道的分离
[wr,wg,wb] = imsplit(watermark);
[r,g,b] = imsplit(photo);

%对原图三个通道svd
[ur,sr,vr] = svd(r);
[ug,sg,vg] = svd(g);
[ub,sb,vb] = svd(b);

%对水印的三个通道svd
[ur_w,sr_w,vr_w] = svd(wr);
[ug_w,sg_w,vg_w] = svd(wg);
[ub_w,sb_w,vb_w] = svd(wb);


%通过改变对角矩阵值的方式，嵌入水印
sr = sr + (a * sr_w);
sg = sg + (a * sg_w);
sb = sb + (a * sb_w);

%再把svd分解出来的东西乘回去，得到三通道的图片信息
new_r = ur * sr * vr';
new_g = ug * sg * vg';
new_b = ub * sb * vb';

%合并三通道，并且把数据类型转成uint8
rst = cat(3,new_r,new_g);
rst = cat(3,rst,new_b);
rst = uint8(rst);


imwrite(rst,'result.jpg')
```

###### 结果展示

![image-20240407121555631](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240407121555631.png)

水印强度为0.1

左原图   右有水印

肉眼区别不大，**但还是能看出来带水印的狗子脸上白亮了很多**

观察图片信息

![image-20240407121742926](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240407121742926.png)

从图片大小来看还是有区别的





















## 水印提取

​	图片的发布者如果想通过 提取水印 来证明自己作者的身份。那他一定知道以下信息:

- 原图
- 水印强度
- 水印图片矩阵svd分解后的左奇异矩阵、右奇异矩阵

###### 思路

待提取的图片，svd分解之后的对角阵 减去 原图的对角阵。再除以水印强度，这就得到了水印图片的对角阵

再根据水印图片矩阵svd分解后的左奇异矩阵、右奇异矩阵，还原出水印图



###### MATLAB源代码

```matlab
a = 0.1

%读取带水印的图片和原图
source = imread("result.jpg");
origin = imread("test.jpg");

source = double(source);
origin = double(origin);

[r_source,g_source,b_source] = imsplit(source);
[r_origin,g_origin,b_origin] = imsplit(origin);


%r图层对角阵
[U,S,V] = svd(r_source);
[u,s,v] = svd(r_origin);
r_watermark = (S-s)/a;

%g图层对角阵
[U,S,V] = svd(g_source);
[u,s,v] = svd(g_origin);
g_watermark = (S-s)/a;

%b图层对角阵
[U,S,V] = svd(b_source);
[u,s,v] = svd(b_origin);
b_watermark = (S-s)/a;

%读取水印原图，获取左奇异矩阵、右奇异矩阵
mark = imread("watermark.jpg");
mark = double(mark);
[r_mark,g_mark,b_mark] = imsplit(mark);

[u,s,v] = svd(r_mark);
r = u * r_watermark * v';

[u,s,v] = svd(g_mark);
g = u * g_watermark * v';

[u,s,v] = svd(b_mark);
b = u * b_watermark * v';

rst = cat(3,r,g);
rst = cat(3,rst,b);
rst = uint8(rst);

imwrite(rst,'extracted.jpg')
```

###### 提取结果

![image-20240407131046905](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240407131046905.png)

左为提取的，右为原图

二者肉眼看上去完全是同一个东西，已经达到了提取出水印，证明作者身份的目的。
