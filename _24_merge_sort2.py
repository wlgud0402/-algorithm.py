def merge_sort(put_list):
    n = len(put_list)
    if n <= 1:
        return
    
    mid = n//2
    g1 = put_list[:mid]
    g2 = put_list[mid:]

    merge_sort(g1)
    merge_sort(g2)

    new_g1 = 0
    new_g2 = 0
    result = 0

    while new_g1 < len(g1) and new_g2 < len(g2):
        if g1[new_g1] < g2[new_g2]:
            put_list[result] = g1[new_g1]
            new_g1 += 1
            result += 1
        else:
            put_list[result] = g2[new_g2]
            new_g2 += 1
            result += 1
    
    while new_g1 < len(g1):
        put_list[result] = g1[new_g1]
        new_g1 += 1
        result += 1
    while new_g2 < len(g2):
        put_list[result] = g2[new_g2]
        new_g2 += 1
        result += 1

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(merge_sort(d))
