import sys


occupied = 0
output_string = ''
for line in sys.stdin:

    len_row = len(line)-1
    occupied += line.count('*')
    if line != '\n':
        output_string = ('.'*(len_row-occupied)+'*' *
                          line.count('*')+'.'*(occupied-line.count('*')))
        print(output_string)

    if(line == '\n'):
        occupied = 0
        output_string = ''
