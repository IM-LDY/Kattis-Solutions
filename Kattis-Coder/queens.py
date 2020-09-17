# import numpy as np
input_number = int(input())

arr = []

# stores the inputs
arr = [input() for i in range(input_number)]
# split the input by white space
new_arr = [i.split(' ') for i in arr]
# Init the game frame n x n
init_arr = [[0 for i in range(input_number)] for j in range(input_number)]
# print(init_arr)
# Make the position corresponding to the input 1
for i in new_arr:
    init_arr[int(i[0])][int(i[1])] = 1
# Condition init to true
results = True
for i in range(input_number):
    if(sum(init_arr[row][i] for row in range(input_number)) > 1):
        results = False  # Checking columns no duplicate
    if(sum(init_arr[i][col] for col in range(input_number)) > 1):
        results = False  # Checking rows
# Checking middle diagonal
mid_dia = [init_arr[i][i] for i in range(input_number)]
mid_dia_sum = sum(mid_dia)

if(mid_dia_sum > 1):
    results = False
# Checking for upper diagnal
# E.G
# Upper diagonal
# [01 12 23 34]
# [02 13 24]
# [03 14]
# Lower Diagonal, they are in mirror, so just swap the position in the for loop
# [10 21 32 43]
# [20 31 42]
# [30 41]


for i in range(2, input_number):
    tmp_list = [(x, input_number-i+x)
                for x in range(i)]  # Checking for upper diagonal
    tmp_list2 = [(input_number-i+x, x)
                 for x in range(i)]  # Checking for lower diagonal
    # See if their sum is larger than one
    if(sum([init_arr[z[0]][z[1]] for z in tmp_list]) > 1):
        results = False
    if(sum([init_arr[z[0]][z[1]] for z in tmp_list2]) > 1):
        results = False
# Check for mid-digonal from right
# [04 13 22 31 40]
# print(init_arr)
# print(input_number)
if sum(
    [init_arr[x][input_number-x-1] for x in range(input_number)]
) > 1:
    results = False
# Check
# Check
#  upper bottom diagnal
#  [14 23 32 41]
# [24 33 42]
# [34 43]
# upper left diagnal
# [01 10]
# [02 11 20]
# [03 12 21 30]
for i in range(input_number-2):
    tmp_list = [x+i
                for x in range(1, input_number-i)]  # Checking for  bottom right diagonal
    inv_tmp_list = tmp_list[::-1]
    if(sum([init_arr[ele1][ele2] for ele1, ele2 in zip(tmp_list, inv_tmp_list)])) > 1:
        results = False
for i in range(2, input_number):
    tmp_list = [x
                for x in range(i)]  # Checking for upper left diagonal
    inv_list = tmp_list[::-1]
    if(sum([init_arr[ele1][ele2]
            for ele1, ele2 in zip(tmp_list, inv_list)]) > 1):
        results = False

if(results == True):
    print('CORRECT')
elif(results == False):
    print("INCORRECT")
