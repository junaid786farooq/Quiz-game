# Programe that check the answer of user.

print("Welcom to mu computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
if answer.lower() == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does DVD stand for? ")
if answer.lower() == "digital video disc":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%")