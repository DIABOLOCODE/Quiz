
from time import sleep


print("Bienvenue dans le quiz de Côme!")
sleep(1)
point = 0
start = input("Veux-tu commencer (y/n)")

if start.lower() == "y":
    print("Alors commencons!")
else:
    quit()
sleep(1)
#Q1
answer = input("Premiere question: comment s'apelle le createur de ce quiz?")
if answer == "Côme":
    print("Bonne reponse!")
    point = point + 1
else:
    print("mauvaise réponse...")
sleep(1)
#Q2
answer = input("signification de GPU?")
if answer.lower() == "graphic processing unit":
    print("Bonne reponse!")
    point = point + 1
else:
    print("mauvaise réponse...")
sleep(1)
#Q3
answer = input("signification de RAM?")
if answer == "random access memory":
    print("Bonne reponse!")
    point = point + 1
else:
    print("mauvaise réponse...")
sleep(1)
#Q4
answer = input("signification de CPU")
if answer == "central processing unit":
    print("Bonne reponse!")
    point = point + 1
else:
    print("mauvaise réponse...")
sleep(1)
print("C'est la fin du quiz: vous avez eu " + str(point) + " bonne réponse sur 4")
if point == 4:
    print("Felicitation! Aucune erreure :)")