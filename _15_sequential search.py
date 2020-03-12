#순차탐색
#18, 33, 900 찾아서 해당 위치번호를 돌려주기
v = [17, 92, 18, 33, 58, 7, 33, 42]

def search(put_list, x):
    n = len(put_list)
    for i in range(0, n):
        if x == put_list[i]:  #원한는숫자x가 리스트v의 i번째 요소와 값이 같으면 위치 i를 출력
            return i

    return -1   #여기서 리턴은 if문이 아니라 반복문 안에 들어가야한다
                #if 문안에 들어가버리면 첫번째 항목에서 if문돌리고 아닐시 바로 -1출력하고 끝

print(search(v, 18))
print(search(v, 33))
print(search(v, 900))
