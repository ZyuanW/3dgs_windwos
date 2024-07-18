import os
import subprocess


# video path
video_path = r"C:\Users\ziyuanw\Desktop\gaussian-splatting\gaussian-splatting\data\ggbond\ggbond.mp4"
# split frame number, how many frames per second
fps = 2


# get current working directory
current_path = os.getcwd()

# last folder path
folder_path = os.path.dirname(video_path)

# images_save_path
images_path = os.path.join(folder_path, 'input')
os.makedirs(images_path, exist_ok=True)

ffmpeg_path = os.path.join(current_path, 'external', r'ffmpeg/bin/ffmpeg.exe')

# script
# video to images
command = f'{ffmpeg_path} -i {video_path} -qscale:v 1 -qmin 1 -vf fps={fps} {images_path}\\%04d.jpg'
subprocess.run(command, shell=True)

# COLMAP script predict camera pose
command = f'python convert.py -s {folder_path}'
subprocess.run(command, shell=True)

# model training script, the model will be saved in the output path
command = f'python train.py -s {folder_path}'
subprocess.run(command, shell=True)
