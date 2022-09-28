import os
import sys
cmd = "python -m torch.distributed.launch --nproc_per_node=<number of gpus per node> --master_port=<any_value>  --use_env main_clean.py \
--model deit_tiny_patch16_224 --batch-size=16 --data-path <imagenet_path>  --epoch 100  \
--reprob 0  --no-repeated-aug --drop 0 --drop-path 0 --start_epoch 0 --warmup-epochs 5 --adjust_lr 512  \
--aa 'rand-m9-mstd0.5-inc1' --output_dir save/deit_normal/deit_tiny_patch16_224_v2"

os.system(cmd)
