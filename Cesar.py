import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import string

alphabet = string.ascii_lowercase

def chiffrer(chaine : str, decalage : int) -> str:
    """Cette fonction renvoie la chaine chiffrer en fonction du décalage

    Parameter
    ---------
    chaine : string
                chaine à chiffrer
    decalage : int
                nombre de décalage sur l'alphabet
    
    Returns
    -------
    string
        chaine chiffrer

    Examples
    --------
    >>> chiffrer("hello world", 3)
    'khoor zruog'
    >>> chiffrer("zebre", 3)
    'cheuh'
    >>> chiffrer("bonjour", 3)
    'erqmrxu'
    """
    res = ''
    for i in range(len(chaine)):   # Parcours lettre par lettre de la chaine a chiffrer
        if chaine[i] == ' ':   # Si il y a un espace mettre un espace  
            res += ' '
        else:
            for j in range(len(alphabet)):   # Parcours de l'alphabet lettre par lettre
                if alphabet[j] == chaine[i]:   # Si la lettre de la chaine est = à la lettre de l'alphabet, on continue
                    total = j + decalage  # total = la somme de la position de la lettre de la chaine dans l'alphabet et du décalage
                    total = total % len(alphabet)   # cas si total > 26
                    res += alphabet[total]   # On ajoute la lettre chiffrer
    return res


def dechiffrer_cesar(chaine : str, decalage : int) -> str:
    """Cette fonction renvoie la chaine déchiffrer en fonction du décalage

    Parameter
    ---------
    chaine : string
                chaine à déchiffrer
    decalage : int
                nombre de décalage sur l'alphabet
    
    Returns
    -------
    string
        chaine déchiffrer

    Examples
    --------
    >>> dechiffrer_cesar("khoor zruog", 3)
    'hello world'
    >>> dechiffrer_cesar("cheuh", 3)
    'zebre'
    >>> dechiffrer_cesar("erqmrxu", 3)
    'bonjour'
    """
    res = ''
    for i in range(len(chaine)):   # Parcours lettre par lettre de la chaine a déchiffrer
        if chaine[i] == ' ':   # Si il y a un espace mettre un espace  
            res += ' '
        else:
            for j in range(len(alphabet)):   # Parcours de l'alphabet lettre par lettre
                if alphabet[j] == chaine[i]:   # Si la lettre de la chaine est = à la lettre de l'alphabet, on continue
                    total = j - decalage   # total = la soustraction de la position de la lettre de la chaine dans l'alphabet et du décalage
                    total = total % len(alphabet)   # cas si total < 0
                    res += alphabet[total]   # On ajoute la lettre dechiffrer
    return res


def frequence_apparitions(chaine):
    """Cette fonction renvoie une liste contenant la fréquence d'apparitions dans la chaine par ordre alphabetique

    Parameter
    ---------
    chaine : string
                chaine à décrypter
                
    Returns
    -------
    list
        liste de nombre

    Examples
    --------
    >>> frequence_apparitions('mh shxa wh yrlu')
    [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]
    """
    apparitions = [0] * 26   # Création d'une liste de 0 de longueur 26
    chaine = chaine.lower()   # On met la chaine en minuscule
    for i in range(len(chaine)):   # Parcours lettre par lettre de la chaine
        if chaine[i] not in alphabet:  # Si c'est un espace ou autre caractère spéciaux on passe à l'itération d'après
            continue
        else:
            apparitions[alphabet.index(chaine[i])] = apparitions[alphabet.index(chaine[i])] + 1   # On ajoute 1 à la position de la lettre de la chaine dans l'alphabet
    return apparitions


def cherche_decalage(chaine):
    """Cette fonction renvoie le decalage effectuer sur la chaine

    Parameter
    ---------
    chaine : string
                chaine à décrypter
                
    Returns
    -------
    int
        decalage

    Examples
    --------
    >>> cherche_decalage('mh shxa wh yrlu')
    3
    """
    francais = [942, 102, 264, 339, 1587, 95, 104, 77, 841, 89, 0, 534, 324, 715, 514, 286, 106, 646, 790, 726, 624, 215, 0, 30, 24, 32]   # Liste d'apparitions des lettres en moyenne de l'alphabet français
    liste = [0] * 26   # Création d'une liste de 0 de longueur 26
    for i in range(len(francais)):   # Parcours de la liste francais iteration par iteration
        for j in range(26):   # Boucle de 26 iterations
            frequences = frequence_apparitions(dechiffrer_cesar(chaine, j))   # On récupère la fréquence d'apparitions de la chaine déchiffrer avec comme décalage j
            liste[i] += frequences[i] * francais[j]   # On ajoute la fréquence de i * la liste francais de i
    return liste.index(max(liste))   # On retourne l'indice du nombre maximum contenue dans la liste


def diagramme_baton(chaine):
    """Cette fonction renvoie la fréquence d'apparitions des lettre sous forme de diagramme

    Parameter
    ---------
    chaine : string
                chaine à décrypter

    Returns
    -------
    None
    """
    categories = []
    valeur = []
    liste = frequence_apparitions(chaine)   # On creer une variable qui récupère le résultat de la fonction frequence_apparitions()
    for i in range(len(liste)):   # Parcours de la liste
        categories += alphabet[i]   # On ajoute à categories les la valeur de l'indice dans l'alphabet
        valeur.append(liste[i])   # On ajoute à valeur les valeur de la liste pour l'indice i
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')   # Cf matplotlib doc
    ax.set_title("Fréquence des lettres dans la chaine de caractères")   # On lui donne un titre
    ax.set_xlabel('Lettres')   # On donne un nom à l'axe des abscisse
    ax.set_ylabel("Nombres d'apparitions")   # On donne un nom à l'axe des ordonné
    plt.bar(categories, valeur) ; plt.show()   # On affiche le diagramme


def decrypter(chaine):
    """Cette fonction renvoie la chaine déchiffrer sans connaitre le décalage

    Parameter
    ---------
    chaine : string
                chaine à décrypter

    Returns
    -------
    string
        chaine décrypter

    Examples
    --------
    >>> decrypter('mh shxa wh yrlu')
    'je peux te voir'
    """
    decalage = cherche_decalage(chaine)   # On récupère le décalage grâce à la fonction cherche_decalage
    return dechiffrer_cesar(chaine, decalage)   # On retourne la fonction dechiffrer_cesar avec comme paramètres : la chaine, le décalage


chaine = "uizqmIumtqm aqvabittm idmk ai umzm icxzma lm ai lmuq awmcz ti zmqvm Uizqm I kmbbm mxwycm tm owcdmzvmumvb jzmaqtqmv zmncam mv mnnmb lm zmkwvviqbzm tmvnivb kwuum umujzm i xizb mvbqmzm lm ti niuqttm quxmzqitm Vq mttm vq ai umzm tquxmzibzqkm lwciqzqmzm vm zmkwqdmvb lwvk ickcvm xmvaqwv lm ti xizb lm tMbib jzmaqtqmv Kmab amctmumvb idmk ti nqv lm ti zmomvkm jzmaqtqmvvm mb tmizzqdmm ic xwcdwqz lc lmuq"

# a = chiffrer("je peux te voir", 3)
# print(a)
# b = dechiffrer_cesar(chaine, 8)
# print(b)
# c = frequence_apparitions('mh shxa wh yrlu')
# print(c)
# diagramme_baton(chaine)
# e = decrypter(chaine)
# print(cherche_decalage('mh shxa wh yrlu'))