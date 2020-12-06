game_board = [list(map(int, input().split(' '))) for i in range(4)]
move = input()


def move_zero_left(arr):
    for row in range(len(arr)):
        for elelment in range(1, 4):
            # only checks for the first 3 elements, otherwise the index will go out of range
            current_ele = arr[row][elelment]
            previous_ele = arr[row][elelment-1]
            # If current element is zero, jump to the next loop
            if current_ele == 0:
                continue
            if current_ele == previous_ele:
                arr[row][elelment-1] = arr[row][elelment]*2
                arr[row][elelment] = 0
            # for the second elelment
            if previous_ele == 0 and elelment == 1:
                arr[row][0] = arr[row][1]
                arr[row][1] = 0
                continue
            # for the thrid element
            if previous_ele+arr[row][0] == and elelment == 2:
                arr[row][0] = current_ele
                arr[row][elelment] = 0
            if

    print(arr)


move_zero_left(game_board)
