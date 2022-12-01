
with open('input.txt', 'r') as f:
    data = f.read()
max_total = 0
elf_cals = []

for elf in data.split("\n\n"):
    total = 0
    new_elf = elf.split("\n")
    for item in new_elf:
        total += int(item)
    if total > max_total:
        max_total = total
    elf_cals.append(total)

top_elfs = sum(sorted(elf_cals)[-3:])
print(top_elfs)

