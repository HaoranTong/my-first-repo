# 定义基本账户类
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} 存入 {amount} 元。余额: {self.balance} 元")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.owner} 取出 {amount} 元。余额: {self.balance} 元")
        else:
            print(f"{self.owner} 余额不足，无法取出 {amount} 元。")

    def get_balance(self):
        return self.balance


# 定义储蓄账户类
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)  # 调用父类构造函数
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"{self.owner} 获得利息 {interest} 元。余额: {self.balance} 元")


# 定义支票账户类
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=-500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= self.overdraft_limit:
            self.balance -= amount
            print(f"{self.owner} 取出 {amount} 元。余额: {self.balance} 元")
        else:
            print(f"{self.owner} 超出透支限额，无法取出 {amount} 元。")


# 创建储蓄账户和支票账户的实例
savings = SavingsAccount("Alice", 1000)
checking = CheckingAccount("Bob", 500)

# 测试储蓄账户
savings.deposit(500)
savings.add_interest()
savings.withdraw(200)

# 测试支票账户
checking.deposit(300)
checking.withdraw(900)  # 超过余额但不超过透支限额
checking.withdraw(100)  # 超出透支限额
