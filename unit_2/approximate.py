cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.001
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
    print("num guesses = ", num_guesses)

    if abs(guess ** 3 - cube) >= epsilon:
        print("Failed on cube root of ", cube)
    else:
        print(guess, " is close to the cube root of ", cube)

"""
This is a pretty static problem meant to show the steps of incrementing through loops

Explanation:

(line 1 to 5): outlines the different variables for this procedure.

(line 7): abs(0.0 ** 27) is 0.0, which is less than epsilon, so we go into that loop and increment our guess input as well as the number of guesses. The next time we run this check in the while loop, we will be checking if: 

`abs(0.001 ** 27)` is larger than epsilon. Then,

`abs(0.002 ** 27)` is larger than epsilon. Then,

`abs(0.003 ** 27)` is larger than epsilon... so on and so forth. Because we are incrementing the guess variable every time we check to see that it is less than epsilon (which is 0.1).

Try changing the `cube` variable (line 1) to any number and run the code. Try a smaller number and see the console output. Then, try increasing the `increment` variable. Just to move the program faster.
"""