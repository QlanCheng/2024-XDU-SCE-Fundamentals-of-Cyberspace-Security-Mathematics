# 2024-XDU-SCE-Fundamentals-of-Cyberspace-Security-Mathematics

2024年网络安全数学基础

这门课属于是上课教了一粒沙，作业要写撒哈拉。

而且前半部分的内容没有任何PPT、教材、资料。作业难度极大



需者自取



## 勘误及说明

你来我往之LFSR破译，本原多项式的生成并不是乱生成的，是有数论说法的。但是作者水瓶有限，用的是随机生成法，这导致了有的本原多项式做出来效果很差，会产生不唯一等现象。



HMM，依然存疑



Bloom过滤器设计，理论m的值并不是200000，当时搞错了。借鉴者须自己注意。dataset.csv数据集文件Windows可能会报病毒自动删除。？？？csv文件能有啥病毒？？？



svd扩展，作业过难，而且要求是隐写方面的。作者无力解决



数论中的prime.py就是一个质数列表。test.py仅仅是用计算机求解的程序，并不是作业



随机几何存疑，题目描述均匀分布。这个均匀分布是表示概率服从均匀分布，还是类似高中生物那样的均匀分布：如图

![Example Image](images/example.png)



作者水平极其有限、必然有大量未发现的错误。读者请自己注意







## 作者声明

- 作者水平很低，是个菜鸡，作业中必然有错误内容



- 编程功力非常有限，代码中可能会产生迷惑行为，不许笑



- 目录结构很乱，主要原因是写作业的时候没考虑到开源



- 如果读者直接copy，作者个人没有任何意见，但是考试啥也不会是你自己的事



- svd扩展我不会，因此本项目中没有



- 部分作业需要手写，主要是后面的群论内容。手写的作业由于作者字太丑（QAQ），不开源，具体而言，包括：**数论基础、代数基础、有限域、椭圆曲线**。项目中可能仍有这些目录，但目录中是资料、非手写内容、用于验证的代码等。并不是最终作业。

  

- 使用的编程语言几乎全部为Python。少量为MATLAB。本门课程几乎不涉及C/C++、JAVA。不选修python的同学可能会红温



- 代码、作业中如果出现了奇奇怪怪的东西，那是我忘了删，呜呜呜





## 每次作业题目

#### 第一次--你来我往之LFSR破译

![image-20240627002156626](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627002156626.png)



#### 第二次--SVD之去噪、水印、svd拓展

![image-20240627002428789](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627002428789.png)

![image-20240627002452303](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627002452303.png)

![image-20240627002522601](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627002522601.png)



#### 第三次--离散马尔科夫链

![image-20240627002540204](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627002540204.png)

#### 第四次--HMM（隐马尔科夫链）

![image-20240627002606954](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627002606954.png)



#### 第五次--Bloom过滤器设计

![image-20240627002701943](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627002701943.png)



#### 第六次--数论基础

![image-20240627002949625](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627002949625.png)

#### 第七次--代数基础、利用生日悖论求解离散对数

![image-20240627003039387](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627003039387.png)

____

![image-20240627003132031](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627003132031.png)

![image-20240627003142739](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627003142739.png)

#### 第八次--概率论

![image-20240627003344562](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627003344562.png)



#### 第九次--有限域

![image-20240627003439409](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627003439409.png)



#### 第十次--椭圆曲线

![image-20240627003541691](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627003541691.png)



#### 第十一次--随机几何

![image-20240627003634718](C:\Users\86198\AppData\Roaming\Typora\typora-user-images\image-20240627003634718.png)
