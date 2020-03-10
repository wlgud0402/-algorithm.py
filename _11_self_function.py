def sum_number(n):
    if n <= 1:
        return 1
    return n + sum_number(n-1)

print(sum_number(10))

def find_max(n)