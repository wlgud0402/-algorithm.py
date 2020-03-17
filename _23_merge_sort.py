#병합정렬
#그룹을 두개로 나누고 정렬해서 정렬된것끼리 비교해 최종 리스트에 넣어줌

def merge_sort(put_list):
    n = len(put_list)
    if n <= 1:
        return put_list

    #그룹을 나누어 각각 병합정렬을 호출하는 과정
    mid = n//2 
    group_1 = merge_sort(put_list[:mid])
    group_2 = merge_sort(put_list[mid:])

    result = []
    
    while group_1 and group_2:
        if group_1[0] < group_2[0]:
            result.append(group_1.pop(0))
        else:
            result.append(group_2.pop(0))
    
    while group_1:
        result.append(group_1.pop(0))
    while group_2:
        result.append(group_2.pop(0))
    
    return result

put_list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(put_list))