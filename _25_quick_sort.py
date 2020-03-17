#quick sort 재귀사용

def quick_sort(put_list):
    n = len(put_list)
    if n<=1:
        return put_list
    standard = put_list[-1]

    group_1 =[]
    group_2 =[]
    
    for i in range(0, n-1):
        if put_list[i] < standard:
            group_1.append(put_list[i])
        else:
            group_2.append(put_list[i])
    
    return quick_sort(group_1) + [standard] + quick_sort(group_2)

d = [6,8,3,9,10,1,2,4,7,5]

print(quick_sort(d))