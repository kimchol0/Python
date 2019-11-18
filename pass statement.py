"""
pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句
"""
#以下实例在字母为o时执行pass语句块

for letter in "Runoob":
    if letter=="o":
        pass
        print("执行pass块")
    print("当前字母：",letter)
print("Good Bye!")
