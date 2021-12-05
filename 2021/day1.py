from numpy import loadtxt

inputs = loadtxt("input_day1.txt")
#inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print(inputs)

def count_increases(data):
    if len(data) <= 1: return 0
    increases = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            increases += 1
    return increases

print(f'Part 1: Number of increases in data: {count_increases(inputs)}')

size_of_window = 3
window_sums = []

for i in range(size_of_window - 1, len(inputs)):
    sum = 0
    for x in range(0, size_of_window):
        sum += inputs[i - x]
    window_sums.append(sum)

print(f'Part 2: Number of increases in window sums: {count_increases(window_sums)}')