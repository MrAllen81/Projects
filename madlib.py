#Chapter 2 Mad Libs Assignment
#Created by: Tyler Allen
#9/13/23
def madlibs():
    name = input("Enter your name")
    print("Welcome " + name + "," + " This program will create a wacky sentence based on the words you enter for each type of speech ")
    Noun = input("Enter a noun")
    Adjective = input("Enter an adjective")
    verb = input("Enter a verb")
    place = input("Enter your favorite place")
    noun = input("Enter another noun")
    print("Your " + Adjective  + " " + noun + " and " + Noun + " are going to " + verb + " at " + place)
    print("Thank you for playing " + name)
    play2 = input("Do you want to play again? ")

    if play2 == "Yes" or "yes":
        madlibs()
    else:
     print("Thank you for playing")
     input("press <enter> key to quit")
    
madlibs()
