# 유클리드의 성질을 이용한 최대공약수
# [1] gcd(a, b) = gcd(b, a%b)
# [2] gcd(n, 0) = n

# ex)60과 24의 최대공약수
# gcd(60,24) = gcd(24, 60%24) = gcd(24,12) = gcd(12, 24%12) =gcd(12, 0) >>>12

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(60,24))