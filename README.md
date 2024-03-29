# INR-QSM
This repo contains Matlab codes for generating input data and python codes for running INR-QSM. 

## Brief introduction 
A subject-specific unsupervised deep learning approach for QSM (quantitative susceptibility mapping) reconstruction using implicit neural representation (INR).

## Feature   
*  A new signal representation scheme for QSM recon which maps the susceptbility value as an implicit function of coordinates
*  The non-local phase effect is considered in patch-based QSM deep learning method 
*  The proposed method is subject-specific and unsupervised, indicating that it is free of generalization problems and the requirement of a large dataset, which are two issues in supervised deep learning methods
*  Several acceleration strategies are adopted to accelerate training process

## Setup   
* STISuite 3.0
* PyTorch 1.11.0  
* Python 3.8

## Usage
**Data preparation**
1.  Generate test data `data.mat` containing `phi`, `msk`, `WG` based on files in `data_prep` folder 
2.  Adjust the `config.py` by inputting correct `voxel size`, `B0_dir`, `patch size`, and other parameters 

**Training and prediction**

3.  Run `main.py` for generating INR-QSM output

## Contact
Feel free to contact `zhangming430424@gmail.com` or `mingzhang.bme@sjtu.edu.cn` for questions/discussions/suggestions.


