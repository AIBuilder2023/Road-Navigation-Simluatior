import imageio
from attributes import *
from pathlib import Path
from tqdm import tqdm
from time import time,localtime,strftime
from attributes import *

def count_files_in_directory(directory):
    # 确保路径存在
    if not Path(directory).exists():
        return 0
    # 使用glob模式匹配所有文件（不包括子目录中的文件）
    file_count = len(list(Path(directory).glob('*'))) - len(list(Path(directory).glob('*/')))
    return file_count


# 示例使用
directory_path = Path("logs/frames")
file_count = count_files_in_directory(directory_path)
print("total frames:",file_count)


frames = []
for t in tqdm(range(file_count-1)):
    frames.append(imageio.imread(f"logs/frames/frame{t*FRAMES_PER_OUTPUT}.png"))

imageio.mimsave(f"logs/gif/traffic-{strftime('%Y%m%d-%H%M%S', localtime(time()))}.gif", frames, fps=FPS)