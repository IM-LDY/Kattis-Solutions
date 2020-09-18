input1 = input()

length_string = len(input1)
white_space = 0
lower_case = 0
upper_case = 0
symbols = 0

for i in input1:
    if(i == '_'):
        white_space += 1
    elif(i.isupper()):
        upper_case += 1
    elif(i.islower()):
        lower_case += 1
    else:
        symbols += 1
print(white_space/length_string)
print(lower_case/length_string)
print(upper_case/length_string)
print(symbols/length_string)
