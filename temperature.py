fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8 # 转换成摄氏度
    print("{:5d}{:7.2f}".format(fahrenheit,celsius))
    fahrenheit += 25
