import re

parser = re.compile(
    r'(byr:(?P<byr>\d{4})(\s|$)+|iyr:(?P<iyr>\d{4})(\s|$)+|eyr:(?P<eyr>\d{4})(\s|$)+|hgt:(?P<hgt>\d+(cm|in))(\s|$)+|hcl:#(?P<hcl>[0-9|a-f]{6})(\s|$)+|ecl:(?P<ecl>(amb|blu|brn|gry|grn|hzl|oth))(\s|$)+|pid:(?P<pid>[0-9]{9})(\s|$)+|cid:(?P<cid>\d+)(\s|$)+)*')
height_parser = re.compile(r'^(?P<height>\d+)(?P<unit>cm|in)$')

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def valid_range(value, min, max):
    return min <= int(value) <= max


def validate_passport(passport):
    # Check all the required fields are present
    if set(passport.keys()) >= required_fields:
        # Check the ranges on the years
        valid_year = valid_range(passport.get("byr"), 1920, 2002) and valid_range(
            passport.get("iyr"), 2010, 2020) and valid_range(passport.get("eyr"), 2020, 2030)
        # Extract the height and check it's range based on units
        parsed_height = height_parser.match(passport.get("hgt")).groupdict()
        if parsed_height.get("unit") == "cm":
            valid_height = valid_range(parsed_height.get("height"), 150, 193)
        else:
            valid_height = valid_range(parsed_height.get("height"), 59, 76)
        # Passport is valid if all the years and the height are valid
        return valid_year and valid_height
    # Doesn't have the required fields
    return False


def parse_file(file_name):
    passports = open(file_name, "r").read().split("\n\n")
    for i in range(0, len(passports)):
        # remove newlines that are in the middle
        temp = passports[i].replace("\n", " ")
        # find valid fields (doesn't handle year/height ranges)
        # if one invalid field is found it will stop filling others in
        temp = parser.match(temp).groupdict()
        # remove None items
        passports[i] = {k: v for k, v in temp.items() if v is not None}
    return passports


def solve(file_name):
    passports = parse_file(file_name)
    valid_count = 0
    for passport in passports:
        valid_count += validate_passport(passport)
    return valid_count


# file_name = "input_day4_test.txt"
#file_name = "input_day4_test2.txt"
file_name = "input_day4.txt"

print(f'Part 2: There are {solve(file_name)} valid passports')
