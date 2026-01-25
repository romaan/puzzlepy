def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    for price in prices:
        minPrice = min(minPrice, price) # Update min price seen
        maxProfit = max(maxProfit, price - minPrice) # Update max profit
    return maxProfit
