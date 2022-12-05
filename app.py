import re

def main():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    stacks = [[] for _ in range(9)]
    total = 0
    n = 4
    for line in data:
        chunks = [line[i:i+n] for i in range(0, len(line), n)]
        for idx,stack in enumerate(chunks):
            if stack.strip() != '':
                stacks[idx].append(stack.strip().replace('[','').replace(']',''))
        total += 1
        if total > 7:
            break

    for line in data:
        if line.startswith('move'):
            directions = line.split(' ')
            number_of_items = int(directions[1])
            source = int(directions[3]) - 1
            destination = int(directions[5]) - 1
            new_list = []
            for num in range(int(number_of_items)):
                new_list.append(stacks[source][0])
                stacks[source].pop(0)
            stacks[destination] = new_list + stacks[destination]

    final_str = ''
    for stack in stacks:
        final_str += stack[0]
    print(final_str)


if __name__ == '__main__':
    main()