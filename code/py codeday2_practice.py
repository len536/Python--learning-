#定义变量：你的年龄（整数）、身高（小数）、姓名（字符串）、「还没想好学啥方向」（用 None 表示）
age=19
height=180.1666
name="冷"
ok=True
nothing=None
print(type(age),type(height),type(name),type(ok),type(nothing))


x=5
print(x,type(x))
x="hello"
print(x,type(x))

print(f"{name}的幸运数字是{age}")
print(f"{height}的值是{height:.2f}")
print(f"{name:>8}")

s="18"
print(s+"岁")
print(int(s)+1)

print(int(4.94444))
print(round(4.9444))

print(str(18)+"岁")
result=0.1+0.3
print(round(result,6)==0.4)

print("day2完工")


