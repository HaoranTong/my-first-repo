# main1.py
# 从包中导入模块
# import mypackage.module1 as module1
# import mypackage.module2 as module2 

# print(module1.add(5, 3))        # 输出: 8
# print(module2.subtract(5, 3))   # 输出: 2

#从包的模块中直接导入函数
from mypackage.module1 import add
from mypackage.module2 import subtract

print(add(5, 3))        # 输出: 8
print(subtract(5, 3))   # 输出: 2


