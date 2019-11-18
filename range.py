#遍历数字序列
for i in range(10):
    print(i,end=" ")
print("\n----------")
#遍历指定区间的值
for i in range(0,20):
    print(i,end=" ")
print("\n----------")
#以指定数字开始并指定不同的增量（甚至可以为负数，也叫做“步长”）
for i in range(0,10,3):
    print(i,end=" ")
print("\n----------")
#负数
for i in range(-10,-100,-30):
    print(i,end=" ")
print("\n----------")
#创建一个列表
createlist=list(range(5))
print(createlist)