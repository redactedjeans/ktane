sols = {1: [2,      2,      3,      4],
        2: ['4',    'p1',   1,      'p1'],
        3: ['l2',   'l1',   3,      '4'],
        4: ['p1',   1,      'p2',   'p2'],
        5: ['l1',   'l2',   'l4',   'l3']}


# solve a specific stage of the module, returns (position, label)
def solve_stage(stage, curr, prev):
    d = curr[0]             # display number
    b = curr[1]             # buttons
    sol = sols[stage][d-1]  # solution

    # interpret solution and return label
    if type(sol) == int:    # solution is position
        return sol, b[sol-1]
    elif len(sol) == 1:     # solution is label
        return b.index(sol)+1, sol
    else:                   # solution depends on earlier stage
        t = sol[0]; st = int(sol[1])    # type, stage
        # find 'previous' solution
        p_sol = solve_stage(st, prev[st-1], prev[:st-1])
        # now find the current solution based on earlier position/label
        if t == 'p':    # solution is position
            return p_sol[0], b[p_sol[0]-1]
        else:   # t == 'l', solution is label
            return b.index(p_sol[1])+1, p_sol[1]


def solve_all():
    NUM_STAGES = 5
    prev = []
    for s in range(NUM_STAGES):
        i = input()
        d = int(i[0]); b = i[-4:]
        soln = solve_stage(s+1, [d, b], prev)
        prev.append([d, b])
        print(soln)


if __name__ == '__main__':
    #print(solve_stage(1, [1, "4321"], []))  # (2, '3')
    #print(solve_stage(2, [4, "3412"], [[1, "4321"]]))   # (2, '4')
    #print(solve_stage(3, [4, "3124"], [[1, "4321"], [4, "3412"]]))   # (4, '4')
    #print(solve_stage(4, [3, "2143"], [[1, "4321"], [4, "3412"], [4, "3124"]]))   # (2, '1')
    #print(solve_stage(5, [3, "1423"], [[1, "4321"], [4, "3412"], [4, "3124"], [3, "2143"]]))   # (1, '1')

    solve_all()
