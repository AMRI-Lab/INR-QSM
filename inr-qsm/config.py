import argparse

class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser('INR-QSM-params')
        
    def initialize(self):
        self.parser.add_argument('--epoch', type=int, default=50, help='number of epoch for INR-QSM')
        self.parser.add_argument('--summary_epoch', type=int, default=1, help='number of epoch for printing')
        self.parser.add_argument('--predict_epoch', type=int, default=5, help='numpy of epoch for predicting')
        self.parser.add_argument('--start_block_epoch', type=int, default=0, help='number of epoch for starting phase compensation')
        self.parser.add_argument('--block_epoch', type=int, default=5, help='type of activation function')
        
        self.parser.add_argument('--gpu', type=int, default=3, help='gpu ID')
        self.parser.add_argument('--seed', type=int, default=1, help='seed ID')
        
        # data load
        self.parser.add_argument('--sub_name', type=str, default='testdata/data1/', help='subject folder')
        '''
            filename: data.mat
            keys: "phi", "mask", 'WG'
        '''
        self.parser.add_argument('--path_name', type=str, default='INRQSM_output', help='output folder, subfolder under `sub_name`')
        self.parser.add_argument('--patch_size', type=list, default=[96,96,48], help='patch size')
        self.parser.add_argument('--voxel_size', type=list, default=[1,1,2], help='voxel size')
        self.parser.add_argument('--B0_dir', type=list, default=[0,0,1], help='direction with respect to B0')
        self.parser.add_argument('--zero_ratio', type=float, default=0.3, help='minimum brain tissue portion')
        self.parser.add_argument('--pre_padmode', type=str, default='twoside', help='padding 0s in oneside or twoside')
        self.parser.add_argument('--pad_auto_cal', type=str, default='given', help='pad with 0s for better accuracy near boundary')
        self.parser.add_argument('--stride_portion', type=list, default=[1./3,1./3,1./3], help='portion of stride regarding patch size')
        
        # network and training
        self.parser.add_argument('--siren_flag', default=1) #no change
        self.parser.add_argument('--hidden_dim_num', type=int, default=512, help='number of neuron in first/hidden layer')
        self.parser.add_argument('--num_layers', type=int, default=10, help='number of layers')
        self.parser.add_argument('--w0', type=int, default=40, help='w0 value in first layer')
        self.parser.add_argument('--w0_hidden', type=int, default=40, help='w0 value in hidden layer')
        self.parser.add_argument('--w0_last', type=int, default=40, help='w0 value in last layer')
        self.parser.add_argument('--block_flag', default=1, help='whether or not use phase compensation')
        self.parser.add_argument('--pad_flag', default=1, help='whether or not use padding instead of patch-size kernel')
        self.parser.add_argument('--sub_block_dict_flag', default=2) #no change
        self.parser.add_argument('--block_sub_add_mode', type=str, default='update_measurement_sub') #no change
        self.parser.add_argument('--load_weight_flag', default=1, help='whether or not use transfer learning')
        self.parser.add_argument('--load_weight_path', type=str, default='transfer_learning/pre_trained_weight_for_transfer_learning.pkl', help='path of transfer-learning weight')
        self.parser.add_argument('--star_lr', type=float, default=1e-5, help='starting learning rate')
        self.parser.add_argument('--end_lr', type=float, default=0.02e-5, help='final learning rate')
        
        self.parser.add_argument('--weight_TV_flag', default=1, help='whether of not use gradient weighted matrix in loss')
        self.parser.add_argument('--TV_weight', type=float, default=0.15, help='TV weighting')
        self.parser.add_argument('--gd_weight', type=float, default=1.0, help='gd weighting')
        self.parser.add_argument('--L1L2_TV_flag', type=str, default='L2', help='L1/L2 loss for TV loss')
        self.parser.add_argument('--L1L2_gd_flag', type=str, default='L2', help='L1/L2 loss for gd loss')
        
    def parse(self):
        self.initialize()
        return self.parser.parse_args()
    
