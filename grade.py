# grade.py ———— Day4:if 判断
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
score = 95
if score >= 90:
    print("成绩优秀")
elif score >= 60:
    print("成绩良好")
else:
    print("成绩一般")
