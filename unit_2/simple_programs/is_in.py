def isIn(char: str, aStr: str) -> bool:
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    
    if len(aStr) == 1:
      return aStr == char

    middle_idx = int(len(aStr) / 2) # after division, it's a float. so change to Int
    sorted_str = "".join(sorted(aStr))

    middle_char = sorted_str[middle_idx]
    
    if middle_char == char: 
        return True
    elif char < middle_char:
        return isIn(char, sorted_str[:middle_idx])
    else:
        return isIn(char, sorted_str[middle_idx:])
    


# import code; code.interact(local=dict(globals(), **locals()))
