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
    #row = curr_cell // 6
    #col = curr_cell % 6

    start_cell = 21
    end_cell = 0
    curr_cell = start_cell

    queue = [curr_cell]

    print(maze[curr_cell])
    print(curr_cell)
    print(queue)

    for i in range(0, 20):
        curr_cell  = get_valid_cell(curr_cell, maze[curr_cell], queue)
        queue.append(curr_cell)
        print(curr_cell)
        print(queue)
        if curr_cell == end_cell:
            print('Done!')
            return

def get_valid_cell(cell_idx, cell, queue):
    for i, val in enumerate(cell):
        if i == 0:
            neighbour = cell_idx - 6
        if i == 1:
            neighbour = cell_idx + 1
        if i == 2:
            neighbour =  cell_idx + 6
        if i == 3:
            neighbour = cell_idx - 1

        if val == 0 and neighbour not in queue:
            return neighbour

def solve_all():
    solve()


if __name__ == '__main__':
    s = solve_all()
