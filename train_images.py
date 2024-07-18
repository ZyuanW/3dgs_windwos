import os
import subprocess

# images_set_path
images_path = r"D:\gitlab2024\gaussian-splatting\data\ggbond\input"

# last folder path
folder_path = os.path.dirname(images_path)

# script
# COLMAP script predict camera pose
command = f'python convert.py -s {folder_path}'
subprocess.run(command, shell=True)
# model training script, the model will be saved in the output path
command = f'python train.py -s {folder_path}'
subprocess.run(command, shell=True)
