from math import *


def square(number):
    print("Il", "n'est pas" if sqrt(number) % 1 == 0 else "est", "carré")


def next_square(number):
    carre = int(sqrt(number)+1)
    print(carre**2 if sqrt(number) % 1 == 0 else "Ce n'est pas un carré")


next_square(154)
next_square(256)
