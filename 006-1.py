import os

if not os.path.exists('new_file1.txt'):
    with open('new_file1.txt',"w", encoding="utf-8") as file:
        file.write('这是新创建的另外一边文件，内容已写入。\n')
    print("文件已创建并写入内容。")
else:
    with open('new_file1.txt',"a", encoding="utf-8") as file:
        file.write('这是已经存在的文件，内容已追加。\n')
    print("文件已存在，追加内容。")
    
