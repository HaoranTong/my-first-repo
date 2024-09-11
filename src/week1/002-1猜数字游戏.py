import random

# 随机生成一个1到100之间的数字
secret_number = random.randint(1, 100)
guess = None
print(secret_number)


# 当用户没有猜对时继续循环
while guess != secret_number:
    # 获取用户输入
    guess = int(input("请输入你猜的数字（1到100之间）(或输入0退出)："))
    if guess == :
        break
    if guess < secret_number:
        print("你猜的数字太小了！")
    elif guess > secret_number:
        print("你猜的数字太大了！")
    else:
        print("恭喜你，猜对了！")
