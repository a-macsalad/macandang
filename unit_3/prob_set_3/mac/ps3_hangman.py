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


# wordlist = loadWords()

def isWordGuessed(secretWord: str, lettersGuessed: list) -> bool:
    correct_letters = [char for char in lettersGuessed if char in secretWord]
    
    if len(correct_letters) == len(set(secretWord)):
        return True
    else:
        return False
    


def getGuessedWord(secretWord: str, lettersGuessed: list) -> str:
    correct_letters = [char for char in lettersGuessed if char in secretWord]

    string_representation = ["_" for x in range(len(secretWord))]
    
    for char in secretWord:
        if char in correct_letters:
            location_idx = [i for i, a in enumerate(secretWord) if a == char] # returns array of indexes

            for idx in location_idx:
                string_representation[idx] = char

    return " ".join(string_representation)



def getAvailableLetters(lettersGuessed: list) -> str:    
    alphabet = string.ascii_lowercase
    remainder = [char for char in alphabet if char not in lettersGuessed]

    return "".join(remainder)

 
def letterAlreadyChosen(letter: str, letters_guessed: list):
    print("")
    print(f"You've already guessed the letter {letter}, you dolt!")
    print("These are your guesses \n", letters_guessed)

def hangman(secretWord: str):
    length = len(secretWord)
    letters_guessed = []
    mistakes_made = 0
    guesses = 8
    game_complete = False

    print("")
    print(" ---------------- ---------------- ----------------")
    print(f"Greetings! I am thinking of a secret word that is {length} letters...")
    print("")
    print("")

    while game_complete != True:
        print("")
        print(" ---------------- ")
        print(f"You have {guesses} guesses left")
        print("You have these available letters: ", getAvailableLetters(letters_guessed))
        print("")

        guess = input("Give us a letter, precious...\n")

        if guess == "":
            print("Choose a letter, dude")

        if guess in secretWord:
            if guess in letters_guessed:
                letterAlreadyChosen(guess, letters_guessed)
                continue

            print("")
            print(f"You guessed the letter {guess}")
            print("Correct!\n")            
        
            letters_guessed.append(guess)
            existing = getGuessedWord(secretWord, letters_guessed)

            print("What your mystery word looks like: \n", existing)
        else:
            if guess in letters_guessed:
                print("IDIOT! You've tried that letter and it didn't work") 

            print("WRONG! That is not in the damn word. FOCUS!") 
            letters_guessed.append(guess)
            guesses -= 1
        #     print(f"Oops! The letter {guess} is not in my word! Hahaha!")
            print("Your hint again: ", getGuessedWord(secretWord, letters_guessed))
        
    
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = "apple"
hangman(secretWord)
