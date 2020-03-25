#최대수익

def max_profit(prices):
    n = len(prices)
    max_profit = 0
    min_prices = prices[0]

    for i in range(1, n):
        profit = prices[i] - min_prices

        if profit > max_profit:
            max_profit = profit
        
        if prices[i] < min_prices:
            min_prices = prices[i]

    return max_profit

prices = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

print(max_profit(prices))