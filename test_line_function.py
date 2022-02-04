import pytest

@pytest.mark.parametrize("input_x1, input_x2, input_x3, expected_y", [
    [(1,2), (2,4), (3,6),  True], 
    [(2,4), (4,8), (6,12), True], 
    ])

    
def test_line_function(input_x1, input_x2, input_x3, expected_y):
    from line_function import line_function_creation
    answer = line_function_creation(input_x1, input_x2, input_x3)
    assert answer == expected_y