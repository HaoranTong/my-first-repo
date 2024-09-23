import os
import glob
from datetime import datetime

def rename_files(folder_path):
    # 获取文件夹中所有JPG文件的路径
    png_files = glob.glob(os.path.join(folder_path, '*.png'))
    
    # 获取每个文件的创建时间，并存储在一个列表中
    files_with_time = []
    for file in png_files:
        creation_time = os.path.getctime(file)
        files_with_time.append((file, creation_time))
    
    # 按照创建时间排序
    files_with_time.sort(key=lambda x: x[1])
    
    # 生成新的文件名，并重命名文件
    for index, (file, _) in enumerate(files_with_time, start=1):
        new_name = f"python学习PPT{index:02d}.png"
        new_path = os.path.join(folder_path, new_name)
        os.rename(file, new_path)
        print(f"重命名: {file} -> {new_path}")

# 指定文件夹路径
folder_path = r"C:\Users\Haora\Desktop\PPT图片文件夹"
rename_files(folder_path)