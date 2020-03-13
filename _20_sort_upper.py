d = [2, 4, 5, 1, 3]
def sel_sort(put_list):
    n = len(put_list)
    for i in range(0, n-1):
        max_idx = i
        for j in range(i+1, n):
            if put_list[j] > put_list[max_idx]:
                max_idx = j
        put_list[i], put_list[max_idx] = put_list[max_idx], put_list[i]

sel_sort(d)
print(d)