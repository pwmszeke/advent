
def main():
    with open('input.txt', 'r') as f:
        data = f.readlines()

    total = 0

    for game in data:
        inputs = game.strip().split(' ')
        total += calc_score(inputs[0], inputs[1])
    print(total)

# A = Rock
# B = Paper
# C = Scissors

# X = Lose = 0
# Y = Draw = 3
# Z = Win = 6

# Rock  = 1
# Paper  = 2
# Scissors   = 3
def calc_score(them, you):
    if them == 'A':
        if you == 'X':
            return 3
        if you == 'Y':
            return 4
        if you == 'Z':
            return 8
    if them == 'B':
        if you == 'X':
            return 1
        if you == 'Y':
            return 5
        if you == 'Z':
            return 9
    if them == 'C':
        if you == 'X':
            return 2
        if you == 'Y':
            return 6
        if you == 'Z':
            return 7


if __name__ == '__main__':
    main()