#n명중 두명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘
#ex) 입력이 ["TOM", "JERRY", "MIKE"]라면 
#       TOM - JERRY
#       TOM - MIKE
#     JERRY - MIKE

def make_friend(names):
    n = len(names)
    friend_pairs = []
    for i in range(0,n-1):          #0부터 n-2까지 반복
        for j in range(i+1, n):     #i+1부터 n-1까지 반복
            pair = []
            pair.append(names[i])
            pair.append(names[j])
            friend_pairs.append(pair)
    return friend_pairs

names = ["TOM", "JERRY", "MIKE", "SIN"]
print(make_friend(names))

