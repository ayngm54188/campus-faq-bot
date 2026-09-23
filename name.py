# name.py —— Day 3：变量

import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# 定义变量
name = "李云璟"
age = 18
school = "合肥工业大学"
major = "信管创新实验班"

# 使用变量
print("我叫" + name)
print("今年" + str(age) + "岁")
print("就读于" + school)
print("专业：" + major)
