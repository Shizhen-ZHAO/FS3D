#!/usr/bin/env bash

CUDA_VISIBLE_DEVICES=6 python tools/train.py \
./configs/prototypical_votenet/train_together/prototypical_votenet_8x8_scannet-3d-18class_0_3.py --sample_num 16 --work_path work_path/scannet_split0_shot3_1

#####Finetuning Stage#####
CUDA_VISIBLE_DEVICES=6 python tools/train.py \
./configs/prototypical_votenet/train_ftl_meta_vote/prototypical_votenet_8x8_scannet-3d-18class_0_3_mv.py --ft part --stage finetuning --work_path work_path/scannet_split0_shot3_1 --load_from ./work_path/scannet_split0_shot3_1/prototypical_votenet_8x8_scannet-3d-18class_0_3/epoch_32.pth
