input1 = [input() for i in range(7)]
counter = 0

# Tell the computer what is 1234567890 and +
zero = """xxxxx
x...x
x...x
x...x
x...x
x...x
xxxxx"""
one = """....x
....x
....x
....x
....x
....x
....x"""
two = """xxxxx
....x
....x
xxxxx
x....
x....
xxxxx"""
three = """xxxxx
....x
....x
xxxxx
....x
....x
xxxxx"""
four = """x...x
x...x
x...x
xxxxx
....x
....x
....x"""
five = """xxxxx
x....
x....
xxxxx
....x
....x
xxxxx"""
six = """xxxxx
x....
x....
xxxxx
x...x
x...x
xxxxx"""
seven = """xxxxx
....x
....x
....x
....x
....x
....x"""
eight = """xxxxx
x...x
x...x
xxxxx
x...x
x...x
xxxxx"""
night = """xxxxx
x...x
x...x
xxxxx
....x
....x
xxxxx"""
plus_sign = """.....
..x..
..x..
xxxxx
..x..
..x..
....."""
# Length of the expression
n_len = (len(input1[0])+1)/6
# Save the input numbers and compare. Then minipulate
input_arr = []
for n in range(int(n_len)):
    tmp_string = ''
    for i in input1:
        number = i[n*5+n:5*(n+1)+n]
        tmp_string += number+'\n'
    input_arr.append(tmp_string)
input_arr = [i[:-1] for i in input_arr]
string_numbers = [zero, one, two, three, four,
                  five, six, seven, eight, night, plus_sign]
real_nms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result_arr = []


def comparison(i):
    for n in range(len(string_numbers)):
        if(string_numbers[n] == i):
            result_arr.append(string_numbers.index(string_numbers[n]))
            return


for x in input_arr:
    comparison(x)

for i in range(len(result_arr)):
    if(result_arr[i] == 10):
        result_arr[i] = '+'


result_string = ''
for i in result_arr:
    result_string += str(i)
calculated_result = (eval(result_string))

result_arr = [i for i in str(calculated_result)]

final_arr = []
for i in result_arr:
    final_arr.append(string_numbers[int(i)])

final_arr_splited = [i.split('\n') for i in final_arr]

tmp_string_one = ''
tmp_string_two = ''
tmp_string_thre = ''
tmp_string_four = ''
tmp_string_five = ''
tmp_string_six = ''
tmp_string_seven = ''
for i in final_arr_splited:
    tmp_string_one += i[0]+'.'
    tmp_string_two += i[1]+'.'
    tmp_string_thre += i[2]+'.'
    tmp_string_four += i[3]+'.'
    tmp_string_five += i[4]+'.'
    tmp_string_six += i[5]+'.'
    tmp_string_seven += i[6]+'.'
print(tmp_string_one[:-1])
print(tmp_string_two[:-1])
print(tmp_string_thre[:-1])
print(tmp_string_four[:-1])
print(tmp_string_five[:-1])
print(tmp_string_six[:-1])
print(tmp_string_seven[:-1])
