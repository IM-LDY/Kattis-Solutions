input1 = input().split(' ')
input2 = input().split(' ')
input3 = input().split(' ')

list1 = []

for a, b, c in zip(input1, input2, input3):
    list1.append([a, b, c])

unique = []
for i in list1:
    if i[0] == i[1]:
        unique.append(i[2])
    elif i[0] == i[2]:
        unique.append(i[1])
    else:
        unique.append(i[0])

output = ''
for i in unique:
    output += i+' '
print(output)
