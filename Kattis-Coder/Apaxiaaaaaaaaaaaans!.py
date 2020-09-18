input1 = input()

string = [input1[0]]

current = input1[0]

for i in input1:
    if i == current:
        pass
    else:
        string.append(i)
        current = i
print(''.join(string))
