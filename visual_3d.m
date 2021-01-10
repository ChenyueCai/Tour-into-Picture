figure(3);
% ratio is backimage h/w
ratio=500/700;
planex = [0 0 0; 0 0 0];
planey = [-1/ratio 0 1/ratio; -1/ratio 0 1/ratio]./2;
planez = [1 1 1; 0 0 0];
back = imread('./box_faces/back.png');
% create the surface and texturemap it with a given image
warp(planex,planey,planez,back);

n=1;
hold on;
planex = [-2 -1 0; -2 -1 0]./n;
planey = [-1 -1 -1; -1 -1 -1]./ratio./2;
planez = [1 1 1; 0 0 0];
im1=imread('./box_faces/l_side.png');
warp(planex,planey,planez,im1);

planex = [-2 -2 -2; 0 0 0]./n;
planey = [-1 0 1; -1 0 1]./ratio./2;
planez = [1 1 1; 1 1 1];
im2=imread('./box_faces/ceiling.png');
warp(planex,planey,planez,im2);

planex = [0 0 0; -2 -2 -2]./n;
planey = [-1 0 1; -1 0 1]./ratio./2;
planez = [0 0 0; 0 0 0];
im3=imread('./box_faces/floor.png');
warp(planex,planey,planez,im3);

planex = [0 -1 -2; 0 -1 -2]./n;
planey = [1 1 1; 1 1 1]./ratio./2;
planez = [1 1 1; 0 0 0];
im4=imread('./box_faces/r_side.png');
warp(planex,planey,planez,im4);