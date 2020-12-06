input1 = int(input())
input2 = [input().split(' ') for i in range(input1)]

# 1 1 2 1 2 2

# 1 1
# 2 1
# 2 2
# 1 1
"""Notes: Approach to this problem is by transforming the numbers of coordinates into arrays of 2, then
use the determinent to calculate area. 0.5*[(1+4+2)-(2+2+2)]=0.5. Note the coordinates must be in anti-clockwise order
and there must be one extra coordinate same as the firt coordinates in the first line at the last line."""


def calc(arr):
    loop_times = arr[0]
    arr = arr[1:]
    sumA = 0
    sumB = 0
    tmp_last_two = arr[:2]
    arr.append(tmp_last_two[0])
    arr.append(tmp_last_two[1])
    for i in range((int(loop_times))*2):
        tmp_int = 0
        if i % 2 == 0:
            tmp_int = i+3
            sumA += (int(arr[i])*int(arr[tmp_int]))
        else:
            tmp_int = i+1
            sumB += (int(arr[i])*int(arr[tmp_int]))
    print(0.5*(abs(sumA-sumB)))


for i in range(input1):
    calc(input2[i])

