input1 = int(input())
input2 = [input() for i in range(input1)]

unique_list = list(set(input2))
unique_possibility = []
unique_index = []
for i in unique_list:
    unique_possibility.append(input2.count(i)/len(input2))
lowest = min(unique_possibility)

if unique_possibility.count(lowest) != 1:
    for i in range(len(unique_possibility)):
        if(unique_possibility[i] == lowest):
            unique_index.append(i)
    tmp_arr = []
    for i in unique_index:
        tmp_arr.append(unique_list[i])
        tmp_arr = sorted(tmp_arr)
    for i in tmp_arr:
        print(i)
else:
    tmp_index=unique_possibility.index(min(unique_possibility))
    print(unique_list[tmp_index])
