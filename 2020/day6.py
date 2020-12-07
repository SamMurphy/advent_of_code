
def parse_file(file_name):
    groups = open(file_name).read().split("\n\n")
    return groups

def solve_part1(file_name):
    groups = parse_file(file_name)
    return sum([len(set(group.replace('\n',''))) for group in groups])

def solve_part2(file_name):
    groups = parse_file(file_name)
    return sum([len(set.intersection(*[set(person) for person in group.split()])) for group in groups])

file_name = "input_day5_test.txt"

test = solve_part1(file_name)
assert(test == 11)
print(f'Test Part 1: Unique questions answered: {test}')

test = solve_part2(file_name)
assert(test == 6)
print(f'Test Part 2: Questions everyone answered: {test}')

file_name = "input_day5.txt"
result = solve_part1(file_name)
print(f'Part 1: Unique questions answered: {result}')
result = solve_part2(file_name)
print(f'Part 2: Questions everyone answered: {result}')