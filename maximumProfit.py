def isProfit(currentTime, currentValue):
    fiveSum = fourSum = tenSum = 0
    if 5 < currentTime:
        fiveSum = isProfit(currentTime-5,(currentTime-5)*1500)
    if 10 < currentTime:
        tenSum = isProfit(currentTime-10,(currentTime-10)*3000)
    if 4 < currentTime:
        fourSum = isProfit(currentTime-4,(currentTime-4)*1000)
    else:
        return currentValue
    return currentValue + max(fiveSum,fourSum, tenSum)
    
x = int(input("Enter Time Unit "))
print("Maximum Profit is ",isProfit(x, 0))

