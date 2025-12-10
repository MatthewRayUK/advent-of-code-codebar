import re
def get_number(input: str) -> int:
    result = re.findall(r"(one|two|three|four|five|six|seven|eight|nine|\d)", input)
    numbers_dict = {
        'one': 1, 
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    if result[0] in numbers_dict.keys():
        first_number = str(numbers_dict[result[0]])
    else:
        first_number = result[0]

    if result[-1] in numbers_dict.keys():
        second_number = str(numbers_dict[result[-1]])
    else:
        second_number = result[-1]
    first_and_last = first_number + second_number
    return int(first_and_last)

def get_total(inputs: list) -> int:
    total = 0
    for line in inputs:
        print(get_number(line))
        total += get_number(line)
    return total

with open('catherine_input.txt', 'r') as file:
    data = file.readlines()
    print(get_total(data))