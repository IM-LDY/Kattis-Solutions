tmp_dic = {}

tmp_input = input().split(' ')
total_time = 0
correct_ans = 0
while tmp_input[0] != '-1':
    if tmp_input[-1] == 'right':
        # Plus the time
        total_time += int(tmp_input[0])
        correct_ans += 1
        try:
            # See whether the question is in the tmp_dic for wrong attempt
            tmp_time = tmp_dic[tmp_input[1]]
            # if it is , the total time have to plus the 20
            total_time += tmp_time
        except:
            # If the question is not in tmp dic, error will occur
            pass
    elif tmp_input[-1] == 'wrong':
        # See whether the question is alr in the dic
        try:
            stored_time = tmp_dic[tmp_input[1]]
            stored_time += 20
            tmp_dic[tmp_input[1]] = stored_time
        except:
            # Not in the dic
            tmp_dic[tmp_input[1]] = 20

    tmp_input = input().split(' ')


print('{} {}'.format(correct_ans, total_time))
