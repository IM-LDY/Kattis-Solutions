input1 = input().split(' ')
while input1 != ['0', '0']:
    input1 = [int(i) for i in input1]
    input2 = int(input())
    input3 = [input().split() for i in range(input2)]

    x = 0
    y = 0
    for i in input3:
        if(i[0] == 'u'):
            y += int(i[1])
        elif(i[0] == 'd'):
            y -= int(i[1])
        elif(i[0] == 'l'):
            x -= int(i[1])
        else:
            x += int(i[1])
    print(*['Robot thinks', x, y])

    width = int(input1[0])-1
    length = int(input1[1])-1

    x = 0
    y = 0
    for i in input3:
        if(i[0] == 'u'):
            y += int(i[1])
        elif(i[0] == 'd'):
            y -= int(i[1])
        elif(i[0] == 'l'):
            x -= int(i[1])
        else:
            x += int(i[1])
        if(x > width):
            x = width
        elif (x < 0):
            x = 0
        if(y > length):
            y = length
        elif(y < 0):
            y = 0
    print(*['Actually at', x, y])
    input1 = input().split(' ')
