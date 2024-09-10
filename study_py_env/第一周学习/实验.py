person = {"name": "Alice", "age": 30}
print(person.keys())  # 输出: dict_keys(['name', 'age'])
person = {"name": "Alice", "age": 30}
age = person.pop("age")  # 删除 "age" 键并返回 30
print(person)  # 输出: {'name': 'Alice'}
print(age)  # 输出: 30
