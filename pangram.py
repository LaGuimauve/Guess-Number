import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Initialisation de l'alphabet


def pangram(sentence):
    for letter in alphabet:  # Pour chaque lettre présente dans l'alphabet
        if letter not in sentence.lower():  # Si jamais une lettre (toutes mises en minuscule
                                            # parmi toutes celles de l'alphabet n'est pas dans la phrase
            return print("Ce n'est pas un pangramme")  # Alors ce n'est pas un pangramme
    return print("C'est un pangramme")  # Sinon, c'est un pangramme
