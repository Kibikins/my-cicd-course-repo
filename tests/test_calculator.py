from src import calculator
 
 
def test_add_numbers():
    assert calculator.add_numbers(2, 3) == 5

 
def test_subtract_numbers():
    assert calculator.subtract_numbers(10, 4) == 6
