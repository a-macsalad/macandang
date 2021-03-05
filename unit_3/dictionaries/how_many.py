animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0

    for alp in aDict:
        count = count + len(aDict[alp])
    
    print(count)

how_many(animals)