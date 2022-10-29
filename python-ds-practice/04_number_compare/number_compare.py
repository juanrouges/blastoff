def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    first = a
    second = b

    result = None

    if first > second:
        result = "First number is greater"
    elif first < second:
        result = "Second number is greater"
    else:
        result = "Numbers are equal"

    return result     