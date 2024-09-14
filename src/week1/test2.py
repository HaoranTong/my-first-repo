# 父类：Animal
class Animal:
    def __init__(self, name):
        self.name = name

    # # 父类提供一个通用的接口
    # def speak(self):
    #     raise NotImplementedError("子类必须实现该方法")

# 子类：Dog
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# 子类：Cat
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# 实例化不同的子类对象
dog = Dog("Buddy")
cat = Cat("Whiskers")

# 通过父类的引用来调用子类的实现
animals = [dog, cat]

for animal in animals:
    print(animal.speak())
