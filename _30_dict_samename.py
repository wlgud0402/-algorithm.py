#딕셔너리를 이용한 동명이인 찾기

name_list = ["Tom", "Jerry", "Mike", "Tom"]
name_list2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

def find_same_name(put_list):
    finded_same = {}
    for name in put_list:
        if name in finded_same:
            finded_same[name] += 1
        else:
            finded_same[name] = 1    #딕셔너리 키=name, 값=1

    result = set()   #결과값 넣을 빈 집합
    
    for i in finded_same:
        if finded_same[i] >= 2:
            result.add(i)

    return result

print(find_same_name(name_list))
print(find_same_name(name_list2))