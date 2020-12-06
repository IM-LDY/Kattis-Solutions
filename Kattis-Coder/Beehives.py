import math

input1 = input().split(' ')
while input1 != ['0.0', '0']:
    input2 = [input().split(' ') for i in range(int(input1[1]))]
    sour_list = []
    for i in range(len(input2)):
        for n in range(i+1, len(input2)):
            a = abs(float(input2[i][0])-float(input2[n][0]))
            b = abs(float(input2[i][1])-float(input2[n][1]))
            length = math.sqrt(a**2+b**2)
            if (length <= float(input1[0])):
                sour_list.append(i)
                sour_list.append(n)

    sour = len(set(sour_list))
    sweet = int(input1[1])-sour

    print('{} sour, {} sweet'.format(sour, sweet))
    input1 = input().split(' ')
