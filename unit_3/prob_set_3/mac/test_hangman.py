# the user can only send in one letter at a time

from ps3_hangman import isWordGuessed

def test_always_passes():
    assert True

def test_user_guesses_wrong():
    secretWord = "apple"
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    assert isWordGuessed(secretWord, lettersGuessed) == False

def test_user_guesses_correct():
    secretWord = "pork"
    lettersGuessed = ['p', 'o', 'r', 'k']
    assert isWordGuessed(secretWord, lettersGuessed) == True

def test_user_encounters_duplicate_letters():
    secretWord = "apple"
    lettersGuessed = ['a', 'p', 'l', 'e']
    assert isWordGuessed(secretWord, lettersGuessed) == True