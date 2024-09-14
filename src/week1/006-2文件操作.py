# 使用 'w' 模式，并指定编码为 UTF-8
with open('new_file.txt', 'w', encoding='utf-8') as file:
    file.write('这是一个新创建的文件，内容已写入。\n')

print("文件已创建并写入内容。")
