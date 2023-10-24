import random
from clues import clue
from files import check_name, write_csv

level_range = [100, 500, 1000]
level_guesses = [10, 7, 5]

def get_valid_number(maximum_number, prompt):
    is_valid_input = False
    while not is_valid_input:
        try:
            lower_bound = int(input(f"try to guess a number between 0 and {maximum_number} " ))
        except ValueError:
            print(f'Your input is not valid, is must be a numeric value.')
            continue

        if 0 <= lower_bound < maximum_number:
            is_valid_input = True
        else:
            print(f'Your input is not valid, it must be greater than {0} and less than {maximum_number}. Try again.')
    
    return lower_bound

def get_level():
    level = 0
    while level > 3 or level <=0:
        level = int(input("choose the level to play (there are 3 levels) "))
    return level


def get_user_input():
    user_name = input('Please write your name: ')
    level = get_level()
    return user_name, level


def execute_game(level, current_points):
    secret_number = random.randint(0,level_range[level-1])
    print(secret_number)
    points = current_points
    user_win = False
    points_per_level = level_guesses[level-1]*level
    for i in range(level_guesses[level-1]):
        user_guest = get_valid_number(level_range[level-1], "guess")
        if(secret_number == user_guest):
            points += points_per_level
            user_win = True
            print(f"You won level {level}!")
            if(level <= len(level_guesses)-1):
                print("Next Level")
                _, points = execute_game(level+1, points)
                break
            else:
                print("There not more levels")
                break
        else:
            points_per_level -= level
            user_win = False
            clue(secret_number)

    return user_win, points

def show_information():
    print('#' * 100)
    print('# Welcome to the best game ever')
    print('# The goal is to guess a secret number')
    print('# First you will be prompt your nickname, then choose the level to play the secret number')
    print('#' * 100)


def main():
    # Show information about the game to the user
    show_information()

    # Get user input
    user_name, level_to_play = get_user_input()

    points = check_name(user_name)

    print(f"Current points for {user_name}", points)
    # execute the game
    user_win, points = execute_game(level_to_play, int(points))
    print("Total points", points)


    if user_win:
        print(f'{user_name.capitalize()} you have won')
    else:
        print(f'{user_name.capitalize()} you are a loser')

    write_csv(user_name, points)


try:
    main()
except KeyboardInterrupt:
    print('\nHasta luego, espero que vuelvas pronto!')