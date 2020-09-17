import math
input1 = input()
input2 = [input().split(' ') for i in range(int(input1))]
concurrent_timing = []
# Get conflict timing


def get_concurrent_timing():
    for i in input2:
        start_timing = int(i[1])-2*int(i[0])
        end_timing = int(i[1])
        flip_timing = (end_timing-start_timing)/2+start_timing
        concurrent_timing.append(start_timing)
        concurrent_timing.append(end_timing)
        concurrent_timing.append(flip_timing)


def unique_timing():
    unique_list = []
    for i in concurrent_timing:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


get_concurrent_timing()
unique_list = unique_timing()

# Get the conflict timing that needs the most order served and divded by 2



def count_occurance():
    tmp_list = []
    for i in unique_list:
        tmp_list.append(concurrent_timing.count(i))

    print(int(math.ceil(max(tmp_list)/2)))


count_occurance()
