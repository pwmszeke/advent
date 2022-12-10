from collections import defaultdict
from itertools import accumulate


def main():
    with open('inputs/9.txt', 'r') as f:
        data = f.read().splitlines()
    
    cycle = 0
    x_register = 1
    current_position = 0
    row = 0
    crt = [[] for i in range(7)]

    for instruction in data:
        if instruction.startswith('no'):
            draw_pixel(current_position, x_register, crt, row)
            cycle += 1
            current_position += 1
            if cycle % 40 == 0:
                row = cycle / 40
                row = int(row)
                current_position = 0
        else:
            number = int(instruction.split(' ')[1])
            draw_pixel(current_position, x_register, crt, row)  
            cycle += 1
            current_position += 1
            if cycle % 40 == 0:
                row = cycle / 40
                row = int(row)
                current_position = 0
            draw_pixel(current_position, x_register, crt, row)             
            cycle += 1
            current_position += 1
            if cycle % 40 == 0:
                row = cycle / 40
                row = int(row)
                current_position = 0
            x_register += number
    for row in crt:
        print("".join(str(x) for x in row))
    
def draw_pixel(current_position, x_register, crt, row):
    if current_position in range(x_register-1, x_register+2):
        crt[row].append('#')
    else:
        crt[row].append('.')

if __name__ == '__main__':
    main()