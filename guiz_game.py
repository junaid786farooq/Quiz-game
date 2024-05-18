# Programe that check the answer of user.

print("Welcom to mu computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")

quiz = {
    "question1" : {
        "question" : "What does CPU stand for? ",
        "answer" : "central processing unit"
        },

    "question2" : {
        "question" : "What does GPU stand for? ",
        "answer" : "graphics processing unit"
        },

    "question3" : {
        "question" : "What does RAM stand for? ",
        "answer" : "random access memory"
        },

    "question4" : {
        "question" : "What does ROM stand for? ",
        "answer" : "read only memory"
        },

    "question5" : {
        "question" : "What does SSD stand for? ",
        "answer" : "solid state drive"
        },

    "question6" : {
        "question" : "What does HDD stand for? ",
        "answer" : "hard disk drive"
        },

    "question7" : {
        "question" : "What does USB stand for? ",
        "answer" : "universal serial bus"
        },

    "question8" : {
        "question" : "What does DVD stand for? ",
        "answer" : "digital video disc"
        },

    "question9" : {
        "question" : "What does DVR stand for? ",
        "answer" : "digital video recorder"
        },

    "question10" : {
        "question" : "What does PC stand for? ",
        "answer" : "personal computer"
        }  
    }

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer : ")

    if answer.lower() == value["answer"]:
        print("Correct")
        score += 1
        print("Your score is:", score )
    else:
        print("Wrong!")
        print("The answer is:", value["answer"])

print("You got " + str(score) + " out of 10 questions correctly.")
print("You percentage is : " + str((score / 10) * 100) + " %")