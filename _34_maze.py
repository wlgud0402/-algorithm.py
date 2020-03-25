#미로

maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}


def solve_maze(maze, start, end):
    will_go =[]
    done = set()

    will_go.append(start)
    done.add(start)

    while will_go:
        load = will_go.pop(0)   #여기서 load는 단순한 문자열에 불과하다 a, ae , aei 등 -1로 마지막글자를 뽑는것!
        last = load[-1]
        if last == end:
            return load
        for point in maze[last]:
            if point not in done:
                will_go.append(load+point)
                done.add(point)
    
    return "?"

print(solve_maze(maze, 'a', 'p'))


