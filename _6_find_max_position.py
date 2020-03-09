#최댓값의 위치를 구하는 알고리즘
v = [17,92,18,33,58,7,33,42]

def find_max_idx(a):
    n = len(a)    
    max_idx = 0                 #리스트중 0번 위치를 최댓값 위치로 기억
    for i in range(1,n):        #
        if a[i] > a[max_idx]:   #최댓값의 위치를 변경
            max_idx = i
    return max_idx

print(find_max_idx(v))

