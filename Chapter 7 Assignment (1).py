first_number = [100, 90, 36, 200, 150, 70, 35, 18, 90, 11, 14]
second_number = [5, 3, 3, 4, 5, 5, 7, 3, 9, 11, 7]
def MathQuiz():
    score = 0
    Question1 = print("What is ", first_number[0], " / " , second_number[0], "?")
    print("a) 21")
    print("b) 20.5")
    print("c) 15")
    print("d) 20")
    answer1 = input("Choice the correct letter: ").lower()
    if answer1 =="d":
         score = score+1
         print("That is correct! Your score is now:",score)
    else:
        print("Sorry that is incorrect!")
        print("Your score is still:",score)
    Question2 = print("What is ", first_number[5], " / " , second_number[4], "?")
    print("a) 14")
    print("b) 16")
    print("c) 15")
    print("d) 14.5")
    answer1 = input("Choice the correct letter: ").lower()
    if answer1 =="a":
         score = score+1
         print("That is correct! Your score is now:",score)
    else:
        print("Sorry that is incorrect!")
        print("Your score is still:",score)
    Question3 = print("What is ", first_number[6], " * " , second_number[9], "?")
    print("a) 380")
    print("b) 345")
    print("c) 385")
    print("d) 485")
    answer1 = input("Choice the correct letter: ").lower()
    if answer1 =="c":
         score = score+1
         print("That is correct! Your score is now:",score)
    else:
        print("Sorry that is incorrect!")
        print("Your score is still:",score)
    Question4 = print("What is ", first_number[1], " * " , first_number[7], "?")
    print("a) 1,080")
    print("b) 1,620")
    print("c) 1,095")
    print("d) 2,620")
    answer1 = input("Choice the correct letter: ").lower()
    if answer1 =="b":
         score = score+1
         print("That is correct! Your score is now:",score)
    else:
        print("Sorry that is incorrect!")
        print("Your score is still:",score)

    Question5 = print("What is ", first_number[2], " * " , second_number[1], "?")
    print("a) 108")
    print("b) 98")
    print("c) 80")
    print("d) 99")
    answer1 = input("Choice the correct letter: ").lower()
    if answer1 =="a":
         score = score+1
         print("That is correct! Your score is now:",score)
    else:
        print("Sorry that is incorrect!")
        print("Your score is still:",score)
    if score == 5:
        print("Your a Genius!")
    elif 2 < score <= 4:
        print("Better luck next time")
    elif 0 <= score < 3:
        print("Maybe Study more math!")
    else:
        print("Invalid Score!")
    
    
    
    
MathQuiz()
