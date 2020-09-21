input1 = int(input())
input2 = [input().split(' ') for i in range(input1)]

other_rounds = [i[2] for i in input2]
first_round = [i[1] for i in input2]


print(sorted(first_round))
