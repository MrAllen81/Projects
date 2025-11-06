

print("Welcome to Dungeons and Deans")
print("Your goal is to earn 120 credits and defeat the final boss")

global playername
global playermajor
playername =  input("Enter your name")
playermajor = input("Enter your major")
import time
def start():
    print ("Welcome to Marist,", playername)
    print("Are you ready to play Dungeons and Deans?")
    Answer = input("yes or no")
    if Answer == "yes" or  Answer == "Yes":
        print ("Woohoo")
    elif Answer == "no" or "No":
        print ("Too bad the game is starting, you are about to enter the Marist Dungeon")
    #Initiate Countdown
    print("3")
    #delays time for 1.5 seconds
    time.sleep(1.5)
    print ("2")
    time.sleep(1.5)
    print ("1")
    time.sleep(1.5)
import random
start()

def level1():
    global attack
    global defense
    global playerclass
    global credits
    global roll2
    classes = ["hunter”, “barbarian”, “healer”, “wizard”, “rogue”, “warlock"]
    print(classes) 
    playerclass = input("Choose a class").lower()
    attack = 0
    defense = 0
    if playerclass == "hunter":
        print("You are a hunter, you’re job is to take down everyone who gets in your way")
        attack = 17
        defense =  15
        print ("attack = 17")
        print("defense equals 15")
    elif playerclass == "barbarian":
        print ("You are a barbarian, you are a party animal have as much fun as possible")
        attack = 16
        defense = 14
        print("attack = 16")
        print("defense = 14")
    elif playerclass == "healer":
        print("You are a healer, you’re job is to help your classmates")
        attack = 13
        defense = 18
        print("attack = 13")
        print("defense = 18")
    elif playerclass == "wizard":
        print("You are a wizard, you can use magic to help you graduate faster, but magic as always, comes at a cost")
        attack = 14
        defense = 12
        print("attack = 14")
        print("defense =12")
    elif playerclass == "rogue":
        print("You are a rogue, you can slip by with assignments and studying but careful there are some evil professors out there")
        attack = 15
        defense = 13
        print("attack = 15")
        print("defense = 13")
    elif playerclass == "warlock":
        print("You are a warlock. Your job is to lead our class to the promise land aka graduation")
        attack = 18
        defense = 16
        print("attack = 18")
        print("defense = 16")
    else:
        print("Try Again")
        level1()
    print("Welcome to Freshman year!")
    time.sleep(1)
    print("Here is your first question!")
    print("You have 3 attempts to answer right and you have a chance to earn credits")
    credits = 0
    attempts = 3
    while attempts >=1:
        Question1 = print("What is 35 x 11?")
        print("a) 380")
        print("b) 375")
        print("c) 355")
        print("d) 385")
        answer1 = input("Choose the correct letter. ").lower()
        if answer1 == "d":
            print("That is correct!")
            credits = credits + 15
            print("Congrats you earned", credits, "credits")
            print("You now have", credits, "credits")
            attempts = 0
        elif answer1 == "skip":
            attempts = 0
            print("You don't gain or lose any credits.")
        elif answer1 == "a" or "b" or "c":
            print("Sorry that is incorrect! Try Again!")
            print("Type 'skip' if you want to skip to next question")
            attempts = attempts - 1
            print("You have", attempts, "attempts left")
        if attempts < 1:
            print("You run into your old high school bully on the first day of school,what do you do?")
            print("1 = Attack and 2 = Run")
            Encounter1 = input("Would you like to attack or run?")
            if Encounter1 == "1":
                print("You attack the high school bully, but the bully has some new defenses too")
                roll = random.randint(1,18)
                if roll < attack:
                    print("Your bully had a defense of", roll)
                    print("However you got revenge on the bully")
                    credits = credits + 5
                elif roll > attack:
                    print("the bully won yet again with a great defense of", roll)
                    print("You gained no credits, you still have", credits, "credits")
            elif Encounter1 == "2":
                print("You try to run away from the bully, but do you get away")
                roll = random.randint(1,18)
                if roll < defense:
                    print("Your defense was better than their attack of", roll)
                    print("You got away, phew....")
                    credits = credits + 5
                elif roll > defense:
                    print("Your defense did not stand a chance against their attack of", roll)
                    print("You did not get away, the bully caught up and threatened you")
                    print("You gained no credits, you still have", credits, "credits")
            time.sleep(1)
            print("After you meet your high school bully, you have successfully gotten through 1 semester")
            print("Onto semester 2!")
            print("Here is the next question")
            attempts2 = 3
            while attempts2 >=1:
                Question2 = print("What is the definition of eschew?")
                print("a) place of origin")
                print("b) to chew loudly")
                print("c) to avoid deliberately")
                print("d) to have not like the taste of something")
                answer2 = input("Choose the correct letter, but you have 3 attempts").lower()
                if answer2 == "c":
                      print("That is correct!")
                      credits = credits + 15
                      print("Congrats you earned 15 credits")
                      attempts2 = 0
                elif answer2 == "skip":
                     attempts2 = 0
                     if playerlcass == rogue:
                         credits = credits + 3
                         print("You earned 3 credits for being a rogue")
                         print("Because you are a rogue, you can skip questions and still earn credits but it can also work the opposite if you get caught skipping")
                elif answer2 == "a" or "b" or "d":
                    print("Sorry that is incorrect! Try Again")
                    credits = credits - 5
                    print("Type 'skip' to skip the next scenario")
                    attempts2 = attempts2 - 1
                    print("You now have", attempts2, "attempts left")
                if attempts2 < 1:
                    time.sleep(1)
                    print("You stumble upon a mysterious chest while walking to class do you open it or ignore it?")
                    print("1 = open and 2 = ignore")
            Encounter2 = input("open or ignore")
            if Encounter2 == "1":
                print("You decided to open the chest, lets roll to see what you got!")
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                roll2 = random.randint(1,10)
                print("You rolled a", roll2)
                if roll2>= 5:
                    print("You earned free textbook, you can now narrow the next question down to 2 answers for free")
                elif roll2< 5:
                    print("The chest was decoy, there was nothing in there")
            elif Encounter2 == "2":
                print("You ignored the chest, you missed out on free textbook which could have helped on the next question, oh well.")
def level2():
    global credits
    global attack
    global defense
    global playerclass
    print("Welcome to level 2, you have officially entered sophmore year")
    time.sleep(1)
    print("Here is your second question!")
    attempts3 = 3
    while attempts3 >=1:
        Question3 = print("Where is Babylon remain located?")
        if roll2 >= 5:
            print("Remember you have that textbook, and you narrowed the question to 2 answers")
            print("However if you answer incorrectly, you lose double the credits")
            print("a) Syria")
            print("b) Iraq")
            answer3 = input("Choose the correct letter").lower()
            if answer3 == "a":
                print("That is incorrect!")
                credits = credits - 30
                print("Oof, you lost 30 credits")
                print("You now have", credits, "credits")
                attempts3 = 0
            elif answer3 == "b":
                print("That is correct!")
                credits = credits + 15
                print("Congrats you earned 15 credits")
                print("You now have", credits, "credits")
                attempts3 = 0
        elif roll2 < 5:
            print("a) Syria")
            print("b) Iraq")
            print("c) Iran")
            print("d) Turkey")
            answer3 = input("Choose the correct letter").lower()
            if answer3 == "b":
                print("That is correct!")
                credits = credits + 15
                print("Congrats you earned 15 credits")
                attempts3 = 0
            elif answer3 == "skip":
                print("You decided to skip, you don't earn or lose any credits")
                attempts3 = 0
            elif answer3 == "a" or "c" or "d":
                print("That is incorrect! Try Again!")
                print("Enter 'skip' to skip to the next scenario")
                credits = credits - 2
                attempts3 = attempts3 - 1
                print("You now have", attempts3, "attempts left")
        if attempts3 < 1:
            print("Your'e housemates decide to throw a halloween party")
            print("Some drunk idiot is wielding a weapon, do you attack or run?")
            print("1 = attack and 2 = run")
            Encounter3 = input("Attack or Run?")
            if Encounter3 == "1":
                print("You decided to attack the drunk idiot, good luck")
                roll3 = random.randint(1,18)
                if roll3 < attack:
                    print("The idiot was super drunk and had a defense of", roll3)
                    print("You were easily able to overtake this guy")
                    print("You saved the day, Kevin Weinman decided to give you 5 credits")
                    credits = credits + 5
                elif roll3 > attack:
                    print("The idiot wasn't drunk enough to be easily defeated, you lost cause he had a defense of", roll3, "vs your attack of", attack)
                    credits = credits - 5
                    print("You lost 5 credits")
            elif Encounter3 == "2":
                print("You decided to run but is the guy fast enough to catch you?")
                roll3 = random.randint(1,18)
                if roll3 < defense:
                    print("You got away cause the idiot had an attack of", roll3)
                    credits = credits + 5
                elif roll3 > defense:
                    print("You did not get away, he caught up to you and knocked you out")
                    credits = credits - 5
            print("Here is your last question for sophmore year")
            attempts4 = 3
            while attempts4 >=1:
                Question4 = print("In what game was Luigi first available as a primary character?")
                print("a) Luigis Mansion")
                print("b) Super Mario Bros 2")
                print("c) Super Mario World 3D")
                print("d) Super Mario Galaxy")
                answer4 = input("Choose the correct letter.").lower()
                if answer4 == "b":
                    print("That is correct! You know your video games")
                    credits = credits + 15
                    print("You now have", credits, "credits")
                    attempts4 = 0
                elif answer4 == "skip":
                    attempts4 = 0
                    print("You don't gain or lose any credits.")
                elif answer4 == "a" or "b" or "c":
                    print("Sorry that is incorrect! Try Again!")
                    print("Type 'skip' if you want to skip to next question")
                    attempts4 = attempts4 - 1
                    credits = credits - 2
                    print("You have", attempts4, "attempts left")
                if attempts4 < 1:
                    print("Your role has earned some boosts for technically getting your associates degree(2 years of college)")
                    if playerclass == "hunter":
                        print("Since you chose Hunter you are only allowed to attack on the next turn but your attack increases")
                        attack = attack + 5
                    elif playerclass == "barbarian":
                        print("You get to narrow the next question to 3 options and your attack increase by a little")
                    elif playerclass == "healer":
                        print("Since you chose healer, you get to phone in a friend for the next question")
                    elif playerclass == "wizard":
                        print(" Since you chose Wizard you can earn extra credits for answering the question right")
                    elif playerclass == "rogue":
                        print("Since you chose rogue, you can get a hint on the next question")
                    elif playerclass == "warlock":
                        print("Since you chose Warlock, you are allowed to skip the next question and earn credits for doing so")
def level3():
    global credits
    global attack
    global defense
    global playerclass
    print("Welcome to Junior Year!")
    print("Now its time to start to preparing for internships")
    attempts5 = 3
    while attempts5 >=1:
        Question5 = print("An interviewer asks you how overcame a challenge. What is the best way to approach this question?")
        if playerclass == "hunter":
            print("a) Triangle Method")
            print("b) Pause Method")
            print("c) Just tell them about your best accomplishment")
            print("d) STAR Method")
            answer5 = input("Choose the correct letter.").lower()
            if answer5 == "d":
                print("That is correct! You know your video games")
                credits = credits + 15
                print("You now have", credits, "credits")
                attempts5 = 0
            elif answer5 == "skip":
                attempts5 = 0
                print("You don't gain or lose any credits.")
            elif answer5 == "a" or "b" or "c":
                print("Sorry that is incorrect! Try Again!")
                print("Type 'skip' if you want to skip to next question")
                attempts5 = attempts5 - 1
                credits = credits - 2
                print("You have", attempts5, "attempts left")
        elif playerclass == "rogue":
            print("Remember you get a hint on this question")
            print("a) Triangle Method")
            print("b) Pause Method")
            print("c) Just tell them about your best accomplishment")
            print("d) STAR Method")
            answer5 = input("Choose the correct letter.").lower()
            print(" Your hint is this method involves being vulnerable")
            if answer5 == "d":
                print("That is correct! You know your video games")
                credits = credits + 15
                print("You now have", credits, "credits")
                attempts5 = 0
            elif answer5 == "skip":
                attempts5 = 0
                print("You don't gain or lose any credits.")
            elif answer5 == "a" or "b" or "c":
                print("Sorry that is incorrect! Try Again!")
                print("Type 'skip' if you want to skip to next question")
                attempts5 = attempts5 - 1
                print("You have", attempts5, "attempts left")
                credits = credits - 2
        elif playerclass == "warlock":
            print("Remember you can skip to the next question so good luck with the next scenario")
            credits = credits + 15
            attempts5 = 0
        elif playerclass == "healer":
            print("Remember as a healer you can phone in a friend for this question")
            print("a) Triangle Method")
            print("b) Pause Method")
            print("c) Just tell them about your best accomplishment")
            print("d) STAR Method")
            answer5 = input("Choose the correct letter.").lower()
            if answer5 == "d":
                print("That is correct! You know your video games")
                credits = credits + 15
                print("You now have", credits, "credits")
                attempts5 = 0
            elif answer5 == "skip":
                attempts5 = 0
                print("You don't gain or lose any credits.")
            elif answer5 == "a" or "b" or "c":
                print("Sorry that is incorrect! Try Again!")
                print("Type 'skip' if you want to skip to next question")
                attempts5 = attempts5 - 1
                credits = credits - 2
                print("You have", attempts5, "attempts left")
        elif playerclass == "wizard":
            print("You are a wizard you can use your magic to earn extra credits")
            print("a) Triangle Method")
            print("b) Pause Method")
            print("c) Just tell them about your best accomplishment")
            print("d) STAR Method")
            answer5 = input("Choose the correct letter.").lower()
            if answer5 == "d":
                print("That is correct! You know your video games")
                credits = credits + 20
                print("You now have", credits, "credits")
                attempts5 = 0
            elif answer5 == "skip":
                attempts5 = 0
                print("You don't gain or lose any credits.")
            elif answer5 == "a" or "b" or "c":
                print("Sorry that is incorrect! Try Again!")
                print("Type 'skip' if you want to skip to next question")
                attempts5 = attempts5 - 1
                credits = credits - 2
                print("You have", attempts5, "attempts left")
        elif playerclass == "barbarian":
            print("You have narrowed this question down to 3 answers")
            print("a) Triangle Method")
            print("b) Just tell them about your best accomplishment")
            print("c) STAR Method")
            answer5 = input("Choose the correct letter.").lower()
            if answer5 == "c":
                print("That is correct! You know your video games")
                credits = credits + 15
                print("You now have", credits, "credits")
                attempts5 = 0
            elif answer5 == "skip":
                attempts5 = 0
                print("You don't gain or lose any credits.")
            elif answer5 == "a" or "b":
                print("Sorry that is incorrect! Try Again!")
                print("Type 'skip' if you want to skip to next question")
                attempts5 = attempts5 - 1
                credits = credits - 2
                print("You have", attempts5, "attempts left")
    if attempts5 < 1:
        print("Hopefully you took advantage of your powerups on that last question because now things will start to get tough")
        time.sleep(1)
        print("You are now running for a board position for your favorite club")
        print("However, your best friend is running against you are you still running or do you secede?")
        print("1 = Run and 2 = secede")
        Encounter5 = input("Run or Secede?")
        if Encounter5 == "1":
            print("You decide to still run, but you now have to roll to see if you win")
            roll5 = random.randint(10,18)
            if roll5 < attack:
                print("You won the election because you rolled a", roll5)
                print("Your friend is lowkey mad at you now")
                print("You gained 5 credits")
                credits = credits + 5
            if roll5 > attack:
                print("Sadly you did not win because you rolled a", roll5)
                print("You lost 3 credits for losing")
                credits = credits - 3
        elif Encounter5 == "2":
            print("You decided to secede, and nothing happens, altough your friend is very happy that you did this for them")
        print("Here is your last question for junior year")
        attempts6 = 3
        while attempts6 >=1:
            Question6 = print("How many elements are on the periodic table?")
            print("a) 118")
            print("b) 120")
            print("c) 206")
            print("d) 119")
            answer6 = input("Choose the correct letter.").lower()
            if answer6 == "a":
                print("That is correct! You know your periodic table")
                credits = credits + 15
                print("You now have", credits, "credits")
                attempts6 = 0
            elif answer6 == "skip":
                attempts6 = 0
                print("You don't gain or lose any credits.")
            elif answer6 == "b" or "c" or "d":
                print("Sorry that is incorrect! Try Again!")
                print("Type 'skip' if you want to skip to next question")
                attempts6 = attempts6 - 1
                credits = credits - 2
                print("You have", attempts6, "attempts left")
        if attempts6 < 1:
            print("You are finally done with Junior year!")
            print("One more year you got this")
def level4():
    global credits
    print("Welcome to Senior Year!")
    print("Kevin Weinman wants to ask a series of questions to see if you are ready to graduate")
    print("He is the final boss and final obstacle so there will be rapid fire questions in.....")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Oh Reminder, these are only 1 attempt questions")
    RFQuestion1 = print("When was Marist Founded?")
    print("a) 1919")
    print("b) 1929")
    print("c) 1939")
    print("d) 1949")
    RFanswer1 = input("Choose the correct letter.").lower()
    if RFanswer1 == "b":
        print("Nicely done, that is correct!")
        print("You earned 20 credits, keep it up")
        credits = credits + 20
    elif RFanswer1 == "a" or "c" or "d":
        print("That is incorrect, Kevin Weinman is disappointed")
        print("You lost 20 credits, do better next time")
        credits = credits - 20
    time.sleep(1)
    print("Here is question # 2")
    RFQuestion2 = print("Which African country was formerly known as Abyssinia?")
    print("a) Egypt")
    print("b) Nigeria")
    print("c) Ethiopia")
    print("d) Kenya")
    RFanswer2 = input("Choose the correct letter.").lower()
    if RFanswer2 == "c":
        print("Nicely done, that is correct!")
        print("You earned 20 credits, keep it up")
        credits = credits + 20
    elif RFanswer2 == "a" or "b" or "d":
        print("That is incorrect, Kevin Weinman is disappointed")
        print("You lost 20 credits, do better next time")
        credits = credits - 20
def main():
    global playername
    global playermajor
    level1()
    print("After Freshman year, you now have", credits, "credits")
    level2()
    print("After Sophmore year you now have ",credits, "credits")
    level3()
    print("After Junior year you now have", credits, "credits")
    level4()
    print("After Senior year you have", credits, "credits")
    if credits >= 120:
        print("Congrats", playername, " you  escaped, I mean graduated Marist with a degree in", playermajor)
        again = input("Would you like to play again?").lower()
        if again == "yes":
            main()
        elif again == "no":
            end = input("press 'enter' to quit")
    elif credits < 120:
        print("You failed to graduate, unfortunate!")
        again = input("Would you like to play again?").lower()
        if again == "yes":
            main()
        elif again == "no":
            end = input("press 'enter' to quit")
main()



    
