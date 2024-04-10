litres = 0
price = 0
name = str(input('Do you want the number of litres for that price or the price for that litres'))
value = float(input('please input the values '))
if name == 'litres' :
    o = value / 92.95

elif name == 'price' :
    o = value * 92.95
print(o)

