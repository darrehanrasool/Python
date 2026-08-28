## Bill Amount 
prices=[10,7,5,8,6]
quantity=[1,2,3,1,1]
total=0
for i in range(len(prices)):
    total=total+prices[i]*quantity[i]

print(total)