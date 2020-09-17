info = input()
def days(num_of_statues):
    printer = 1
    days = 0
    while printer < int(num_of_statues):
        printer = printer*2
        days+= 1
        
    days+=1
    return days
print(days(info))