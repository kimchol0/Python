#while中使用break
n=5
while n>0:
    n-=1
    if n==2:
        break
    print(n)
print("循环结束。")
print("\n----------")
#while中使用continue
n=5
while n>0:
    n-=1
    if n==2:
        continue
    print(n)
print("循环结束。")