for letter in "Runoob":#第一个实例
    if letter == "b":
        break
    print("当前字母为：",letter)

var=10 #第二个实例
while var>0:
    print("当前变量值为：",var)
    var = var-1
    if var==5:
        break
print("Good Bye!")

print("\n----------")
#以下实例循环字符串Runoob，碰到字母o跳过输出
for letter in "Runoob": #第三个实例
    if letter=="o":
        continue
    print("当前字母：",letter)
var=10 #第四个实例
while var>0:
    var = var-1
    if var==5: #变量为5时跳过输出
        continue
    print("当前变量值：",var)
print("Good Bye!")