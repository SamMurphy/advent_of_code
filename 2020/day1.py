from numpy import loadtxt

inputs = loadtxt("input_day1.txt")
inputs.sort()

number_of_iters = 0
# find two inputs that sum to 2020
for x in range(0, len(inputs)):
    for y in range(x, len(inputs)):
        number_of_iters += 1
        if (inputs[x] + inputs[y]) == 2020:
            print(
                f'Inputs {x} and {y} add up to 2020 - {inputs[x]} + {inputs[y]} = 2020')
            output = inputs[x] * inputs[y]
            print(f'Answer: {output}')
        elif (inputs[x] + inputs[y]) > 2020:
            break

print(f'Number of iterations: {number_of_iters}')

number_of_iters = 0
# find three inputs that sum to 2020
for x in range(0, len(inputs)):
    for y in range(x, len(inputs)):
        if (inputs[x] + inputs[y]) > 2020:
            break
        for z in range(y, len(inputs)):
            number_of_iters += 1
            if (inputs[x] + inputs[y] + inputs[z]) == 2020:
                print(
                    f'Inputs {x}, {y}, and {z} add up to 2020 - {inputs[x]} + {inputs[y]} + {inputs[z]} = 2020')
                output = inputs[x] * inputs[y] * inputs[z]
                print(f'Answer: {output}')
            elif (inputs[x] + inputs[y] + inputs[z]) > 2020:
                break

print(f'Number of iterations: {number_of_iters}')
