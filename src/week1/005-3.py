class BankAccount:
    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"存入 {amount} 元，账户余额: {self.balance} 元")

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足")
        else:
            self.balance -= amount
            print(f"取出 {amount} 元，账户余额: {self.balance} 元")

# 创建一个 BankAccount 对象
account = BankAccount("Alice", 100)

# 存入和取出金额
account.deposit(50)
account.withdraw(30)
account.withdraw(150)
