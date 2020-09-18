

input1 = int(input())
input2 = input().split(' ')

input2 = [int(i) for i in input2]

init_number = input2[0]
init_arr = [input2[0]]

for i in input2:
    if i > init_number:
        init_arr.append(i)
        init_number = i
print(len(init_arr))
print(*init_arr)
