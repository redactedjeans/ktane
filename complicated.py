# define all the rules as a 4-dimensional tuple
# red,  blue,   star,   led
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

def solve():
    pass

def solve_all():
    solve()


if __name__ == '__main__':
    print(rules[0][1][1][0].upper())    #D

    # s = solve_all()
    # print(s)
