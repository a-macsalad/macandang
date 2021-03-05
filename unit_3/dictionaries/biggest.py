animals = { 'a': ['aardvark'], 'b': ['baboon', "bear"], 'c': ['coati', "cat", "cockatoo"]}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    max_num = max(aDict, key=aDict.get)

    return max_num
    

biggest(animals)
    