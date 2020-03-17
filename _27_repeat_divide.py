#재귀함수를 이용한 이분탐색

def repeat_divide(put_list, find_num, start, end):
    if start > end:
        return "X"

    mid = (start + end) // 2
    if find_num == put_list[mid]:
        return mid
    elif find_num > put_list[mid]:
        return repeat_divide(put_list, find_num, mid+1, end)    #찾는 범위가 변화해
    else:                                                       #위치가 바뀌는것이다
        return repeat_divide(put_list, find_num, start, mid-1)
    
    return "X"

def divide_find(put_list, find_num):
    return repeat_divide(put_list, find_num, 0, len(put_list)-1)

d = [1,4,9,16,25,36,49,64,81]
print(divide_find(d, 36))
print(divide_find(d, 4))
print(divide_find(d, 700))

    