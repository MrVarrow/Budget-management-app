import re
from datetime import datetime
from email_validator import validate_email


# Checks if string is empty
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


def tuple_is_empty(given_tuple: tuple) -> bool:
    if given_tuple == ():
        return True
    return False


# Check if string match format: xx.xx or xx
def correct_price_format(string: str) -> bool:
    if re.search(r'^\d{1,10}(\.\d{1,2})?$', string):
        return True
    return False


# Check if str had int format with 1 to 3 digits
def string_has_int_format(string: str) -> bool:
    if re.search(r'^\d{1,2}$', string):
        return True
    return False


# Check if variable is grater than result of difference of 2 variables
def variable_grater_than_difference(variable: int, diff_component_1: int, diff_component_2: int) -> bool:
    if int(variable) > int(diff_component_1) - int(diff_component_2):
        return True
    return False


# Check if one variable is grater than other
def variable_grater_than_other_variable(variable_1: int, variable_2: int) -> bool:
    if int(variable_1) > int(variable_2):
        return True
    return False


# Check if string starts with letter, has 1-30 letters with spaces allowed
def string_with_only_letters_and_spaces(string: str) -> bool:
    if re.search(r'^[a-zA-Z][a-zA-Z\s]{0,29}$', string):
        return True
    return False


# Check if given date is in the past
def the_given_date_has_already_passed(given_date) -> bool:
    today = datetime.now().date()
    if given_date > today:
        return True
    return False


# Check if number is between 0 and 20 (including 20)
def number_between_0_and_20(number: int) -> bool:
    if 0 < int(number) <= 20:
        return True
    return False


# Check if length of the string is more or equal than given number
def length_of_string_more_equal_than(string: str, desire_length: int) -> bool:
    if len(string) >= desire_length:
        return True
    return False


def lower_char_in_string(string: str) -> bool:
    if re.search("[a-z]", string):
        return True
    return False


def upper_char_in_string(string: str) -> bool:
    if re.search("[A-Z]", string):
        return True
    return False


# External lib for validation
def validate_email_address(email: str) -> None:
    validate_email(email)
