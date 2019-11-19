list=[1,2,3,4]
it=iter(list) #创建迭代器对象
print("输出迭代器的下一个元素：",next(it)) #输出迭代器的下一个元素
print("输出迭代器的下下个元素：",next(it)) #输出迭代器的下一个元素
print("利用for循环遍历之后的迭代器元素：",end=" ")
for x in it: #for循环遍历之后的迭代器元素
    print(x,end=" ")

print("\n----------")

import sys #引入sys模块
list2=[1,2,3,4]
it2=iter(list2) #创建迭代器对象
while True:
    try:
        print(next(it2),end=" ")
    except StopIteration:
        sys.exit()