#삽입정렬
d = [2,4,5,1,3]

def find_insert_idx(new_list, value):
    for i in range(0,len(new_list)):
        if value < new_list[i]:
            return i 
    
    return len(new_list)

def insert_sort(put_list):
    new_list = []
    while put_list:
        value = put_list.pop(0)
        insert_idx = find_insert_idx(new_list, value)
        new_list.insert(insert_idx, value)
    return new_list

print(insert_sort(d))