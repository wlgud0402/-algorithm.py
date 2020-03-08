#32p예제
#1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램
def sum_square(n):
    s = 0
    for i in range(1,n+1):
        s = s + i*i
    return s

print(sum_square(10))

def sum_square2(n):
    return n * (n+1) * ((2*n)+1) //6

print(sum_square2(10))