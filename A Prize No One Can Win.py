input1 = input().split(' ')
input2 = input().split(' ')
input1 = [int(i) for i in input1]
input2 = [int(i) for i in input2]
input2 = sorted(input2)[::-1]
tmp_arr = []

for i in range(len(input2)-1):
    if(input2[i]+input2[i+1]) > input1[1]:
        tmp_arr.append(i)

print(len(input2)-len(tmp_arr))
