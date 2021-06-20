import random

# import time

alea = random.randint(1, 3)  # Nombre aléatoire entre 1 et 100


def almost(answer):
    if answer < alea:
        print("C'est plus")
    else:
        print("C'est moins")


def tirage_easy():
    answer = 0
    coup = 0
    while answer != alea:
        answer = int(input())
        if answer - 50 > alea or answer + 50 < alea:
            print("Vous êtes très loin")
            almost(answer)
            coup += 1
        elif answer - 25 > alea or answer + 25 < alea:
            print("Vous êtes assez loin")
            almost(answer)
            coup += 1
        elif answer - 15 > alea or answer + 15 < alea:
            print("Vous êtes plutôt proche")
            almost(answer)
            coup += 1
        elif answer - 10 > alea or answer + 10 < alea:
            print("Vous êtes proche")
            almost(answer)
            coup += 1
        elif answer - 5 > alea or answer + 5 < alea:
            print("Vous êtes très proche")
            almost(answer)
            coup += 1
        elif answer - 3 > alea or answer + 3 < alea:
            print("Vous brûlez")
            almost(answer)
            coup += 1
        elif answer - 1 > alea or answer + 1 < alea:
            print("Vous êtes à un cheveu !")
            almost(answer)
            coup += 1
        else:
            print(f"Vous avez trouvé ! Vous avez utilisé {coup + 1} coups pour trouver")
            break


def tirage_ascendant(answer, coup):
    while answer != alea:
        answer = int(input())
        if answer - 50 > alea or answer + 50 < alea:
            print("Vous êtes très loin")
            almost(answer)
            coup -= 1
        elif answer - 25 > alea or answer + 25 < alea:
            print("Vous êtes assez loin")
            almost(answer)
            coup -= 1
        elif answer - 15 > alea or answer + 15 < alea:
            print("Vous êtes plutôt proche")
            almost(answer)
            coup -= 1
        elif answer - 10 > alea or answer + 10 < alea:
            print("Vous êtes proche")
            almost(answer)
            coup -= 1
        elif answer - 5 > alea or answer + 5 < alea:
            print("Vous êtes très proche")
            almost(answer)
            coup -= 1
        elif answer - 3 > alea or answer + 3 < alea:
            print("Vous brûlez")
            almost(answer)
            coup -= 1
        elif answer - 1 > alea or answer + 1 < alea:
            print("Vous êtes à un cheveu !")
            almost(answer)
            coup -= 1
        elif coup == 0:
            print("Perdu, trop de tentatives")
            break
        else:
            print(f"Vous avez trouvé ! Il vous restait {coup - 1} coups pour trouver")
            break


def tirage_normal():
    answer = 0
    coup = 15
    tirage_ascendant(answer, coup)


def tirage_hard():
    answer = 0
    coup = 5
    tirage_ascendant(answer, coup)


menu = """Menu
Pour sortir, tapez exit
Pour jouer en mode facile, tapez easy
Pour jouer en mode normal, tapez normal
Pour jouer en mode difficile, tapez hard
Que désirez-vous ?"""


def game():
    choice = 0
    while choice != "exit":
        print(menu)
        choice = input()
        if choice == "easy":
            print("Vous possédez un nombre de coups illimité")
            tirage_easy()
        elif choice == "normal":
            print("Vous possédez 15 coups")
            tirage_normal()
        elif choice == "hard":
            print("Vous possédez 5 coups")
            tirage_hard()
        elif choice == "exit":
            break
        else:
            print("Choix non valide")
        while choice != "oui" or choice != "non":
            print("""Recommencer ?
            oui
            non""")
            choice = input()
            if choice == "oui":
                game()
            elif choice == "non":
                break
            else:
                print("Choix non valide")
        break

game()
