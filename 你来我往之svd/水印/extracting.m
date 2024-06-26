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