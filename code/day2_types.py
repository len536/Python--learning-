# ==============================
# day2_types.py —— Day 2：变量与基本类型
# 运行：py code\day2_types.py
# ==============================

# --- 一、五大类型逐个见面 ---
n = 42            # int：整数，任意大、不溢出
pi = 3.14159      # float：浮点（精度是 C 的 double 级）
name = "冷"        # str：字符串，单双引号等价
ok = True         # bool：注意首字母大写！小写 true 是 NameError
nothing = None    # NoneType：空值，相当于 Java 的 null

print(type(n), type(pi), type(name), type(ok), type(nothing))
# <class 'int'> <class 'float'> <class 'str'> <class 'bool'> <class 'NoneType'>

# --- 二、变量是标签不是盒子：动态类型 ---
x = 5             # 标签 x 贴在整数 5 上
print(x, type(x)) # 5 <class 'int'>
x = "hello"       # 撕下来贴到字符串上 —— C/Java 里这是编译错误
print(x, type(x)) # hello <class 'str'>

# --- 三、f-string 格式化 ---
print(f"{name} 的幸运数是 {n}")
print(f"pi 保留两位 = {pi:.2f}")     # 四舍五入到 3.14
print(f"[{name:>8}]")                # 右对齐占 8 格（中文占 2 格，实际显示会宽些）
print(f"pi 的值：{pi=}")             # 调试神器：变量名和值一起输出

# --- 四、类型转换（拆箱）---
s = "18"
print(s + "岁")      # 字符串拼接 OK："18岁"
# print(s + 1)       # TypeError：str 不能直接 + int，别开这行
age = int(s)         # int() 把字符串翻译成数字
print(age + 1)       # 19，数字运算 OK
print(int(3.99))     # 3！直接砍尾巴，不是四舍五入
print(round(3.99))   # 4，round 才是四舍五入
print(str(18) + "岁")  # str() 把数字变字符串

# --- 五、float 精度坑（经典面试题）---
result = 0.1 + 0.2
print(result)                    # 0.30000000000000004 ！
print(result == 0.3)             # False ！
print(round(result, 6) == 0.3)   # True —— 比较浮点前先 round

# --- 六、bool 是 int 的子类 ---
print(True + True)               # 2，True 就是 1
print(isinstance(True, int))     # True，亲儿子认证
print(sum([True, False, True]))  # 2，数 True 个数的惯用技巧

# --- 七、input()：永远返回 str（本节最大坑）---
birth = input("输入你的出生年份：")   # 敲 2007
# print(birth + 18)               # TypeError：birth 是 str！
birth = int(birth)               # 拆箱成整数
print(f"2026 - 出生年 = {2026 - birth} 岁")

print("day2 完工")
