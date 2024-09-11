# 1. 变量和数据类型
num1 = 10  # 整数
num2 = 20.5  # 浮点数
name = "Python学习"  # 字符串
is_learning = True  # 布尔类型

# 2. 基本运算符
sum_result = num1 + num2
diff_result = num2 - num1

# 3. 控制结构
if is_learning:
    print(f"正在学习{name}")
else:
    print("暂停学习")

# 4. 循环结构
for i in range(4):
    print(f"循环次数: 第{i}次循环")

# 5. 函数定义
def add_numbers(a, b):
    return a + b

# 调用函数
result = add_numbers(num1, num2)
print(f"两个数的和是: {result}")
