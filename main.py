import random

level_range = [100, 500, 1000]
level_guesses = [10, 7, 5]

def level():
    level = 0
    while level > 3 or level <=0:
        level = int(input("Ingrese el nivel a jugar (hay 3 niveles) "))
    return level

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
    

def game(level):
    number_to_guess = random.randint(0,level_range[level-1])
    print(number_to_guess)
    for i in range(level_guesses[level-1]):
        number = int(input(f"Intenta adivinar un numero entre 0 y {level_range[level-1]} " ))
        if(number_to_guess == number):
            print("Ganaste")
            if(level <= len(level_guesses)-1):
                print("Siguente nivel")
                game(level+1)
                break
            else:
                print("Ya no quedan más niveles")
                break
        else:
            clue(number_to_guess)
    
    

def main():
    level_to_play = level()
    game(level_to_play)

if __name__ == "__main__":
    main()
