# main.py
# import mymodule

# print(mymodule.greet("Alice"))  # 输出: Hello, Alice!

from mymodule import greet
print(greet("Bob"))  # 输出: Hello, Bob!

try:
    from mymodule import greet
    print(greet("Bob"))  # 输出: Hello, Bob!
    