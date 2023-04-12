import string

alphabet = string.ascii_uppercase

Rotors = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'VZBRGITYUPSDNHLXQWMJQOFECK']

Num_Rotors = []
for i in range(len(Rotors)):
    liste = []
    for lettre in Rotors[i]:
        liste.append(alphabet.index(lettre))
    Num_Rotors += liste

Reflecteurs = ['YRUHQSLDPXNGOKMIEBFZCWVJAT', 'RDOBJNTKVEHMLFCWZAXGYIPSUQ']

Num_Reflecteurs = []
for j in range(len(Reflecteurs)):
    liste = []
    for lettre in Reflecteurs[j]:
        liste.append(alphabet.index(lettre))
    Num_Reflecteurs += liste


def Choix_Rotors():
    print('Choisissez 3 Rotors entre: 1, 2, 3, 4 et 5')
    Rotor = ['1', '2', '3', '4', '5']
    Rotor1 = input('Rotor n°1 : ')
    while Rotor1 not in Rotor:
        print('Il faut entrer un entier entre:', Rotor)
        Rotor1 = input('Rotor n°1 : ')
    Rotor.remove(Rotor1)
    Rotor1 = int(Rotor1)
    Rotor2 = input('Rotor n°2 : ')
    while Rotor2 not in Rotor:
        print('Il faut entrer un entier entre:', Rotor)
        Rotor2 = input('Rotor n°2 : ')
    Rotor.remove(Rotor2)
    Rotor2 = int(Rotor2)
    Rotor3 = input('Rotor n°3 : ')
    while Rotor3 not in Rotor:
        print('Il faut entrer un entier entre:', Rotor)
        Rotor3 = input('Rotor n°3 : ')
    Rotor.remove(Rotor3)
    Rotor3 = int(Rotor3)
    return Rotor1 - 1, Rotor2 - 1, Rotor3 - 1
    
    
def Choix_Reflecteur():
    print('Choisissez 1 Réflecteur entre: 1 et 2')
    Reflecteur = ['1', '2']
    Reflecteur1 = input('Reflecteur : ')
    while Reflecteur1 not in Reflecteur:
        print('Il faut entrer un entier entre:', Reflecteur)
        Reflecteur1 = input('Reflecteur : ')
    Reflecteur1 = int(Reflecteur1)
    return Reflecteur1 - 1


def Paire_Connexion():
    run = False
    while run == False:
        lettre_use = ''
        connexion = input('Entrez 6 paires de lettres (sans espaces): ')
        if len(connexion) != 12:
            print('Il faut entrer 6 paires de lettres (12 lettres différentes) parmis:', alphabet)
            continue
        connexion = connexion.upper()
        for i in range(len(connexion)):
            if connexion[i] not in alphabet or connexion[i] in lettre_use:
                print('Il faut entrer 6 paires de lettres (12 lettres différentes) parmis:', alphabet)
                break
            if connexion[-1] == connexion[i] and i == len(connexion) - 1:
                run = True
            lettre_use += connexion[i]
    return connexion


def Pos_Rotor():
    print('Poistion initial des Rotors:')
    Rotor1 = input('Entrez la lettre initial du Rotor n°1: ')
    while Rotor1.upper() not in alphabet:
        print('Il faut entrer une lettre parmis:', alphabet)
        Rotor1 = input('Entrez la lettre initial du Rotor n°1: ')
    Rotor1.upper()
    Rotor2 = input('Entrez la lettre initial du Rotor n°2: ')
    while Rotor2.upper() not in alphabet:
        print('Il faut entrer une lettre parmis:', alphabet)
        Rotor2 = input('Entrez la lettre initial du Rotor n°2: ')
    Rotor2.upper()
    Rotor3 = input('Entrez la lettre initial du Rotor n°3: ')
    while Rotor3.upper() not in alphabet:
        print('Il faut entrer une lettre parmis:', alphabet)
        Rotor3 = input('Entrez la lettre initial du Rotor n°3: ')
    Rotor3.upper()
    return Rotor1, Rotor2, Rotor3


def Decalage_Rotor(rotor):
    rotor = rotor[1:] + rotor[0]
    return rotor


def Initial_Rotor(rotor, lettre):
    pos = alphabet.index(lettre)
    rotor = rotor[pos:] + rotor[:pos]
    return rotor


def Lettre_Apres_Connexion(lettre, connexion):
    indice = connexion.index(lettre)
    if indice % 2 == 1:
        return connexion[indice - 1]
    else:
        return connexion[indice + 1]


def Lettre_Apres_Rotor(lettre, Rotor, Rotors, indice):
    new_alphabet = alphabet[Rotors.index(Rotor[0]):] + alphabet[:Rotors.index(Rotor[0])]
    lettre = Rotor[indice]
    indice = new_alphabet.index(lettre)
    return lettre, indice


def Lettre_Apres_Rotor_inverse(lettre, Rotor, Rotors, indice):
    new_alphabet = alphabet[Rotors.index(Rotor[0]):] + alphabet[:Rotors.index(Rotor[0])]
    lettre = new_alphabet[indice]
    indice = Rotor.index(lettre)
    return lettre, indice


def Lettre_Apres_Reflecteur(lettre, Reflecteur, indice):
    indice = alphabet.index(Reflecteur[indice])
    lettre = Reflecteur[indice]
    return lettre, indice


def Message():
    message = input('Entrez le message à coder ou à décoder: ')
    return message

def Chiffrer():
    Rotor = Choix_Rotors()
    Rotor1 = Rotors[Rotor[0]]
    Rotor2 = Rotors[Rotor[1]]
    Rotor3 = Rotors[Rotor[2]]
    position_Rotor = Pos_Rotor()
    Pos_Rotor1 = position_Rotor[0]
    Pos_Rotor2 = position_Rotor[1]
    Pos_Rotor3 = position_Rotor[2]
    Rotor1 = Initial_Rotor(Rotor1, Pos_Rotor1)
    Rotor2 = Initial_Rotor(Rotor2, Pos_Rotor2)
    Rotor3 = Initial_Rotor(Rotor3, Pos_Rotor3)
    Reflecteur = Choix_Reflecteur()
    Reflecteur1 = Reflecteurs[Reflecteur]
    Paire = Paire_Connexion()
    message = Message()
    res = ''
    for lettre in message:
        if lettre in Paire:
            lettre = Lettre_Apres_Connexion(lettre, Paire)
        Rotor1 = Decalage_Rotor(Rotor1)
        if Rotor1[0] == Pos_Rotor1:
            print(1)
            Rotor2 = Decalage_Rotor(Rotor2)
            if Rotor2[0] == Pos_Rotor2:
                Rotor3 = Decalage_Rotor(Rotor3)
        lettre, indice = Lettre_Apres_Rotor(lettre, Rotor1, Rotors[Rotor[0]], alphabet.index(lettre))[0], Lettre_Apres_Rotor(lettre, Rotor1, Rotors[Rotor[0]], alphabet.index(lettre))[1]
        lettre, indice = Lettre_Apres_Rotor(lettre, Rotor2, Rotors[Rotor[1]], indice)[0], Lettre_Apres_Rotor(lettre, Rotor2, Rotors[Rotor[1]], indice)[1]
        lettre, indice = Lettre_Apres_Rotor(lettre, Rotor3, Rotors[Rotor[2]], indice)[0], Lettre_Apres_Rotor(lettre, Rotor3, Rotors[Rotor[2]], indice)[1]
        lettre, indice = Lettre_Apres_Reflecteur(lettre, Reflecteur1 , indice)[0], Lettre_Apres_Reflecteur(lettre, Reflecteur1 , indice)[1]
        lettre, indice = Lettre_Apres_Rotor_inverse(lettre, Rotor3, Rotors[Rotor[2]], indice)[0], Lettre_Apres_Rotor_inverse(lettre, Rotor3, Rotors[Rotor[2]], indice)[1]
        lettre, indice = Lettre_Apres_Rotor_inverse(lettre, Rotor2, Rotors[Rotor[1]], indice)[0], Lettre_Apres_Rotor_inverse(lettre, Rotor2, Rotors[Rotor[1]], indice)[1]
        lettre, indice = Lettre_Apres_Rotor_inverse(lettre, Rotor1, Rotors[Rotor[0]], indice)[0], Lettre_Apres_Rotor_inverse(lettre, Rotor1, Rotors[Rotor[0]], indice)[1]
        lettre = alphabet[indice]
        if lettre in Paire:
            lettre = Lettre_Apres_Connexion(lettre, Paire)
        res += lettre
    return res


# print(Reflecteurs, Num_Reflecteurs)
# print(Rotors, Num_Rotors)
# print(Choix_Rotors())
# print(Choix_Reflecteur())
# print(Paire_Connexion())
# print(Pos_Rotor())
# print(Decalage_Rotor(Rotors[0]))
# print(Initial_Rotor(Rotors[0], "G"))
# print(Lettre_Apres_Connexion("U", "FLGDQVZNTOWY"))
# print(Lettre_Apres_Rotor("F", Rotors[0]))
# print(Lettre_Apres_Reflecteur("S", Reflecteurs[0]))
print(Chiffrer())

