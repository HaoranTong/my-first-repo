while True:
    try:
        x = input("请输入被除数: ")
        y = input("请输入除数: ")
        x = int(x)  # 将被除数转换为整数
        y = int(y)  # 将除数转换为整数
        z = x / y   # 执行除法运算
        print(f"{x} 除以 {y} 的结果是：{z}")
        break  # 如果没有异常，跳出循环
    except ValueError:
        print("请输入有效的数字。")
    except ZeroDivisionError:
        print("除数不能为0。")
    finally:
        print("程序执行完毕")
