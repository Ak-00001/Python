# Python quiz game


questions = ("a",
             "b",
             "c",
             "d",
             "e")

options = (("A","B","C","D"),
           ("A","B","C","D"),
           ("A","B","C","D"),
           ("A","B","C","D"),
           ("A","B","C","D"))


answers = ("C","D","A","B","A")
guesses = []
score= 0
questions_num = 0

for question in questions:
    print("----------------------")
    print(questions)
    for option in options[questions_num]:
        print(option)


    guess = input("Enter (A,B,C,D)").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
    questions_num+=1

