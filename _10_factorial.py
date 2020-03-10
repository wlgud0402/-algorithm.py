def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)    #fact 안에 fact를 넣어놈 재귀함수

print(fact(1))
print(fact(5))

