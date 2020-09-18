import math
input1 = input().split(' ')
input1 = [float(i) for i in input1]

r = math.sqrt(input1[0]/3.1415926)

length_needed = 2*3.1415926*r

if(length_needed > input1[1]):
    print('Need more materials!')
else:
    print('Diablo is happy!')
