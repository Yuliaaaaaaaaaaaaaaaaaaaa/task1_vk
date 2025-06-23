import pytest


#pytest tests.py --html=report.html
def reverse_string(s):
    s = s[::-1]
    return s


def count_vowels(s):
    c = 0
    s = s.lower()
    vowels = 'aeiouyаоуэиыеёюя'
    for i in s:
        if i in vowels:
            c += 1
    return c


def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    return False


@pytest.mark.parametrize("string, str_expected_result", [
    ("", ""),
    ("a", "a"),
    ("abc d", "d cba"),
    (" ", " "),
    ("asdfg", 'gfdsa'),
])
def test_reverse_string(string, str_expected_result):
    assert reverse_string(string) == str_expected_result


'''
("", "") проверяем пустую строку
("a", "a") проверяем 1-символьную строку
("abc d", "d cba") проверяем строку с пробелом
(" ", " ") проверяем пробел
("asdfg", 'gfdsa') проверяем обычную строку (не пустую, без пробелов)
'''


@pytest.mark.parametrize("vowels, vow_expected_result", [
    ("", 0),
    (" ", 0),
    ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \
    абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ \
    !#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789", 32),
    ('"', 0),
    ("aAaWqer", 4),
])
def test_count_vowels(vowels, vow_expected_result):
    assert count_vowels(vowels) == vow_expected_result

'''
("", 0) проверяем пустую строку
(" ", 0) проверяем пробел
("a ... 9", 32) проверяем, работает ли функция для букв с различным регистром,
а также работу ф-ции только на гласные(для этого включены в строку все символы)
('"', 0) это символ, не включённый в предыдущем тесте, поэтому его проверяем
("aAaWqer", 4) рандомная строка на случай если в тесте "a ... 9" ответ неправильно
работающей функции совпадёт с правильным ответом (вероятность большая)
'''


@pytest.mark.parametrize("palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("asdfggfdsa", True),
    ("AsdfgfDsa", True),
    ("Was it a car or a cat I saw", False),
    ("abcde", False)
])
def test_is_palindrome(palindrome, expected_result):
    assert is_palindrome(palindrome) == expected_result

'''
("", True) проверяем пустую строку
("a", True) проверяем 1-символьную строку
("asdfggfdsa", True) проверяем палиндром-строку с четным кол-вом символом
("AsdfgfDsa", True) проверяем палиндром-строку с нечетным кол-вом символом
и разным регистром у букв
("Was it a car or a cat I saw", True) проверяем палиндром-слово, при
котором сама строка палиндромом не является (но сл/соч является)
("abcde", False) проверяем не палиндром
'''