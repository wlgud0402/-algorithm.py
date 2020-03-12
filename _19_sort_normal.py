#new_list 에 넣는게 아니라 리스트 안에서 직접 자료의 위치를 바꾸면서 정렬

d = [2, 4, 5, 1, 3]
def sel_sort(put_list):
    n = len(put_list)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if put_list[j] < put_list[min_idx]:
                min_idx = j
        put_list[i], put_list[min_idx] = put_list[min_idx], put_list[i]

sel_sort(d)
print(d)