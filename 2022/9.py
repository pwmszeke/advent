from collections import defaultdict
from itertools import accumulate


def main():
    with open('inputs/9.txt', 'r') as f:
        data = f.read().splitlines()
    
    cycle = 1
    x_register = 1
    signal_sum = 0

    for instruction in data:
        if instruction.startswith('no'):
            cycle += 1
            if check_cycle(cycle):
                print(f'Cycle {cycle}: {x_register}')
                signal_sum += (cycle * x_register)
        else:
            number = int(instruction.split(' ')[1])
            cycle += 1
            if check_cycle(cycle):
                print(f'Cycle {cycle}: {x_register}')
                signal_sum += (cycle * x_register)
            cycle += 1
            x_register += number
            if check_cycle(cycle):
                print(f'Cycle {cycle}: {x_register}')
                signal_sum += (cycle * x_register)
    print(signal_sum)

def check_cycle(cycle):
    values = [20, 60, 100, 140, 180, 220]
    if cycle in values:
        return True


if __name__ == '__main__':
    main()