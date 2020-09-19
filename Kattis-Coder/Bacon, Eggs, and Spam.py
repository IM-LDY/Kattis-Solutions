n = int(input())
while n:

    input2 = [input() for i in range(n)]

    def calc():
        foods = [i.split(' ')[1:] for i in input2]
        foods_new = []
        for i in foods:
            for x in i: 
                foods_new.append(x)
        foods_new = sorted(list(set(foods_new)))

        for i in foods_new:
            tmp_list = [i]
            for x in input2:
                if i in x:
                    tmp_list.append(x.split(' ')[0])
            print(*tmp_list)
        print(' ')
    calc()
    n = int(input())
