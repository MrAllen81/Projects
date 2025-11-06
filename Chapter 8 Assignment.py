print("Welcome to Tyler's 5 Question Math Quiz!")
print("GOOD LUCK!")
first_number = [100, 90, 36, 200, 150, 70, 35, 18, 90, 11, 14]
second_number = [5, 3, 3, 4, 5, 5, 7, 3, 9, 11, 7]
def MathQuiz():
    attempts = 3
    while attempts == 3:
        Question1 = print("What is ", first_number[0], " / " , second_number[0], "?")
        print("a) 21")
        print("b) 20.5")
        print("c) 15")
        print("d) 20")
        answer1 = input("Choose the correct letter. ").lower()
        if answer1 == "d":
            print("That is correct!")
            attempts = 10
        elif answer1 == "skip":
            attempts = 10
        elif answer1 == "a" or "b" or "c":
            print("Sorry that is incorrect! Try Again!")
            print("Type 'skip' if you want to skip to next question")
            attempts = 3
        elif answer1 == "skip":
            attempts = 10
    while attempts == 10:
        Question2 = print("What is ", first_number[5], " / " , second_number[4], "?")
        print("a) 14")
        print("b) 16")
        print("c) 15")
        print("d) 14.5")
        answer2 = input("Choose the correct letter: ").lower()
        if answer2 == "a":
            print("That is correct!")
            attempts = 20
        elif answer2 == "skip":
            attempts = 20
        elif answer2 =="b" or "c" or "d":
            print("Sorry that is incorrect! Try Again!")
            print("Type 'skip' if you want to skip to next question")
            attempts = 10
    while attempts == 20:
        Question3 = print("What is ", first_number[6], " * " , second_number[9], "?")
        print("a) 380")
        print("b) 345")
        print("c) 385")
        print("d) 485")
        answer3 = input("Choose the correct letter: ").lower()
        if answer3 == "c":
            print("That is correct!")
            attempts = 30
        elif answer3 == "skip":
            attempts = 30
        elif answer3 == "a" or "b" or "d":
            print("Sorry that is incorrect! Try Again!")
            print("Type 'skip' if you want to skip to next question")
            attempts = 20
    while attempts == 30:
        Question4 = print("What is ", first_number[1], " * " , first_number[7], "?")
        print("a) 1,080")
        print("b) 1,620")
        print("c) 1,095")
        print("d) 2,620")
        answer4 = input("Choose the correct letter: ").lower()
        if answer4 == "b":
            print("That is correct!")
            attempts = 40
        elif answer4 == "skip":
            attempts = 40
        elif answer4 == "a" or "c" or "d":
            print("Sorry that is incorrect! Try Again!")
            print("Type 'skip' if you want to skip to next question")
            attempts = 30
    while attempts == 40:
        Question5 = print("What is ", first_number[2], " * " , second_number[1], "?")
        print("a) 108")
        print("b) 98")
        print("c) 80")
        print("d) 99")
        answer5 = input("Choose the correct letter: ").lower()
        if answer5 == "a":
            print("That is correct!")
            attempts = 50
        elif answer5 == "skip":
            attempts = 50
        elif answer5 == "b" or "c" or "d":
            print("Sorry that is incorrect! Try Again!")
            print("Type 'skip' if you want to skip to next question")
            attempts = 40
    if attempts == 50:
        print("Thank you for taking my quiz")
                    
                    


MathQuiz()
