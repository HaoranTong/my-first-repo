class Dog:
    def __init__(self, name):
        self.name = name  # self.name 存储的是一个指向 "Buddy" 的内存地址


dog1 = Dog("Buddy")
dog2 = Dog("ADD")

print(dog1.name)  # 输出 "Buddy"
print(dog2.name)  # 输出 "Buddy"

# 修改 dog2 的属性
dog2.name = "Max"
print(dog1.name)  # 输出 "Max"（dog1 和 dog2 指向同一个对象，属性共享）
print(dog2.name)  # 输出 "Max"（dog1 和 dog2 指向同一个对象，属性共享）
