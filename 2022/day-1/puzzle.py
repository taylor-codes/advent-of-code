cal_counts_list = []

with open('input.txt', 'r') as file:
    curr_elf_cal_count = 0
    max_elf_cal_count = 0
    for line in file:
        if line.strip():
            curr_elf_cal_count += int(line.strip())
        else:
            cal_counts_list.append(curr_elf_cal_count)
            curr_elf_cal_count = 0

print(f'Part 1 solution: {max(cal_counts_list)}')

cal_counts_list.sort()
print(f'Part 2 solution: {sum(cal_counts_list[-3:])}')
