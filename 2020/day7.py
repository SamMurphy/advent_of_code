import re

line_parser = re.compile(
    r'^(\w+(?: \w+)?) bags contain ((?:(?:\d+|no) (?:\w+(?: \w+)?) bag(?:s)?(?:, )?)+)\.$')
quanity_parser = re.compile(r'(\d+|no) (\w+(?: \w+)?)')
BAG_NAME = 'shiny gold'


class BagQuantity:
    def __init__(self, rule):
        self.bag = rule[1]
        self.quantity = int(rule[0]) if rule[0] != 'no' else None

    def __repr__(self):
        return f'{self.quantity} {self.bag}'


def parse_file(file_name):
    lines = open(file_name).readlines()
    groups = [line_parser.match(line).groups() for line in lines]
    rules = {group[0]: [BagQuantity(quanity_parser.match(
        bag).groups()) for bag in group[1].split(', ')] for group in groups}
    return rules


def can_carry_bag(type_of_bag, rules):
    bags_that_can_carry = set()
    for bag, can_contain in rules.items():
        for rule in can_contain:
            if type_of_bag in rule.bag:
                bags_that_can_carry.add(bag)
                bags_that_can_carry.update(can_carry_bag(bag, rules))
    return bags_that_can_carry


def contains_bags(type_of_bag, rules):
    count = 0
    for bag, can_contain in rules.items():
        if bag == type_of_bag:
            for rule in can_contain:
                if rule.quantity != None:
                    count += rule.quantity
                    count += rule.quantity * contains_bags(rule.bag, rules)
    return count


def solve_part1(file_name):
    rules = parse_file(file_name)
    bags = can_carry_bag(BAG_NAME, rules)
    return len(bags)


def solve_part2(file_name):
    rules = parse_file(file_name)
    return contains_bags(BAG_NAME, rules)


file_name = "input_day7_test.txt"
test = solve_part1(file_name)
assert(test == 4)
print(f'Part 1: TEST: {test} bags can carry a {BAG_NAME} bag')

file_name = "input_day7_test2.txt"
test = solve_part2(file_name)
assert(test == 126)
print(f'Part 2: TEST: {BAG_NAME} bags contain {test} other bags')

file_name = "input_day7.txt"
print(f'Part 1: {solve_part1(file_name)} bags can carry a {BAG_NAME} bag')
print(f'Part 2: {BAG_NAME} bags contain {solve_part2(file_name)} other bags')
