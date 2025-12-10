import re

def get_number(input: str) -> int:
    numbers = re.findall(r'\d', input)
    first_and_last = numbers[0] + numbers[-1]
    return int(first_and_last)

def get_total(inputs: list) -> int:
    total = 0
    for line in inputs:
        total += get_number(line)
    return total


with open('catherine_input.txt', 'r') as file:
    data = file.readlines()
    print(get_total(data))
        

    