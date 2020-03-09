v = [17,92,18,33,58,7,33,42]

def find_max(a):
    n = len(a)    
    max_v = a[0]         #리스트의 첫번째 값을 최댓값으로 기억>기준
    for i in range(1,n):    #첫번째 값을 정해놨으므로 비교는 두번째 수부터>>[0],[1]
        if a[i] > max_v:    #이번값이 현재까지 기억된 최댓값보다 크면 최댓값을 변경
            max_v = a[i]
    return max_v

print(find_max(v))

