d = [2,4,5,1,3]
#제일 작은것들부터 찾음
def find_min_idx(put_list):
    n = len(put_list)
    min_idx = 0
    for i in range(1, n):
        if put_list[i] < put_list[min_idx]:  #리스트1번째항이 0번째항보다 작다면
            min_idx = i     #리스트 최고 작은항은 i번째항
    return min_idx

def sel_sort(put_list):
    new_list = []
    while put_list:
        min_idx = find_min_idx(put_list)
        value = put_list.pop(min_idx)
        new_list.append(value)
    return new_list

print(sel_sort(d))