def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test_val = a if a < b else b
    
    while test_val > 1:
        if a % test_val != 0 or b % test_val != 0:
            test_val = test_val - 1
        else:
            break
        
    return test_val