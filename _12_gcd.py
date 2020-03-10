#최대공약수
def gcd(a,b):
    i = min(a,b)    #두수중 최솟값을 구하는 파이썬 함수
    while True:     #if문이 True가 될때까지 반복
        if a%i == 0 and b%i == 0:
            return i
        i = i - 1   #i를 1만큼 감소시키고 다시 다른 값들을 나눠줌

print(gcd(3,6))