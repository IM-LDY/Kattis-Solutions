input1 = input()
input2 = input().split(' ')

result = True
for i in range(1, len(input2)+1):
    if(i == input2[i-1] or i == 'mumble'):
        print(i)
        pass
    else:
        result = False

if result == True:
    print('makes sense')
else:
    print('something is fishy')
