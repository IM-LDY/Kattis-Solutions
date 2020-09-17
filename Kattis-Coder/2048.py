input1 = input()
input2 = input()
input3 = input()
input4 = input()
input5 = input()

arr = [[int(x) for x in input1.split(' ')], [int(x) for x in input2.split(
    ' ')], [int(x) for x in input3.split(' ')], [int(x) for x in input4.split(' ')]]
for i in arr:
    for x in range(len(i)):
        if x == 0:
            pass
        elif i[x] != i[x-1]:
            pass
        elif i[x] == i[x-1]:
            i[x-1] = 2*(i[x])
            i[x] = 0
        elif i[x-1] == 0:
            i[x-1] = i[x]
            i[x] = 0
print(arr)