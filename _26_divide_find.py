#이분탐색

def divide_find(put_list, find_num):
    start = 0
    end = len(put_list) -1

    while start <= end:
        mid = (start + end) //2
        if find_num == put_list[mid]:
            return mid
        elif find_num > put_list[mid]:
            start = mid +1
        else:
            end = mid -1

    return -1

d = [1,4,9,16,25,36,49,64,81]
print(divide_find(d, 36))
print(divide_find(d, 9))
print(divide_find(d, 700))