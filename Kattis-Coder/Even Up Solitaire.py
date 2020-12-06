input1 = input()
input2 = input().split(' ')
input2 = list(map(int, input2))


def calc(arr):
    counter = 0
    pop_arr = []
    while counter < len(input2)-1:
        if((arr[counter]+arr[counter+1]) % 2 == 0):
            pop_arr.append(counter)
            pop_arr.append(counter+1)
            counter += 2
            try:
                if(((arr[counter]+arr[counter-3]) % 2 == 0) and not (counter-3 in pop_arr) and counter-3 >= 0):
                    counter += 1
                    pop_arr.append(counter)
            except:
                pass
        else:
            counter += 1

    print(len(arr)-len(pop_arr))


calc(input2)
