
def parse_file(file_name):
    program = [[line.split()[0], int(line.split()[1])]
               for line in open(file_name).readlines()]
    return program


def execute(program, fix_loop):
    jump_instructions = set()
    nop_instructions = set()
    last_instruction_changed = -1
    first_time = True

    while True:
        infinite_loop = False
        pc = 0
        acc = 0
        executed_instructions = set()
        # Exectue the program
        while pc < len(program):
            if pc in executed_instructions:
                # Stop the program if infinite loop is detected
                infinite_loop = True
                break
            executed_instructions.add(pc)
            # Handle instructions
            if program[pc][0] == 'nop':
                if first_time:
                    nop_instructions.add(pc)
                pc += 1
            elif program[pc][0] == 'acc':
                acc += program[pc][1]
                pc += 1
            elif program[pc][0] == 'jmp':
                if first_time:
                    jump_instructions.add(pc)
                pc += program[pc][1]

        first_time = False
        # If there is an infinite loop, try to fix it
        if fix_loop:
            if infinite_loop:
                # Reset the last instruction we changed
                if last_instruction_changed != -1:
                    program[last_instruction_changed][0] = 'jmp' if program[last_instruction_changed][0] == 'nop' else 'nop'
                if infinite_loop:
                    # Change each of the jump/noop instructions one at a time until the inf loop is fixed
                    if len(jump_instructions):
                        last_instruction_changed = jump_instructions.pop()
                        program[last_instruction_changed][0] = 'nop'
                    elif len(nop_instructions):
                        last_instruction_changed = nop_instructions.pop()
                        program[last_instruction_changed][0] = 'jmp'

        if not fix_loop or not infinite_loop:
            break

    return acc


def solve_part2(file_name):
    program = parse_file(file_name)
    acc = execute(program, True)
    return acc


def solve_part1(file_name):
    program = parse_file(file_name)
    acc = execute(program, False)
    return acc


file_name = "input_day8_test.txt"
test = solve_part1(file_name)
assert(test == 5)
print(f'Part 1: TEST: Value before infinite loop: {test}')
test = solve_part2(file_name)
assert(test == 8)
print(f'Part 2: TEST: Value of fixed program: {test}')


file_name = "input_day8.txt"
print(f'Part 1: Value before infinite loop: {solve_part1(file_name)}')
print(f'Part 2: TEST: Value of fixed program: {solve_part2(file_name)}')
