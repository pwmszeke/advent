import re

def main():
    with open('input.txt', 'r') as f:
        data = f.read()
    
    sequence = ''
    starting_index = 0
    for idx,letter in enumerate(data):
        if letter in sequence:
            sequence = ''
        else:
            sequence += letter
            if len(sequence) > 3:
                print(idx-3)


if __name__ == '__main__':
    main()