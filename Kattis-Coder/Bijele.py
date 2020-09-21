input1 = input().split(' ')
input1 = [int(i) for i in input1]

tmp_arr = []

target_arr = [1, 1, 2, 2, 2, 8]

for a, b in zip(input1, target_arr):
    tmp_arr.append(b-a)

print(*tmp_arr)
