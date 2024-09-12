# 创建一个字典
student_grades = {'Ailice':80, 'Bob':98, 'Charlie':78, 'David':"qw"}

# 查询成绩
print(f"Ailice'sgrade is: {student_grades['Ailice']}")

# 更新一个成绩
student_grades['Ailice'] = 95
print(f"Ailice's updated grade is: {student_grades['Ailice']}")

# 删除一个学生记录
del student_grades['Charlie']
print(f"Updated grades: {student_grades}")
