input1 = int(input())
input2 = [int(input()) for i in range(input1)]

all_ans = {}


def generate_all_solutions():
    op_signs = ['//', '*', '-', '+']
    for a in op_signs:
        for b in op_signs:
            for c in op_signs:
                tmp_expression = '4 '+a+' 4 '+b+' 4 '+c+' 4'
                val = eval(tmp_expression)
                all_ans[val] = tmp_expression.replace('//', '/')


generate_all_solutions()


def outcome_decider(number):
    for key, value in all_ans.items():
        if number == key:
            return value+' = ' + str(number)
    return 'no solution'


for i in input2:
    if i < -60 or i > 256:
        print("no solution")
    else:
        print(outcome_decider(i))
