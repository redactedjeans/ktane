pws = ['about', 'after', 'again', 'below', 'could',
       'every', 'first', 'found', 'great', 'house',
       'large', 'learn', 'never', 'other', 'place',
       'plant', 'point', 'right', 'small', 'sound',
       'spell', 'still', 'study', 'their', 'there',
       'these', 'thing', 'think', 'three', 'water',
       'where', 'which', 'world', 'would', 'write']


# check given options against list of passwords and return all possible
#   solutions
def solve(opts):
    sols = pws.copy()   # get (deep) copy of password list

    # for each possible password...
    #   iterates over password list because copy gets modified by loop
    for sol in pws:
        # look at the columns one by one
        for i, col in enumerate(opts):
            # if this letter is not one of the options
            if sol[i] not in col:
                # check if removed already, and do it if not
                if sol in sols: sols.remove(sol)

    return sols # return solution list


# run solve() on more and more input until one solution is found
def solve_all():
    # set required variables
    opts = []
    solved = False

    # loop while no solution is found
    i = 0
    while not solved:
        # get 'column'
        n = input().strip()
        opts.append(list(n))
        i += 1

        # check for solution with current data
        s = solve(opts)
        if len(s) <= 1: solved = True

    # return solution
    if (s): return s[0]
    else: return None


if __name__ == '__main__':
    s = solve_all()
    if s:
        print("The solution is: " + s + ".")
    else:
        print("There is no solution.")
