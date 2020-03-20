#친구찾기

def all_friend(friend_info, himself):
    qu =[]
    done = set()

    qu.append(himself)
    done.add(himself)

    while qu:
        out_friend = qu.pop(0)
        print(out_friend)
        for friend in friend_info[out_friend]:
            if friend not in done:
                qu.append(friend)
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