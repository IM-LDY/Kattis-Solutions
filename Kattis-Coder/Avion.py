input1 = [input() for i in range(5)]

tmp_list = []
counter = 1
for i in input1:
    if ('FBI' in i):
        tmp_list.append(counter)
    counter += 1
if len(tmp_list) == 0:
    print('HE GOT AWAY!')
else:
    print(*tmp_list)
