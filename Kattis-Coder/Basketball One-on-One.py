input1 = input()

a_score = 0
b_score = 0
for i in range(0, len(input1), 2):
    if(input1[i] == 'A'):
        a_score += int(input1[i+1])
    else:
        b_score += int(input1[i+1])

if(a_score > b_score):
    print('A')
else:
    print('B')
