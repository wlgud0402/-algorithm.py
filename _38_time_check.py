#최대수익을 찾는 알고리즘에서 n 과 n2 의 차이
import time
import random


def max_profit_slow(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]

            if profit > max_profit:
                max_profit = profit
    
    return max_profit

def max_profit_fast(prices):
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

def test(n):
    a = []
    for i in range(0,n):
        a.append(random.randint(5000,20000))
    
    start = time.time()
    mps = max_profit_slow(a)
    end = time.time()
    time_slow = end - start

    start = time.time()
    mpf = max_profit_fast(a)
    end = time.time()
    time_fast = end - start

    print(n, mps, mpf)

    m = 0
    if time_fast > 0:
        m = time_slow / time_fast
    
    print(n, time_slow, time_fast, m)

test(100)
test(1000)
test(10000)