bags=int(input("Number of bags purchased:"))
price=5.50
if bags<25:
    discount=0.95
elif bags>=50:
    discount=0.80
elif bags>=75:
    discount=0.6

print(discount)
total=price*bags*discount
print(total)
