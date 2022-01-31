import pytest

@pytest.mark.parametrize("input_x, expected_y", [
    [1, 5], 
    [2, 10],
    [3, 15]])

    
def test_line_function(input_x, expected_y):
    from line_function import line_function_creation
    answer = line_function_creation(input_x)
    assert answer == expected_y