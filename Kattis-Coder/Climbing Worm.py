input1 = input().split(' ')

input1 = [int(i) for i in input1]


def calc(a, b, h):
    init_distance = 0
    counter = 0

    while init_distance < h:
        init_distance += a
        counter += 1
        if(init_distance >= h):
            print(counter)
            break
        else:
            init_distance -= b


calc(input1[0], input1[1], input1[2])
