# 父类：Vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print(f"{self.brand} {self.model} 正在启动...")
    
    def stop(self):
        print(f"{self.brand} {self.model} 已经停止。")
    
    def info(self):
        return f"{self.year} {self.brand} {self.model}"

# 子类：Car
class Car(Vehicle):
    def __init__(self, brand, model, year, seating_capacity):
        super().__init__(brand, model, year)  # 调用父类的构造函数
        self.seating_capacity = seating_capacity
    
    def info(self):
        base_info = super().info()  # 调用父类的方法
        return f"{base_info}, 座位数: {self.seating_capacity}"
    
    def honk(self):
        print("汽车喇叭：嘟嘟！")

# 子类：Truck
class Truck(Vehicle):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)  # 调用父类的构造函数
        self.load_capacity = load_capacity
    
    def info(self):
        base_info = super().info()  # 调用父类的方法
        return f"{base_info}, 载重能力: {self.load_capacity} 吨"
    
    def honk(self):
        print("卡车喇叭：嗡嗡！")

car = Car("Toyota", "Corolla", 2018, 5)
truck = Truck("Isuzu", "NQR", 2015, 3)
print(car.info())
car.start()
car.honk()
car.stop()
print(truck.info())
truck.start()
truck.honk()

# Output: