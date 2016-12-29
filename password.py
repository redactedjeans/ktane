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
    opts = []
    solved = False
    
    i = 0
    while not solved:
        # get 'column'
        n = input()
        opts.append(list(n))
        i += 1
        
        # check for solution with current data
        s = solve(opts)
        if len(s) <= 1: solved = True

    # print solution
    if (s):
        print('SOLUTION:', s[0])
    else:
        print('NO SOLUTION')


if __name__ == '__main__':
    solve_all()
