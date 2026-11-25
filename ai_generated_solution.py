def multiply(a, b):
    # Multiply two numbers with type checking
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both arguments must be int or float')
    return a * b

def divide(a, b):
    # Divide a by b with type and zero division checks
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both arguments must be int or float')
    if b == 0:
        raise ZeroDivisionError('Division by zero is undefined')
    return a / b

def add(a, b):
    # Simple addition function
    return a + b

def main():
    # Tests for add
    assert add(1, 2) == 3, 'add(1,2) should be 3'
    assert add(-1, 5) == 4, 'add(-1,5) should be 4'
    assert add(0, 0) == 0, 'add(0,0) should be 0'
    # Tests for multiply
    assert multiply(3, 4) == 12, 'multiply(3,4) should be 12'
    assert multiply(-2, 5) == -10, 'multiply(-2,5) should be -10'
    # Tests for divide
    assert divide(10, 2) == 5, 'divide(10,2) should be 5'
    assert divide(-9, 3) == -3, 'divide(-9,3) should be -3'
    # Test divide by zero raises ZeroDivisionError
    try:
        divide(5, 0)
        assert False, 'divide(5,0) should raise ZeroDivisionError'
    except ZeroDivisionError:
        pass
    # Test type error
    try:
        multiply('a', 2)
        assert False, 'multiply with string should raise TypeError'
    except TypeError:
        pass
    print('All tests passed')

if __name__ == '__main__':
    main()