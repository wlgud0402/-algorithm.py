#삽입정렬을통해 리스트 안에서 직접 위치를 바꿈
#파괴적
#처음 리스트 와 나중에 만들어진 리스트는 같지 않다

def ins_sort(put_list):
    n = len(put_list)
    for i in range(1, n):
        key = put_list[i]
        j = i - 1
        while j >= 0 and put_list[j] > key:
            put_list[j + 1] = put_list[j]
            j -= 1
        put_list[j + 1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)