from collections import Counter
input1 = input().split(' ')
input2 = input().split(' ')

input1 = [int(i) for i in input1]
A = [int(i) for i in input2]

N = input1[0]
t = input1[1]


# This function calculates is there any 2 sum equals to 7777


def t_1():
    s = set(A)
    for i in range(1, 7777):
        if i in s and 7777-i in s:
            print("Yes")
            return
    print('No')
    return

# This function checks duplicate


def t_2():
    if len(set(A)) == len(A):
        print('Unique')
    else:
        print('Contains duplicate')
    return


def t_3():
    # uniques = list(set(A))
    # for i in uniques:
    #     if A.count(i) > (N/2):
    #         print(i)
    #         return
    # print(-1)
    # return
    a, b = Counter(A).most_common(1)[0]
    print(a if b > (N/2) else -1)


def t_4(arr):
    if len(arr) % 2 == 1:
        print(arr[int(((len(arr)-1)/2)+1)-1])
    else:
        print('{} {}'.format(arr[int(len(arr)/2)-1],
                             arr[int((len(arr)/2)+1)-1]))


def t_5():
    tmp_list = [i for i in A if i <= 999 and i >= 100]
    print(*sorted(tmp_list))


if t == 1:
    t_1()
elif t == 2:
    t_2()
elif t == 3:
    t_3()
elif t == 4:
    t_4(sorted(A))
else:
    t_5()
