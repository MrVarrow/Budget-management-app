import re


def empty_string_inside_widget(contents: str) -> bool:
    if contents == "":
        return True
    return False


def variable_is_none(variable) -> bool:
    if variable is None:
        return True
    return False


def two_strings_are_the_same(string_1: str, string_2: str) -> bool:
    if string_1 == string_2:
        return True
    return False


def false_in_bool_list(bool_list: list[bool]) -> bool:
    if False in bool_list:
        return True
    return False


def special_character_in_string(string: str) -> bool:
    if re.search(r"\W", string):
        return True
    return False


def digits_in_string(string: str) -> bool:
    if re.search("[0-9]", string):
        return True
    return False


# Checks if string is a numeric format like int or decimal with 1 to 3 digits after the decimal point
def valid_quantity_string(string: str) -> bool:
    if re.search(r'^\d+(?:[.]\d{1,2,3}|$)$', string):
        return True
    return False


def tuple_is_empty(given_tuple):
    if given_tuple == ():
        return True
    return False


# Check if string match format: xx.xx or xx
def correct_price_format(string):
    if re.search(r'^\d{1,10}(\.\d{1,2})?$', string):
        return True
    return False


# Check if str had int format with 1 to 3 digits
def string_has_int_format(string):
    if re.search(r'^\d{1,2}$', string):
        return True
    return False


