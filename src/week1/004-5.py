# 创建一个字典
my_dict = {'Alice': 85, 'Bob': 90, 'Charlie': 78}


# 访问字典中的值
# print("Alice's score:", my_dict['Alice'])  # 输出: Alice's score: 85

# 添加新的键值对
my_dict['David'] = 92  # 添加 David 的成绩
print("After adding David:", my_dict)  # 输出: {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}

# 修改键值对
my_dict['Alice'] = 88  # 修改 Alice 的成绩
print("After modifying Alice's score:", my_dict)  # 输出: {'Alice': 88, 'Bob': 90, 'Charlie': 78, 'David': 92}

# 删除键值对
del my_dict['Charlie']  # 删除 Charlie 的成绩
print("After deleting Charlie:", my_dict)  # 输出: {'Alice': 88, 'Bob': 90, 'David': 92}

# pop() 方法：移除并返回指定键的值。
# items()、keys()、values()：获取字典的键、值或键值对。
# 使用 pop() 移除键值对
bob_score = my_dict.pop('Bob')  # 移除 Bob 的成绩
print("After pop:", my_dict)  # 输出: {'Alice': 88, 'David': 92}
print("Bob's score:", bob_score)  # 输出: 90

# 获取字典中的所有键、值、键值对
print("Keys:", my_dict.keys())  # 输出: Keys: dict_keys(['Alice', 'David'])
print("Values:", my_dict.values())  # 输出: Values: dict_values([88, 92])
print("Items:", my_dict.items())  # 输出: Items: dict_items([('Alice', 88), ('David', 92)])
