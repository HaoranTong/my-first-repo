import random

# 定义包含各种字符类型的字符串
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_characters = "!@#$%^&*()"

#组合所有字符类型
all_characters = uppercase_letters + lowercase_letters + digits + special_characters

#创建一个空字符串用于存储密码
password = ""

# 在一个循环中，随机选择一个字符添加到密码字符串中，循环12次
for i in range(12):
    password += random.choice(all_characters)

# 打印生成的密码
print("建议密码：", password)
print("提醒把密码和账号一起保存哦！")
