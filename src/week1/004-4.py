# 创建一个列表
my_list = [3, 1, 4, 1, 5, 9]

# 添加元素到列表
my_list.append(2)  # 在列表末尾添加 2
print("After append:", my_list)  # 输出: [3, 1, 4, 1, 5, 9, 2]

my_list.append(4)  # 在列表末尾添加 2
print("After append:", my_list)  # 输出: [3, 1, 4, 1, 5, 9, 2,4]



# 删除列表中的某个元素
my_list.remove(1)  # 删除列表中第一个出现的 1
print("After remove:", my_list)  # 输出: [3, 4, 1, 5, 9, 2,4]

# 修改列表中的某个元素
my_list[0] = 7  # 将第一个元素修改为 7
print("After modification:", my_list)  # 输出: [7, 4, 1, 5, 9, 2,4]

print("Index of 4:", my_list.index(4))  # 输出: 1

# 排序列表
my_list.sort()  # 升序排序
print("After sorting:", my_list)  # 输出: [1, 2, 4, 5, 7, 9]

# 查找元素
print("Index of 5:", my_list.index(5))  # 输出: 3
try:
    index = my_list.index(5,1,3)  # 在索引 1 和 3 之间查找 5
except ValueError as e:
    print("Value not found:",e)  # 输出: Value not found
    #print("Index of 6:", my_list.index(6))  # 输出: 3

# pop() 方法：移除并返回列表中的最后一个元素。
# 列表切片：获取列表的子列表。。

# 使用 pop() 移除并返回最后一个元素
print(my_list)  # 输出: [1, 2, 4, 5, 7, 9]
last_element = my_list.pop()  # 移除 9
print("After pop:", my_list)  # 输出: [1, 2, 4, 5, 7]
print("Popped element:", last_element)  # 输出: 9

print("Popped element:", my_list.pop())  # 输出: 
print("After pop:", my_list)

print("Popped element:", my_list.pop())  # 输出: 
print("After pop:", my_list)


# 列表切片
sub_list = my_list[1:4]  # 获取索引 1 到 3 的元素，索引 4 处的元素不包含
print("Sub-list:", sub_list)  # 输出: [2, 4, 5]
