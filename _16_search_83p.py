#찾는값이 나오는 모든 위치를 리스트로 돌려주는 것   찾는값 18,33,900
#찾는값이 없다면 빈리스트[] 를 출력함  

v = [17, 92, 18, 33, 58, 7, 33, 42]

def search_list(put_list, find_number):
    n = len(put_list)
    empty_list = []
    for i in range(0, n):
        if  find_number == put_list[i]:
            empty_list.append(i)    #maked_list.append()의 형태
    return empty_list               #만들어진 결과 리스트를 돌려줌
        
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))