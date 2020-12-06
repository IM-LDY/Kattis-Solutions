input1 = int(input())

input2 = [input() for i in range(input1*2)]
test_numbers = []
test_cases = []
for i in range(len(input2)):
    try:
        test_numbers.append(int(input2[i]))
        test_cases.append(input2[i+1])
    except:
        pass


def calc(case_number, n, ropes):

    ropes = ropes.replace(' ', '')
    red_ropes = []
    blue_ropes = []
    tmp_numers = ''

    for i in ropes:
        try:
            int(i)
            tmp_numers += i
        except:
            pass
        if(i == 'R'):
            red_ropes.append(int(tmp_numers))
            tmp_numers = ''
        if(i == 'B'):
            blue_ropes.append(int(tmp_numers))
            tmp_numers = ''
    # only one color of rope
    if len(blue_ropes)*len(red_ropes) == 0:
        print('Case #{}: 0'.format(case_number+1))
        return
    # B or R is lesser?
    least = min(len(red_ropes),len(blue_ropes))
    sum = 0
    red_ropes = sorted(red_ropes)[::-1]
    blue_ropes = sorted(blue_ropes)[::-1]
    for i in range(least):
        sum += red_ropes[i]
        sum += blue_ropes[i]
        sum -= 2
    print('Case #{}: {}'.format(case_number+1, sum))


for i in range(input1):
    calc(i, test_numbers[i], test_cases[i])
