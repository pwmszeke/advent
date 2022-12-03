
def main():
    with open('input.txt', 'r') as f:
        data = f.readlines()

    total = 0
    idx = 0

    for line in data:
        if idx+2 > len(data):
            break
        first, second, third = data[idx].strip(), data[idx+1].strip(), data[idx+2].strip()
        common_letter = ''.join(set(first).intersection(second).intersection(third))
        print(common_letter)
        total += get_value(common_letter)
        idx += 3

    print(total)

def get_value(letter):
    if letter.islower():
        return ord(letter) - 96    
    else:
        return ord(letter) - 38

if __name__ == '__main__':
    main()