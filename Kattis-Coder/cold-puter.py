input1 = input()
input2 = input().split(' ')


def cal(input1, input2):
    counter = 0

    for i in range(int(input1)):
        if int(input2[i]) < 0:
            counter += 1
    return counter


print(cal(input1, input2))
