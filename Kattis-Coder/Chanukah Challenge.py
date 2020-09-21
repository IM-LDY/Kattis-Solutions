input1 = int(input())

input2 = [input().split() for i in range(input1)]

for i in input2:
    tmp_sum = 0
    for n in range(1, int(i[1])+1):
        tmp_sum += n
    print(str(i[0])+' '+str(tmp_sum+int(i[1])))
