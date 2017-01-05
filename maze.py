maze = [
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 0],

        [0, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],

        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 0],

        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 0],

        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 0],
        [0, 1, 0, 1],

        [0, 0, 1, 1],
        [1, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [0, 1, 1, 0]
    ]


def solve():
    print(maze)

    curr_cell = 28
    row = curr_cell // 6
    col = curr_cell % 6

    print(maze[curr_cell])

    print(curr_cell)
    print(row, col)

    open_wall = get_valid_cell(maze[curr_cell])

    print(open_wall)

    if open_wall == 0:
        curr_cell -= 6

    if open_wall == 1:
        curr_cell += 1

    if open_wall == 2:
        curr_cell += 6

    if open_wall == 3:
        curr_cell -= 1

    print(row, col)

    print(curr_cell)

def get_valid_cell(cell):
    for i, val in enumerate(cell):
        if val == 0:
            return i

def solve_all():
    solve()


if __name__ == '__main__':
    s = solve_all()
