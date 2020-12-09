
def parse_file(file_name):
    xmas_data = [int(line) for line in open(file_name)]
    return xmas_data


def smallest_plus_largest(xmas_subset):
    xmas_subset.sort()
    return xmas_subset[0] + xmas_subset[len(xmas_subset) - 1]


def solve_part2(xmas_data, invalid_number):
    for x in range(0, len(xmas_data)):
        sum = xmas_data[x]
        for y in range(x+1, len(xmas_data)):
            sum += xmas_data[y]
            if sum == invalid_number:
                return smallest_plus_largest(xmas_data[x:y+1])
            elif sum > invalid_number:
                break
    return None


def solve_part1(xmas_data, preamble, previous):
    for i in range(preamble, len(xmas_data)):
        current = xmas_data[i]
        valid = False
        for j in range(i - previous, i):
            for k in range(j, i):
                if xmas_data[j] + xmas_data[k] == current:
                    valid = True
                    break
        if not valid:
            return current
    return None

file_name = "input_day9_test.txt"
xmas_data = parse_file(file_name)
test = solve_part1(xmas_data, 5, 5)
assert(test == 127)
print(f'Part 1: Test: First number that doesnt match is {test}')
test = solve_part2(xmas_data, test)
assert(test == 62)
print(f'Part 2: Test: Sum of contigous pair is {test}')

file_name = "input_day9.txt"
xmas_data = parse_file(file_name)
part1 = solve_part1(xmas_data, 25, 25)
print(f'Part 1: First number that doesnt match is {part1}')
part2 = solve_part2(xmas_data, part1)
print(f'Part 2: Sum of contigous pair is {part2}')

