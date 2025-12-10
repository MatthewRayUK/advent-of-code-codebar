from day1_part2 import get_number


def test_text_to_number():
    text = 'onethsseven'
    number = get_number(text)
    assert number == 17

def test_mixed_text_to_number():
    text = '4hdye8nine'
    number = get_number(text)
    assert number == 49

def test_mixed_text_to_number_2():
    text = 'zoneight234'
    number = get_number(text)
    assert number == 14

def test_just_numbers():
    text = '9h1xcrcggtwo38'
    number = get_number(text)
    assert number == 98

def test_single_number():
    text = 'mztttgnxdqt4'
    number = get_number(text)
    assert number == 44

def test_single_number_2():
    text = '3fiveone\n'
    number = get_number(text)
    assert number == 31

def test_short_input():
    text = '9g'
    number = get_number(text)
    assert number == 99