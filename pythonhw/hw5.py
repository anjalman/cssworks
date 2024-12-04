price = [7,1,3,2,5,4,6]
profit = 0
for i in range(len(price)-1):
    for j in range(i+1,len(price)):
        if price[i] < price [j] :
            dif =  price[j] - price[i]
            if dif > profit:
                profit = dif
print(profit)