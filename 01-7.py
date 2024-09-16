numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_num = 0
for number in numbers:
    if number > max_num:
        max_num = number
result = (f"列表numbers中的最大值是:{max_num}")
print(result)  # 输出：列表numbers中的最大值是:9
