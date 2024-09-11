def calculate_sum(n):
    sums = 0
    for i in range(1, n+1):  # 包括 n 本身
        sums += i
    return sums

# 获取用户输入
while True:
    i = input("请输入一个整数：")
    try:
        i = int(i)
        break
    except ValueError:
        print("输入错误，请输入一个整数！")
# 调用函数并输出结果
sum1 = calculate_sum(int(i))
print(f"从1加到{i}的和是：{sum1}")
