import re

def main():
    with open('input.txt', 'r') as f:
        data = f.read()
    
    sequence = ''
    for idx,letter in enumerate(data):
        sequence += letter
        if len(sequence) == 14:
            if is_unique(sequence):
                print(idx+1)
            else:
                sequence = sequence[1:]

def is_unique(sequence):
    characters = set()
    for char in sequence:
        if char in characters:
            return False
        characters.add(char)
    return True

if __name__ == '__main__':
    main()