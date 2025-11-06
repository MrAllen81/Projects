# Answer to Test 2 Practice Test Programming Problem #2
# Guess the secret number
def main():
    again = "y"
    while again == "y":
        secret_number = "7"    #Set the secret number to "7"
        guesses = 3            #Initialize number of guesses to 3
        # Ask the user to guess the number.
        # If they use all 3 guesses then
        # The "while" loop ends and the game is over.
        # If they guess the correct number then the
        # the code will break out of the while loop and and the game is oer.
        answer = input("Guess a number between 1 and 10: ")
        while guesses > 0:            # While there are still guesses left
            if answer==secret_number:
                print("You guess the number!")
                break                 # The user guess correctly so break out of the loop
            else:
                guesses = guesses - 1
                print("Sorry that is not correct.")
                if guesses == 0:
                    print("Sorry, you are out of guesses")
                else:
                    answer = input("Guess a number between 1 and 10: ")
        again =input("Would you like to play again? Type Y or N: ").lower()
    print("Game over. Thank you for playing. ")
    
main()
            
