#创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter),end=" ")
print(next(myiter),end=" ")
print(next(myiter),end=" ")
print(next(myiter),end=" ")
print(next(myiter),end=" ")

print("\n----------")

#在 20 次迭代后停止执行
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x,end=" ")