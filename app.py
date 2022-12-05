
def main():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    stacks = [
        ['T', 'Z', 'B'],
        ['N', 'D', 'T', 'H', 'V'],

    ]
    total = 0
    for line in data:
        both = line.split(',')
        first = list(map(int, both[0].split('-')))
        second = list(map(int, both[1].split('-')))
        if first[0] >= second[0]:
            if first[1] <= second[1]:
                total += 1
                continue
        if second[0] >= first[0]:
            if second[1] <= first[1]:
                total += 1
    print(total)

if __name__ == '__main__':
    main()