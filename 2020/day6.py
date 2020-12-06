
def parse_file(file_name):
    groups = open(file_name).read().split("\n\n")
    return groups

def solve_part1(file_name):
    groups = parse_file(file_name)
    return sum([len(set(group.replace('\n',''))) for group in groups])

def solve_part2(file_name):
    groups = parse_file(file_name)
    return sum([len(set.intersection(*[set(x) for x in block.split()])) for block  in groups])

test_file = "input_day5_test.txt"
file_name = "input_day5.txt"

test = solve_part1(test_file)
assert(test == 11)
print(f'Test Part 1: The sum of the questions is: {test}')

result = solve_part1(file_name)
print(f'Part 1: The sum of the questions is: {result}')

test = solve_part2(test_file)
assert(test == 6)
print(f'Test Part 2: The sum of the questions everyone answered is: {test}')

result = solve_part2(file_name)
print(f'Part 1: The sum of the questions everyone answered is: {result}')