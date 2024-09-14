# 父类（基类）：Employee
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_monthly_salary(self):
        # 父类的基本月薪计算方法
        return self.base_salary
    
    def show_details(self):
        print(f"员工姓名: {self.name}, 基本工资: {self.base_salary}")
        
# 子类：全职员工 FullTimeEmployee
class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)  # 调用父类的构造函数
        self.bonus = bonus
    
    def calculate_monthly_salary(self):
        # 重写父类的方法，包含奖金计算
        return self.base_salary + self.bonus
    
    def show_details(self):
        # 扩展父类的方法，显示更多信息
        super().show_details()  # 调用父类的 show_details 方法
        print(f"奖金: {self.bonus}")

# 子类：兼职员工 PartTimeEmployee
class PartTimeEmployee(Employee):
    def __init__(self, name, base_salary, hours_worked, hourly_rate):
        super().__init__(name, base_salary)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def calculate_monthly_salary(self):
        # 兼职员工的月薪按工作时长计算
        return self.hours_worked * self.hourly_rate
    
    def show_details(self):
        super().show_details()
        print(f"工作时长: {self.hours_worked}, 时薪: {self.hourly_rate}")

# 使用示例
full_time_employee = FullTimeEmployee("Alice", 3000, 500)
part_time_employee = PartTimeEmployee("Bob", 0, 80, 15)

# 调用子类的方法
full_time_employee.show_details()
print(f"全职员工月薪: {full_time_employee.calculate_monthly_salary()} 元")
print("------")
part_time_employee.show_details()
print(f"兼职员工月薪: {part_time_employee.calculate_monthly_salary()} 元")
