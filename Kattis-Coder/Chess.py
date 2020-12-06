"""Train of thoughts: Init the gaming board, then define four functions each indicating the 4 directions that the queen can move
Before start moving, check whether the start and ending positions are of different color, if they are, directly output impossible."""


# The game_board

# Init queen's position
data_dic = {"A": 1, "B": 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, "G": 7, "H": 8}

# Take inputs and cahnge the position from english to number
input1 = [input().split(' ') for i in range(int(input()))]
for i in range(len(input1)):
    for ele in range(4):
        if input1[i][ele] in data_dic:
            input1[i][ele] = data_dic[input1[i][ele]]
        else:
            input1[i][ele] = int(input1[i][ele])


def left_up_purge(co_one, co_two):
    if co_one > 1 and co_two < 8:
        # move left
        co_one -= 1
        # move right
        co_two += 1
        return co_one, co_two
    else:
        return


def right_up_purge(co_one, co_two):
    if co_one < 8 and co_two < 8:
        # move left
        co_one += 1
        # move right
        co_two += 1
        return co_one, co_two
    else:
        return


def right_bottom_purge(co_one, co_two):
    if co_one < 8 and co_two > 1:
        # move left
        co_one += 1
        # move right
        co_two -= 1
        return co_one, co_two
    else:
        return


def left_bottom_purge(co_one, co_two):
    if co_one > 1 and co_two > 1:
        # move left
        co_one -= 1
        # move right
        co_two -= 1
        return co_one, co_two
    else:
        return


def calc(starting_point):

    co_one = starting_point[0]
    co_two = starting_point[1]
    source_point_arr = [[co_one, co_two]]

    for i in range(7):
        try:
            co_one, co_two = left_up_purge(co_one, co_two)
            source_point_arr.append([co_one, co_two])
        except:
            pass
    co_one = starting_point[0]
    co_two = starting_point[1]
    for i in range(7):
        try:
            co_one, co_two = right_up_purge(co_one, co_two)
            source_point_arr.append([co_one, co_two])
        except:
            pass
    co_one = starting_point[0]
    co_two = starting_point[1]
    for i in range(7):
        try:
            co_one, co_two = left_bottom_purge(co_one, co_two)
            source_point_arr.append([co_one, co_two])
        except:
            pass
    co_one = starting_point[0]
    co_two = starting_point[1]
    for i in range(7):
        try:
            co_one, co_two = right_bottom_purge(co_one, co_two)
            source_point_arr.append([co_one, co_two])
        except:
            pass
    return source_point_arr


for i in range(len(input1)):
    starting = input1[i][:2]
    ending = input1[i][2:]
    a = calc(starting)
    b = calc(ending)
    repeated = False
    for n in a:
        for x in b:
            if n == x:
                repeated = True
                repeated_point = n
                break
    if repeated:
        x = repeated_point[0]
        y = repeated_point[1]
        for i in data_dic.keys():
            if data_dic[i] == x:
                x = i
            if data_dic[i] == starting[0]:
                starting[0] = i
            if data_dic[i] == ending[0]:
                ending[0] = i
        # number of steps
        steps = 2

        # if move and destination is the same, minus one step
        if x == ending[0] and y == ending[1]:
            steps -= 1
            x = ''
            y = ''
          # array to store the result
        result_arr = [steps, starting[0],
                      starting[1], x, y, ending[0], ending[1]]
        # pop empty string
        result_arr = [i for i in result_arr if i != '']
        print(*result_arr)

    else:
        print('Impossible')
