class Dog:
    def __init__(self, name,age):
        self.name = name  # 在类的构造函数中，self 指代当前对象
        self.age = age

    def get_name(self):
        return self.name  # 这里使用 self 来访问实例属性

dog = Dog("Buddy",6)  # 创建实例
print(dog.name,dog.age)  # 在类外部使用对象名访问属性，不需要 self
print(dog.get_name())  # 在类外部使用对象名访问方法，不需要 self