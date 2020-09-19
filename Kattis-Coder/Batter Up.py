input1 = input()
input2 = input().split(' ')
try:
    while (input2.count('-1')):
        input2.remove('-1')
except:
    pass
input2 = [int(i) for i in input2]
print(sum(input2)/len(input2))
