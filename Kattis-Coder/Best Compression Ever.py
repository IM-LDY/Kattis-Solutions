input1 = input().split(' ')

exp = input1[0] + '*' + input1[1]

if eval(exp) < 1000:
    print('yes')

else:
    print('no')
