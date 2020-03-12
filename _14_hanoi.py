def hanoi(n, from_pos, to_pos, support_pos):
    if n == 1:
        print(from_pos, "->" ,to_pos)
        return

    hanoi(n-1, from_pos, support_pos, to_pos)
    print(from_pos, "->", to_pos)
    hanoi(n-1, support_pos, to_pos, from_pos)

hanoi(3,1,3,2)