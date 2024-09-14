# 基类
class Animal:
    def speak(self):
        raise NotImplementedError("子类必须实现这个方法")

# 子类
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 创建实例
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # 不同对象通过相同接口表现不同的行为
