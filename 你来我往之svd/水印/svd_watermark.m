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