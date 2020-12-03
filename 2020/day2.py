def test_rule_one(password, character, minimum, maximum):
    count = 0
    for letter in password:
        if letter == character:
            count += 1
        if count > maximum:
            break
    if count <= maximum and count >= minimum:
        return True
    return False


def test_rule_two(password, character, index_one, index_two):
    if (password[index_one] == character) != (password[index_two] == character):
        return True
    return False


def solve(file_name):
    valid_rule_one_passwords = 0
    valid_rule_two_passwords = 0

    lines = [line.split(" ") for line in open(file_name)]

    for line in lines:
        # Parse rules
        # Get min and max
        min_max = line[0].split("-")
        minimum = int(min_max[0])
        maximum = int(min_max[1])
        # Get character
        character = line[1][0:1]
        # Get the password
        password = line[2].strip("\n\r")
        # Test the rules
        valid_rule_one_passwords += test_rule_one(
            password, character, minimum, maximum)
        valid_rule_two_passwords += test_rule_two(
            password, character, minimum - 1, maximum - 1)

    return [valid_rule_one_passwords, valid_rule_two_passwords]


#file_name = "input_day2_test1.txt"
file_name = "input_day2.txt"

print('--- String Splitting ---')
results = solve(file_name)
print(f'Valid Rule 1 Passwords: ', results[0])
print(f'Valid Rule 2 Passwords: ', results[1])
