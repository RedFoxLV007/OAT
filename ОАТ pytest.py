# pip install pytest = устанавили пай-тест (в консоли)

import pytest # импорт модуль пай-тест

# def test_capital_case():
#
#     assert "semaphore".capitalize()=="Semaphore"
#
# def test_raises_exeption_on_non_string_arguments():
#     with pytest.raises(TypeError):
#         "semaphore".capitalize(9)



def is_triangle(a,b,c):
    return a + b > c # return bool

# test_case
def test_is_triangle_base_test():
    result = is_triangle(2,4,5)
    expected_result = True
    assert expected_result == result

def test_is_triangle_isnot_exist():
    result = is_triangle(7,1,1)
    expected_result = False
    assert expected_result == result

def test_is_triangle_negative_test():
    result = is_triangle(-2, -4, -5)
    expected_result = False
    assert expected_result == result

