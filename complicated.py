# define all the rules as a 4-dimensional tuple
# red,  blue,   star,   led,    solution
# 0     0       0       0       C
# 0     0       0       1       D
# 0     0       1       0       C
# 0     0       1       1       B
# 0     1       0       0       S
# 0     1       0       1       P
# 0     1       1       0       D
# 0     1       1       1       P
# 1     0       0       0       S
# 1     0       0       1       B
# 1     0       1       0       C
# 1     0       1       1       B
# 1     1       0       0       S
# 1     1       0       1       S
# 1     1       1       0       P
# 1     1       1       1       D
rules = (
         (
          (
           ('c', 'd'),
           ('c', 'b')
          ),
          (
           ('s', 'p'),
           ('d', 'p')
          )
         ),
         (
          (
           ('s', 'b'),
           ('c', 'b')
          ),
          (
           ('s', 's'),
           ('p', 'd')
          )
         )
        )

# solve a single wire
def solve(wire):
    rule = rules[wire[0]][wire[1]][wire[2]][wire[3]]
    if rule == 'c':
        return 'CUT'
    elif rule == 'd':
        return "DON'T CUT"
    elif rule == 's':
        return 'IF EVEN'
    elif rule == 'p':
        return 'HAS PARALLEL'
    elif rule == 'b':
        return '2+ BATTERIES'
    #TODO: interpret solution and return solution

# solve all wires
def solve_all(debug=0):
    # set variables
    NUM_WIRES = 6
    soln = []

    #print prompt
    print('LED? COLOUR(S) STAR?')
    # solve each wire and return solution
    for i in range(NUM_WIRES):
        wire = []
        # get wire 'description'
        d = input().strip().lower().split()
        # parse 'description' into 0s and 1s
        wire.append(1 if 'r' in d[1] else 0)        # red wire?
        wire.append(1 if 'b' in d[1] else 0)        # blue wire?
        wire.append(1 if d[2][0] == 'y' else 0)     # star present?
        wire.append(1 if d[0][0] == 'y' else 0)     # LED on?
        # get solution, print if necessary, and save
        s = solve(wire)
        if debug: print(s)
        soln.append(s)

    # return solution
    return soln


if __name__ == '__main__':
    s = solve_all(1)
    print(s)
