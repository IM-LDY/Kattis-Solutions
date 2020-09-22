input1 = input().split(' ')
input1 = sorted([int(i) for i in input1])
minus1 = abs(input1[0]-input1[1])
minus2 = abs(input1[1]-input1[2])
if(minus1 == minus2):
    print(input1[-1]+minus1)
elif(minus1 > minus2):
    print(input1[0]+minus2)
else:
    print(input1[1]+minus1)
