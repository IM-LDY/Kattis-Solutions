import math
input1 = int(input())
K_plused = input1
"""Notes: first output integer must be larger than the input, cuz his friends will be trying some also.
so plus 2 everytime for the input number and try to calculate if the input is even and plus 1 if the input is odd.
only chop at the center, meanning if 6, then 6/2=3, 3 then cannot be splitted. if 8 then 8/2=4, 4 can be splitted to 2 which can
then be splitted to 1. 10 can be splitted to 5 and 5 cannot be further splitted."""
break_pluseds = 0

chops = 0


def K_checker(K_plused):
    if K_plused % 2 == 0:
        K_plused += 2
        if ((K_plused/2) % 2) != 0:
            K_plused += 2
    else:
        K_plused += 1
        if ((K_plused/2) % 2) != 0:
            K_plused += 2
    return K_plused


def only_one():
    if input1 == 1:
        print(*[2, 1])


def chop(n):
    chopped = n/2
    return chopped


K_plused = K_checker(K_plused)
K_plused2 = K_checker(K_plused)
only_one()


def calc(K_plused):
    # for main boy's chocolate
    tmp_original_checker = 0
    chops = 0
    for i in range(math.ceil(K_plused/2)):
        # if >= input1
        if tmp_original_checker >= input1:

            if tmp_original_checker == input1:
                break
            else:
                # if chopped pieces is more than what the main boy want, dun give him the whole piece, gv him chopped again piece and see.
                tmp_original_checker -= K_plused
                K_plused = chop(K_plused)
                chops += 1
                tmp_original_checker += K_plused

        else:
            K_plused = chop(K_plused)
            tmp_original_checker += K_plused
            chops += 1
    return chops, tmp_original_checker


chops, tmp_or = calc(K_plused)
if tmp_or != input1:
    K_plused += 2
    K_plused = K_checker(K_plused)
    chops, tmp_or = calc(K_plused)
if input1 != 1:
    print(*[K_plused, chops])
