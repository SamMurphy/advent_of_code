

ROW_CHARACTERS = 7
COLUMN_CHARACTERS = 3

def parse_file(file_name):
    boarding_passes = [line for line in open(file_name)]
    return boarding_passes

def get_seat_info(boarding_pass):
    row_string = boarding_pass[0: ROW_CHARACTERS]
    column_string = boarding_pass[ROW_CHARACTERS: ROW_CHARACTERS + COLUMN_CHARACTERS]
    # Convert from string to binary
    row_string = row_string.replace('B', '1')
    row_string = row_string.replace('F', '0')
    column_string = column_string.replace('R', '1')
    column_string = column_string.replace('L', '0')
    # Convert from binary to int
    row_number = int(row_string, 2)
    column_number = int(column_string, 2)
    return [row_number, column_number]

def get_seat_id(row, column):
    return row * 8 + column

def get_sorted_seat_ids(boarding_passess):
    seat_ids = []
    for i in range(0, len(boarding_passess)):
        seat_info = get_seat_info(boarding_passess[i])
        seat_ids.append(get_seat_id(seat_info[0], seat_info[1]))
    seat_ids.sort()
    return seat_ids

def solve_part2(file_name):
    boarding_passes = parse_file(file_name)
    # Get the ordered list of all ids
    seat_ids = get_sorted_seat_ids(boarding_passes)
    # Find the missing number
    for i in range(0, len(seat_ids)):
        if seat_ids[i + 1] != seat_ids[i] + 1:
            return seat_ids[i] + 1


def solve_part1(file_name):
    boarding_passes = parse_file(file_name)
    highest_id = 0
    for boarding_pass in boarding_passes:
        seat_info = get_seat_info(boarding_pass)
        seat_id = get_seat_id(seat_info[0], seat_info[1])
        if seat_id > highest_id:
            highest_id = seat_id
    return highest_id

def print_seat_info(boarding_pass):
    seat_info = get_seat_info(boarding_pass)
    seat_id = get_seat_id(seat_info[0], seat_info[1])
    print(f'Row: {seat_info[0]} \tColumn: {seat_info[0]} \tSeat ID: {seat_id}')

def test_part1():
    print_seat_info('BFFFBBFRRR')
    print_seat_info('FFFBBBFRRR')
    print_seat_info('BBFFBBFRLL')

test_part1()
print(f'Part 1: Highest ID: {solve_part1("input_day5.txt")}')
print(f'Part 2: My seat ID: {solve_part2("input_day5.txt")}')