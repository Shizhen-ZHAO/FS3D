_base_ = [
    '../../_base_/datasets/fs_scannet/split0_fs/scannet-3d-18class_5_shot.py', '../../_base_/models/prototypical_votenet.py',
    '../../_base_/schedules/schedule_3x-fs.py', '../../_base_/default_runtime.py'
]

# model settings
model = dict(
    bbox_head=dict(
        num_classes=18,
        bbox_coder=dict(
            type='PartialBinBasedBBoxCoder',
            num_sizes=18,
            num_dir_bins=1,
            with_rot=False,
            mean_sizes=[[0.76966727, 0.8116021, 0.92573744],
                        [1.876858, 1.8425595, 1.1931566],
                        [0.61328, 0.6148609, 0.7182701],
                        [1.60902004, 1.58128208, 0.90361559],
                        [0.97949594, 1.0675149, 0.6329687],
                        [0.531663, 0.5955577, 1.7500148],
                        [1.05553907, 1.31581702, 1.2656445],
                        [1.06356644, 2.74768757, 1.37541882],
                        [0.21132214, 0.4206159, 0.5372846],
                        [1.4440073, 1.8970833, 0.26985747],
                        [1.0294262, 1.4040797, 0.87554324],
                        [1.3766412, 0.65521795, 1.6813129],
                        [0.6650819, 0.71111923, 1.298853],
                        [0.41999173, 0.37906948, 1.7513971],
                        [0.55121669, 0.67342385, 0.75326565],
                        [0.50867593, 0.50656086, 0.30136237],
                        [0.92678109, 1.24428201, 0.47475251],
                        [0.40749664, 0.51440984, 0.5975826]])))

# yapf:disable
log_config = dict(interval=30)
# yapf:enable
load_from = None