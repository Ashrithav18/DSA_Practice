def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # update minimum price
        min_price = min(min_price, price)
        
        # calculate profit
        profit = price - min_price
        
        # update max profit
        max_profit = max(max_profit, profit)
    
    return max_profit


# Function Call
prices = [7,1,5,3,6,4]
print(maxProfit(prices))   # Output: 5