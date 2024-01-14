import os
from key import KeyError
try:
    nbr1 = int(input("Entrer le nombre 1: "))
    nbr2 = int(input("Entrer le nombre 2: "))
    opera = input("un opérateur (+, -, *, /): ")
    if opera == '+':
        print(nbr1+nbr2)
    elif opera == '-':
        print(nbr1-nbr2)
    elif opera == '*':
        print(nbr1*nbr2)
    elif opera == '/':
        print(nbr1/nbr2)
    else:
        raise ValueError
    chaine = input("Entrer un nombre: ")
    convert = int(chaine)
    file = input("Entrer nom de fishier: ")

    if os.path.exists("c://"+file):
        print("file found")

    else:
        raise FileNotFoundError
    dictonaire = {'cle1': 3, 'cle2': "hello", 'cle3': 777}
    key = input("Entrer une cle: ")
    if key in dictonaire.keys():
        print("key found: ", key)
    else:
        raise KeyError()
    list4 = [1, 2, 4, 5]
    index = int(input("Entrer l'index: "))
    print("le nombre dans la list est: ", list4[index])

except ValueError as wrongType:
    print("you typed the wrong type")
except ZeroDivisionError as dividedByZero:
    print("You can't devide by 0 (zero)")
except FileNotFoundError as wrongfile:
    print("the file does not exist")
except IndexError as ind:
    print("l'index est hors des limites de la liste")
except Exception as key:
    print(key)
