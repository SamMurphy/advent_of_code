def check_route(grid, down, right):
    number_of_trees_hit = 0
    x = 0
    for y in range(down, len(grid), down):
        x = x + right
        if x >= len(grid[y]):
            x = x - len(grid[y])
        # print(f'Test grid [{x},{y}] = {grid[y][x]}')
        if (grid[y][x] == '#'):
            number_of_trees_hit += 1
    return number_of_trees_hit


def parse_file(file_name):
    lines = [list(line.strip('\n\r')) for line in open(file_name)]
    # for row in lines:
    #    print(row)
    return lines


def part_one(file_name):
    down = 1
    right = 3
    grid = parse_file(file_name)
    return check_route(grid, down, right)


def part_two(file_name):
    grid = parse_file(file_name)
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # right, down
    trees_product = 1
    for slope in slopes:
        trees_hit = check_route(grid, slope[1], slope[0])
        # print(f'Checking slope - Right {slope[0]} Down {slope[1]} - Hits {trees_hit} trees!')
        trees_product *= trees_hit

    return trees_product


print('Testing Part One - Hit {} trees!'.format(part_one("input_day3_test.txt")))
print('Part One - Hit {} trees!'.format(part_one("input_day3.txt")))
print('Testing Part Two - Tree Product is {}'.format(part_two("input_day3_test.txt")))
print('Part Two - Tree Product is {}'.format(part_two("input_day3.txt")))
