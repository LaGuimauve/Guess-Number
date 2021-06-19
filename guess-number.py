import random

# import time

alea = random.randint(1, 5)  # Nombre aléatoire entre 1 et 100


def tirage():
    answer = 0
    coup = 0
    while answer != alea:
        answer = int(input("Entrez un chiffre"))
        if answer > alea:
            print("Choisissez plus petit")
            coup += 1
        elif answer < alea:
            print("Choisissez plus grand")
            coup += 1
        else:
            print(f"Vous avez trouvé ! Vous avez mis {coup + 1} coups pour trouver")


while choice != "exit":


tirage()
