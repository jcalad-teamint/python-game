import random

def es_primo(n):
    for i in range(2,int(n/2)):
        if (n%i) == 0:
            return False
    return True

def primo(n):
    print("Es primo") if es_primo(n) else print("No es primo")

def multiplo_cinco(n):
    if (n%5) == 0:
        print("Es multiplo de cinco")
    else: 
        print("No es multiplo de cinco")

def multiplo_tres(n):
    if (n%3) == 0:
        print("Es multiplo de tres")
    else: 
        print("No es multiplo de tres")

def multiplo_dos(n):
    if (n%2) == 0:
        print("Es multiplo de dos")
    else: 
        print("No es multiplo de dos")

def par(n):
    if (n%2) == 0:
        print("Es numero par")
    else: 
        print("Es numero impar")

funtions = {0: par, 1: primo, 2: multiplo_cinco, 3: multiplo_tres, 4: multiplo_dos}

def clue(n):
    clue_number = random.randint(0,4)
    funtions[clue_number](n)