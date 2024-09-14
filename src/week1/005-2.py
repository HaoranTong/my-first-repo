def number_pairs(limit):
    for i in range(1, limit+1):
        yield i, i**2

# 创建一个生成器对象，用于生成数字和它们的平方
pairs = number_pairs(5)
print(next(pairs))

# 使用列表存储生成的键值对
pair_list = list(number_pairs(5))
# 使用元组存储生成的键值对
#pair_tuple = tuple(number_pairs(5))
# 使用字典将列表转化为一个映射，将数字与其平方对应
pair_dict = {key: value for key, value in pair_list}

print("生成的列表:", pair_list)
#print("生成的元组:", pair_tuple)
print("生成的字典:", pair_dict)
