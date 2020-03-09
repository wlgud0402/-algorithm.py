def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0,n-1):          #0부터 n-2까지 반복
        for j in range(i+1, n):     #i+1부터 n-1까지 반복
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["TOM", "JERRY", "MIKE", "TOM"]
name2 = ["TOM", "JERRY", "MIKE", "TOM","MIKE"]
print(find_same_name(name))
print(find_same_name(name2))