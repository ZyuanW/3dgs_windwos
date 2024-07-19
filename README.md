# 3DGS Setup on Windows
This project mainly implements code deployment based on the following work: https://github.com/jonstephens85/gaussian-splatting-Windows
## Cloning this repo
```
git clone https://github.com/ZyuanW/3dgs_windwos.git
```

## Setup Conda env
dowload following environment file

### link for conda env
```
https://drive.google.com/file/d/1OdMW1Zjc9jD4x9nY9CP9oEJx7iPod4AV/view?usp=sharing
```
unzip the envs.7z

copy `/envs/gaussian_splatting` to the path of conda envs

### activate envs
`conda activate gaussian_splatting`

## Run

### input data
input data should be video under `3dgs_winows/data`   
video path: `~/3dgs_windows/data/video`

### train_video.py
This scirpt will first generate a folder called input at the `video path`, use ffmpeg to splite the video to sequence frames.   
Then use colmap to predict the camera pose and initial point cloud, this will save to `3dgs_windows/output`.   
It will automatically start training, and will save at 7k steps and end at 30k steps, output to `3dgs_windows/output/xxx/point_cloud/`.

### train_images.py
This script is basically use sequences frames as input data. If you already have sequences frames, use this.



