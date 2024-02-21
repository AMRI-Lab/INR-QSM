% Please add STISuite to working path

load data.mat
vox=[1,1,3];
H=[0,0,1];

[~,X0]=FastQSM_normalized(phi,msk,'voxelsize',vox,'H',H);
% [phi] is the 3D normalized tissue phase with a unit of "ppm"
% [msk] is 3D the brain mask
% [vox] is the voxel size, eg, [1,1,3]
% [H] is orientation vector, eg, [0,0,1]

weight_low=0.5;
weight_high=0.7;
WG=TVweighting(X0,msk,vox,[weight_low,weight_high]);
% weight_low is the lowest threshold and weight_high is the highest threshold for
% weighting matrix. 
% [WG] is the final 4D weighted matrix 

save data.mat phi mask WG