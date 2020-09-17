

input1 = input()
input2 = input().split(' ')


def cal(input1, input2):
    largest = input2[0]

    counter = 1
    nbs = f'{input2[0]}'
    for i in range(int(input1)):
        if(input2[i] > largest):
            largest = input2[i]
            counter += 1
            nbs += (' '+input2[i])
    print(counter)
    print(nbs)


cal(input1, input2)
