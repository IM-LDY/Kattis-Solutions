input1 = input()
input2 = input().split(' ')
# input2 = [2, 2, 1, 3, 3, 2]
# Cases: 2 1 3 4 decreasing increasing
# Cases: 1 2 3 4 increasing
# Cases: 1 2 4 3 5 6 increasing decreasing increasing
# Cases: 1 2 3 4 5 3 increasing decreasing
# Cases: 4 3 2 1 decreasing
input2 = [int(i) for i in input2]
trend = []  # Array to store the trend of the numebrs
change_pos = []  # Arrary to store where the trend chagnes
if(len(input2) == 1):
    input2.append(input2[0])

input2_copy = input2.copy()


def first_trend_determiner():
    if(len(input2_copy) == 1):
        return
    if(input2_copy[0] > input2_copy[1]):
        trend.append('decreasing')
        return
    elif(input2_copy[0] < input2_copy[1]):
        trend.append('increasing')
        return
    else:
        input2_copy.pop(0)
        first_trend_determiner()


no_trend = False
first_trend_determiner()
try:
    current_trend = trend[0]
except:
    no_trend = True
    print(*[1, 1])
init_var = input2[0]
# Get the trends of the inputs to see whethere it is possible to revert
for i in range(1, int(input1)):
    if((input2[i] > init_var) and (current_trend == 'decreasing')):
        trend.append('increasing')
        current_trend = 'increasing'
        change_pos.append(i)
    elif((input2[i] < init_var) and (current_trend == 'increasing')):
        trend.append('decreasing')
        current_trend = 'decreasing'
        change_pos.append(i)
    init_var = input2[i]


def trend_possibility():
    # 1 2 3 4 5, 1 1 2 3 4, 1 2 3 3 4, 1 4 5 6 10, 1 1 1 1 8
    if(len(trend) == 1 and trend[0] == 'increasing'):  # 1 2 3 4 # Settled
        print(*[1, 1])
        return
    # 9 8 7 8 9, 10 8 6 6 7, 10 10 10 9 10, 9 9 9 8 11
    # settled
    if(len(trend) == 2 and trend[0] == 'decreasing' and trend[1] == 'increasing'):
        tmp_lists = input2[0:change_pos[0]][::-1]
        for i in input2[change_pos[0]:]:
            tmp_lists.append(i)
        ans = all(i <= j for i, j in zip(tmp_lists, tmp_lists[1:]))
        if ans:
            print(*[1, change_pos[0]])
        else:
            print('impossible')
        return
    # 6
    # 1 2 3 2 2 1, 1 8 10 2 2 0, 1 2 3 4 3 2, 1 1 2 1 2 2, 1 10 9 8 7 6 7, 10 13 19 19 15 14 20
    if(len(trend) == 3 and trend[0] == 'increasing' and trend[1] == 'decreasing' and trend[2] == 'increasing'):
        arr_to_revert = [input2[change_pos[1]-1]]
        index_arr_to_revert = [change_pos[1]-1, ]
        # arr_to_revert = []
        pause = False
        for i in range(1, change_pos[1]):
            if(input2[change_pos[1]-i] <= input2[change_pos[1]-i-1]):
                if pause == False:
                    index_arr_to_revert.append(change_pos[1]-i-1)
                    arr_to_revert.append(input2[change_pos[1]-i-1])
            else:
                pause = True
        index1 = index_arr_to_revert[0]
        index2 = index_arr_to_revert[-1]

        a = input2[:index2]
        b = input2[index1+1:]
        all_lists = []
        for i in a:
            all_lists.append(i)
        for i in arr_to_revert:
            all_lists.append(i)
        for i in b:
            all_lists.append(i)
        ans = all(i <= j for i, j in zip(all_lists, all_lists[1:]))
        if ans:
            print(*[index2+1, change_pos[1]
                    ])
        else:
            print('impossible')
        return
    # 7
    # 1 2 3 4 4 3 2, 1 2 2 3 2, 1 1 2 3 4 7 6, 1 2 3 4 3, 1 5 2, 1,1 2, 2,1, -2 2 1
    # Settled
    if(len(trend) == 2 and trend[0] == 'increasing' and trend[1] == 'decreasing'):

        original_li = input2[:change_pos[0]-1]  # [3, 3, 5, 5, 5, 5, 5, 5]
        tmp_lists = input2[change_pos[0]-1:][::-1]  # [3, 5]
        pause = False
        for i in original_li[::-1]:
            if(original_li[-1] == tmp_lists[-1] and pause == False):
                tmp_lists.append(tmp_lists[-1])
                original_li.pop(-1)
            else:
                pause = True
        len_start = len(original_li)
        for i in tmp_lists:
            original_li.append(i)
        len_ends = (len(tmp_lists)+len_start)
        ans = all(i <= j for i, j in zip(original_li, original_li[1:]))
        if ans:
            print(*[len_start+1, len_ends
                    ])
        else:
            print('impossible')
        return
    if(len(trend) == 1 and trend[0] == 'decreasing'):  # Settled
        print(*[1, input1], sep=' ')
        return
    if not no_trend:
        print('impossible')


def output_ans():
    if(len(trend) == 1 and trend[0] == 'increasing'):
        output = f'{input2[0]} {input2[0]}'


trend_possibility()
