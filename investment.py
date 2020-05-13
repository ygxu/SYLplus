amount = float(input("Enter amount: "))  # 数额
inrate = float(input("Enter Interest rate: "))  # 利率
period = int(input("Enter period: "))  # 期限
value = 0
year = 1
while year <= period:
        value = amount + (inrate * amount)
        print("Year {} Rs. {:.2f}".format(year, value))
        amount = value
        year = year + 1
