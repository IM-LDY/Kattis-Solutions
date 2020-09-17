import numpy as np
input1 = input()


def calc(input1):
    for i in range(len(input1)):
        print(i)
        if (len(input1)-i) >= 3:
            tmpList = [input1[i], input1[i+1], input1[i+2]]
            if(len(np.unique(tmpList)) == 3):
                i += 2
                print('C')
        if(input1[i] == 'R'):
            print('S')
        elif (input1[i] == 'B'):
            print('k')
        else:
            print('H')


calc(input1)
