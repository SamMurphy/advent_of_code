import re


class PasswordData:
    def __init__(self, password_data):
        self.min = int(password_data[0])
        self.max = int(password_data[1])
        self.char = password_data[2]
        self.password = password_data[3]


def regex(file_name):
    parser = re.compile(r'(\d+)-(\d+)\s(\w):\s(\w+)')
    lines = [PasswordData(parser.match(line).groups())
             for line in open(file_name)]

    rule1_passwords = [password_data for password_data in lines if password_data.min <=
                       password_data.password.count(password_data.char) <= password_data.max]

    rule2_password = [data for data in lines if (
        data.password[data.min - 1] == data.char) != (data.password[data.max - 1] == data.char)]

    return [len(rule1_passwords), len(rule2_password)]


#file_name = "input_day2_test1.txt"
file_name = "input_day2.txt"

print('--- Regular Expressions Time ---')
results = regex(file_name)
print(f'Valid Rule 1 Passwords: ', results[0])
print(f'Valid Rule 2 Passwords: ', results[1])
