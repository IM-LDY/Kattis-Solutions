input1 = input().split(' ')
input2 = input()
input1 = sorted([int(i) for i in input1])
order = {"A": input1[0], "B": input1[1], "C": input1[2]}

print('{} {} {}'.format(order[input2[0]], order[input2[1]], order[input2[2]]))
