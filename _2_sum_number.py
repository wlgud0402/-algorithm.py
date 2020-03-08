#1부터 n까지의 합 구하기
def sum_number(abc):
    s = 0   
    for i in range(1,abc+1):
        s = s+i
    return s

print(sum_number(10))

def sum_number2(abc):           #가우스식>>1부터 n까지의 합 =  n * (n+1) //2
    return(abc* (abc+1) //2)
print(sum_number2(100))

