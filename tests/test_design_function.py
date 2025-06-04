from lib.design_function import *

def test_given_empty_string_output_false():
    result = include_to_do("")
    assert result == False

def test_given_TODO__in_string_output_true():
    result = include_to_do("#TODO")
    assert result == True

def test_given_string_with_TODO_will_output_true():
    result = include_to_do("hello #TODO")
    assert result == True