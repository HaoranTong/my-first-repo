# 初始化一个空字典来存储日报数据
daily_report = {}

# 无限循环，直到用户选择退出
while True:
    # 显示操作选项
    print("请选择操作：")
    print("1. 输入日报内容")
    print("2. 查看日报内容")
    print("3. 退出程序")
    
    # 获取用户选择
    choice = input("请输入选项编号（1-3）：")
    
    # 根据用户选择执行相应操作
    if choice == "1":
        date = input("请输入日期（格式：YYYY-MM-DD）：")
        content = input("请输入日报内容：")
        daily_report[date] = content
        print("日报内容已保存。")
    elif choice == "2":
        date = input("请输入要查看的日期（格式：YYYY-MM-DD）：")
        if date in daily_report:
            print("日报内容：", daily_report[date])
        else:
            print("该日期的日报内容不存在。")
    elif choice == "3":
        print("程序已退出。")
        break  # 退出循环，结束程序
    else:
        print("无效的选项编号，请重新输入。")
