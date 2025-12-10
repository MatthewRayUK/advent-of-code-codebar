from day1 import get_number, get_total

def test_total_142():
    list_input = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    total = get_total(list_input)
    assert total == 142

def test_get_line_number():
    text = '1abc2'
    num = get_number(text)
    assert num == 12 

def test_get_line_number_2():
    text = 'a1b2c3d4e5f'
    num = get_number(text)
    assert num == 15

def test_get_line_number_3():
    text = 'treb7uchet'
    num = get_number(text)
    assert num == 77

def test_get_line_number_4():
    text = 'qfrpksmzzvfkddtfh6838'
    num = get_number(text)
    assert num == 68