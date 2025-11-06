def askQuestion(question, answer):
    your_response = input(question + '\n').lower()
    
    if your_response == answer.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False

def printFinalScore(score):
    if score == 5:
        print("Congratulations! You got a perfect score!")
    elif score >= 3:
        print("Good job! You scored", score, "out of 5.")
    else:
        print("Better luck next time. You scored", score, "out of 5.")

def main():
    print("Welcome my Math Quiz!")
    
    questionList = ["What is 100 / 5?", "What is 70 / 5?", "What is 35 * 11?", "What is 90 * 18?", "What is 36 * 3?"]
    
    answerList = ["20", "14", "385", "1,620", "108"]
    
    score = 0
    
    for i in range(len(questionList)):
        if askQuestion(questionList[i], answerList[i]):
            score += 1
    
    printFinalScore(score)
    print("Thanks for playing!")

main()
