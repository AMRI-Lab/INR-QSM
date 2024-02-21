# INR-QSM
A subject-specific unsupervised deep learning approach for QSM (quantitative susceptibility mapping) reconstruction using implicit neural representation.
## Features   
**(1)** A new signal representation scheme for QSM recon which maps the susceptbility value as an implicit function of the coordinate;  
**(2)** The non-local phase effect is considered for the first time in the patch-based QSM deep learning method;  
**(3)** The proposed method is subject-specific and unsupervised, indicating that it is free of generalization problems and the requirement of a large dataset, which are two issues in the supervised deep learning methods;  
**(4)** Several acceleration strategies are adopted to accelerate the training process.

## Usage
**(step 1)** Generating test data `data.mat` containing `phi`, 'msk', 'WG' based on files in `data_prep` folder;  
**(step 2)** Adjusting the `config.py` by inputting correct voxelsize, B0_dir, patch size, and other parameters;  
**(step 3)** Running `main.py` for generating INR-QSM output.

## Note
Feel free to contact mingzhang.bme@sjtu.edu.cn for any questions.


