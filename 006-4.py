with open('new_file3.txt', 'r') as file:
    while True:
        line = file.readline()  # 每次读取一行
        if not line:  # 文件结束时退出循环
            break
        if "跳过" in line:  # 如果行包含特定关键字，跳过该行
            continue
        print(f"读取到的行: {line.strip()}")
