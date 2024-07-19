import subprocess

# output_path
model_path = r'C:\Users\ziyuanw\Desktop\gaussian-splatting\output'

# start the viewer
command = f'SIBR_gaussianViewer_app.exe -m {model_path}'
run_path = 'external/viewers/bin'
subprocess.run(command, shell=True, cwd=run_path)
