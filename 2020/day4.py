import re

field_parser = re.compile(r'([a-z]{3}):(.*)')
year_parser = re.compile(r'^(\d{4})$')
height_parser = re.compile(r'^(\d+)([a-z]{2})$')
hair_parser = re.compile(r'^#[0-9|a-f]{6}$')
eye_parser = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
pid_parser = re.compile(r'^([0-9]{9})$')


class PassportField:
    def __init__(self, passport_data):
        self.header = passport_data[0]
        self.data = passport_data[1]

    def __str__(self):
        return f'{self.header}: {self.data}'


def parse_file(file_name):
    passports = [line.split() for line in open(
        file_name, "r").read().split("\n\n")]

    for i in range(0, len(passports)):
        passports[i] = [PassportField(field_parser.match(
            field).groups()) for field in passports[i]]

    return passports


def validate_field(header, data):
    if header == "byr":
        if year_parser.match(data):
            year = int(year_parser.match(data).groups()[0])
            if year >= 1920 and year <= 2002:
                return True
        return False
    elif header == "iyr":
        if year_parser.match(data):
            year = int(year_parser.match(data).groups()[0])
            if year >= 2010 and year <= 2020:
                return True
        return False
    elif header == "eyr":
        if year_parser.match(data):
            year = int(year_parser.match(data).groups()[0])
            if year >= 2020 and year <= 2030:
                return True
        return False
    elif header == "hgt":
        if height_parser.match(data):
            height_data = height_parser.match(data).groups()
            height = int(height_data[0])
            units = height_data[1]
            if units == "cm" and height >= 150 and height <= 193:
                return True
            elif units == "in" and height >= 59 and height <= 76:
                return True
        return False
    elif header == "hcl":
        if hair_parser.match(data):
            return True
        return False
    elif header == "ecl":
        if eye_parser.match(data):
            return True
        return False
    elif header == "pid":
        if pid_parser.match(data):
            return True
        return False
    elif header == "cid":
        return True
    else:
        return False


def solve_part1(file_name):
    valid_count = 0
    passports = parse_file(file_name)
    for passport in passports:
        if len(passport) == 8:
            valid_count += 1
        elif len(passport) == 7:
            for field in passport:
                no_cid = True
                if "cid" in field.header:
                    no_cid = False
                    break
            valid_count += no_cid

    return valid_count


def solve_part2(file_name):
    valid_count = 0
    passports = parse_file(file_name)

    for passport in passports:
        valid_number_of_fields = False
        if len(passport) >= 7:
            valid_number_of_fields = True
        fields_validated = True
        for field in passport:
            if len(passport) == 7 and field.header == "cid":
                valid_number_of_fields = False
                break
            fields_validated = validate_field(field.header, field.data)
            if not fields_validated:
                break
        if valid_number_of_fields and fields_validated:
            valid_count += 1

    return valid_count


# file_name = "input_day4_test.txt"
#file_name = "input_day4_test2.txt"
file_name = "input_day4.txt"

print(f'Part 1: There are {solve_part1(file_name)} valid passports')  # 233 | 8
print(f'Part 2: There are {solve_part2(file_name)} valid passports')  # 111 | 4
