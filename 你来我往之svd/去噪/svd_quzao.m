image = imread('test.jpg');

[r,g,b] = imsplit(image);

r = double(r);
g = double(g);
b = double(b);

[ur,sr,vr] = svd(r);
sr(15:end,15:end) = 0;
new_r =uint8( ur*sr*vr');

[ug,sg,vg] = svd(g);
sg(15:end,15:end) = 0;
new_g =uint8( ug*sg*vg');


[ub,sb,vb] = svd(b);
sb(15:end,15:end) = 0;
new_b =uint8( ub*sb*vb');

rst = cat(3,new_r,new_g);
rst = cat(3,rst,new_b);

imshow(rst);
imwrite(rst,'rst.jpg')