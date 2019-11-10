a,b = 0,1
while b<1000:
    print(b,end=",") #关键字end表示将结果输出到同一行，或者在输出末尾添加不同的字符
    a,b = b,a+b
'''
最后一行也可写为以下形式
m=b
n=a+b
a=m
b=n
'''