#For循环，break语句用于跳出当前循环体
sites=["Baidu","Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程")
        break
    print("循环数据：" + site)
else:
    print("没有循环数据！")
print("完成循环！")