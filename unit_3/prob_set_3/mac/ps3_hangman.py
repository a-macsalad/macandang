import random
import string 

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

# wordlist = loadWords()

def isWordGuessed(secretWord: str, lettersGuessed: list) -> bool:
    correct_letters = [char for char in lettersGuessed if char in secretWord]
    
    if len(correct_letters) == len(set(secretWord)):
        return True
    else:
        return False
    


def getGuessedWord(secretWord: str, lettersGuessed: list) -> str:
    correct_letters = [char for char in lettersGuessed if char in secretWord]
    final_list = []
    
    for char in secretWord:
        if char in correct_letters:
            final_list.append(char)
        else:
            final_list.append("_")
    return " ".join(final_list)



def getAvailableLetters(lettersGuessed: list) -> str:
    alphabet = string.ascii_lowercase
    remainder = [char for char in alphabet if char not in lettersGuessed]

    return "".join(remainder)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    length = len(secretWord)
    rounds = 0
    

    print("")
    print(" ---------------- ")
    print(f"Greetings! The secret word contains {length} letters...")
    print(" ---------------- ")
    print("")


    print("The Rules: You get 1 guess per round. 8 Rounds total.")
    
    guess = input("Give us a letter, precious ")
    print(f"You guessed the letter {guess}")

    # while rounds < 8:
        
    
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# secretWord = "tabulate"
# hangman(secretWord)
