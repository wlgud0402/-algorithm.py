#친구 찾기 + 친밀도
def all_friend(friend_info, himself):
    qu =[]  #중복자가 따로따로 들어감
    done = set() #집합에는 중복된것들이 한개로만 들어감 mike가 백개 들어가도 mike 하나로 나옴

    qu.append((himself, 0))
    done.add(himself)

    while qu:
        (out_friend, friendly) = qu.pop(0)
        print(out_friend, friendly)
        for friend in friend_info[out_friend]:
            if friend not in done:
                qu.append((friend, friendly+1))
                done.add(friend)

friend_info = {
    'Summer' :['John','Justin','Mike'],
    'John' :['Summer','Justin'],
    'Justin' :['John','Summer','Mike','May'],
    'Mike' :['Summer','Justin'],
    'May' :['Justin','Kim'],
    'Kim' :['May'],
    'Tom' :['Jerry'],
    'Jerry' :['Tom']
}

all_friend(friend_info, 'Summer')

print()

all_friend(friend_info, 'Jerry')