from pip._vendor import requests
import random  # This library is to generate random numbers. Function show line 44
import time  # This module allows you to work with time related functions. Shown line 14
import sys  # provides various functions & variables that are used to manipulate different parts of the Python runtime
# environment. Function shown on line 74


# A Pokemon Game logo as an introduction to make it look good.
logo = '''\33[33m██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗
██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
\33[0m '''

print(logo)
time.sleep(1)

print('                Hello & Welcome to the game!', '\n')  # Welcome message
time.sleep(1.5)

# Rules of the game using colour and styling.
print("                 \33[30m\33[43m   ✮.RULES OF THE GAME.✮  \33[0m          ")
print('''+--------------------------------------------------------------+
| ❤ Pick your your Pokemon or get a random Pokemon             |
| ❤ Select a stat to play against your opponent                |
| ❤ The stats of the two cards are compared                    |
| ❤ The player with the highest stat than their opponent wins  |
| ❤ You will be able to play the game multiple times           |
| ❤ The scores will be compared  at the end of each game       |
+--------------------------------------------------------------+
''')


def random_pokemon():
    """ 
    Returns a dictionary containing information about a randomly chosen Pokemon.
    A Pokemon is chosen randomly by generating a random ID number between 1-151.
    The dictionary includes the Pokemon's name, ID, height, weight, attack, and speed.

    Returns:
    dict: A dictionary containing the following Pokemon details:
        - 'name': The name of the randomly chosen Pokemon.
        - 'id': The ID number of the randomly chosen Pokemon.
        - 'height': The height of the randomly chosen Pokemon.
        - 'weight': The weight of the randomly chosen Pokemon.
        - 'attack': The base attack stat of the randomly chosen Pokemon.
        - 'speed': The base speed stat of the randomly chosen Pokemon.
    
    Note:
    The function utilizes the PokeAPI (https://pokeapi.co/) to fetch information about the Pokemon.
    """  
    # Generates a random number between 1-151 for selecting a Pokemon
    random_no = random.randint(1, 151)  
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_no)  # Number is inserted to the API url to get Pokemon.
    response = requests.get(url)  # Pulls out information from the url using the request library
    pokemon = response.json()  # Retrieves specific information for that Pokemon.
    
    # Dictionary that contains the returned Pokemon name, id, height, weight and stats.
    return {   
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'attack': pokemon['stats'][1]['base_stat'], # Attack stat is at index 1 in the 'stats' list
        'speed': pokemon['stats'][5]['base_stat'], # Speed stat is at index 5 in the 'stats' list
    }


def choose_pokemon(): 
    """
    Prompts the user to enter a Pokemon name or ID number, retrieves information
    about the specified Pokemon from the PokeAPI, and returns a dictionary with
    relevant details.

    Returns:
    dict: A dictionary containing the following Pokemon details:
        - 'name': The name of the Pokemon.
        - 'id': The ID number of the Pokemon.
        - 'height': The height of the Pokemon.
        - 'weight': The weight of the Pokemon.
        - 'attack': The base attack stat of the Pokemon.
        - 'speed': The base speed stat of the Pokemon.

    Note:
    The function uses the PokeAPI (https://pokeapi.co/) to fetch Pokemon information.
    """
    name = input('Please enter the Pokemon name or ID number: ') # Promt the user to enter a Pokemon name or ID number
    url2 = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(name)  # Construct the API URL using the entered name or ID
    response = requests.get(url2) # Make a GET request to the PokeAPI to retrieve information about the Pokemon
    pokemon = response.json() # Parse the JSON response into a Python dictionary
    
    # Return a dictionary containing relevant details about the specified Pokemon
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'attack': pokemon['stats'][1]['base_stat'], # Attack stat is at index 1 in the 'stats' list
        'speed': pokemon['stats'][5]['base_stat'], # Speed stat is at index 5 in the 'stats' list
    }


def delay(s):
    """
    Displays text with a delay, making it appear as if the text is moving slowly.

    Args:
    s (str): The text to be displayed with a delay.

    Note:
    This function uses sys.stdout.write to print each character of the input string
    with a delay introduced by time.sleep(0.05) to simulate a slow-moving effect.
    """
    # Iterate through each character in the input string
    for c in s:
        sys.stdout.write(c) # Write the character to the standard output
        sys.stdout.flush()  # Flush the standard output to ensure immediate display
        time.sleep(0.05)  # Introduce a delay of 0.05 seconds between characters


def run():
    """
    Runs a Pokemon comparison game allowing the user to choose between entering a Pokemon name or ID
    or getting a random Pokemon. The game involves comparing selected stats of the user's Pokemon
    with a randomly generated enemy Pokemon. The user earns points based on the comparison, and the
    game can be played again. The points are stored in a file named 'pokemon.txt'.

    Note:
    The function utilizes various input prompts, delays, and visual effects to enhance the user experience.

    Returns:
    None

    Raises:
    KeyboardInterrupt: If the user interrupts the program (e.g., by pressing Ctrl+C), the game will exit.
    """
    # Points stored for when the user wins or loses
    winner = 0
    loser = 0

    while True:  # 'While True' functions helps to start a new game again if user still wants to keep playing.
        print('Would you like to enter the pokemon you want or get a random pokemon? ')
        enter_random = input('[ENTER]  or  [RANDOM]: ').lower()  # .lower() = to make text lower case when user enters.

        user_pokemon = random_pokemon()  # Variable to create a random Pokemon for user.
        enemy_pokemon = random_pokemon()  # Variable to create a random Pokemon for Enemy(computer).

        if enter_random == 'random':  # if user inputs to get a 'random' Pokemon, a random Pokemon will be selected.
            delay('\n\33[30m\33[43m         LOADING......             \33[0m')  # Loading sign moving across slowly.
            print('')  # Creates a new blank line.
            print('\nYour Pokemon is: {}'.format(user_pokemon['name'].title()), '\n')  # User Pokemon is shown here.
            # Stats of the Pokemon is shown here ⬇
            print('     Name: {} \n     ID: {}'.format(user_pokemon['name'].title(), user_pokemon['id']))
            print('     Height: {} \n     Weight: {}'.format(user_pokemon['height'], user_pokemon['weight']))
            print('     Attack: {} \n     Speed: {} \n'.format(user_pokemon['attack'], user_pokemon['speed']))

            print('Your enemy Pokemon is: {}'.format(enemy_pokemon['name'].title()))  # Enemy Pokemon is shown here
            time.sleep(1)

            print("\n[ID]   [HEIGHT]   [WEIGHT]   [ATTACK]   [SPEED]")  # Stats for the user to choose to play against.
            stat_choice = input('Which stat do you want to use? ').lower()  # User enters the stat
            time.sleep(0.5)

            user_stat = user_pokemon[stat_choice]  # Variable is the stat the user picked.
            enemy_stat = enemy_pokemon[stat_choice]  # Variable is to create the stat user picked for the enemy.

            print('\nYour pokemon {} is: {}'.format(stat_choice, user_stat))  # User Pokemon stat and stat number.
            time.sleep(1)

            print('Your enemy pokemon {} is: {}'.format(stat_choice, enemy_stat), '\n')  # Enemy Pokemon stat & number.
            time.sleep(1)

            if user_stat > enemy_stat:  # If user stat number is higher than enemy, adds 1 point to the winner.
                winner += 1
                print('Your {} is higher.'.format(stat_choice))
                print('You Won! Well done.')

            elif user_stat < enemy_stat:  # If user stat number is lower than enemy, adds 1 point to the enemy.
                loser += 1
                print('Your {} is lower.'.format(stat_choice))
                print('You lost! Better luck next time!')

            else:  # If the stat numbers are the same, a point gets added for user and enemy.
                winner += 1
                loser += 1
                print('Draw!')

        elif enter_random == 'enter':  # if user inputs 'enter' then this function lets user enter name or id.
            user_choose = choose_pokemon()  # User enters the Pokemon name or ID here
            delay('\n\33[30m\33[43m         LOADING......             \33[0m')
            print('')
            print('\nYou entered pokemon: {}'.format(user_choose['name'].title()), '\n')

            print('      Name: {} \n      ID: {} '.format(user_choose['name'].title(), user_choose['id']))
            print('      Height: {} \n      Weight: {} '.format(user_pokemon['height'], user_pokemon['weight']))
            print('      Attack: {} \n      Speed: {} \n'.format(user_choose['attack'], user_choose['speed']))

            print('Your enemy Pokemon is: {}'.format(enemy_pokemon['name'].title()), '\n')
            time.sleep(1)

            print("[ID]   [HEIGHT]   [WEIGHT]   [ATTACK]   [SPEED]")
            stat_choice = input('Which stat do you want to use? ').lower()
            time.sleep(0.5)

            user_stat = user_choose[stat_choice]
            enemy_stat = enemy_pokemon[stat_choice]

            print('\nYour pokemon {} is: {}'.format(stat_choice, user_stat))
            time.sleep(1)
            print('Your enemy pokemon {} is: {}'.format(stat_choice, enemy_stat), '\n')
            time.sleep(1)

            if user_stat > enemy_stat:
                winner += 1
                print('Your {} is higher.'.format(stat_choice))
                print('You Won! Well done.')

            elif user_stat < enemy_stat:
                loser += 1
                print('Your {} is lower.'.format(stat_choice))
                print('You lost! Better luck next time!')

            else:
                winner += 1
                loser += 1
                print('Draw!')

        # If user doesn't enter 'random' or 'enter' correctly at the beginning, an error message will pop up to try again.
        # A new loop will appear to play the game.
        elif enter_random != 'enter' or 'random':
            print('\n       \33[30m \x1b[48;5;160m \033[1m     ERROR!      \33[0m')  # \033[1m = Bold font

            print('Sorry, I did not recognise what you typed.')
            enter_random = input('Please type ENTER or RANDOM here: ').lower()  # User can enter again correctly.
            # A new loop for random, enter etc. is created again.
            if enter_random == 'random':
                delay('\n\33[30m\33[43m        LOADING......          \33[0m')
                print('')
                print('\nYour Pokemon is: {}'.format(user_pokemon['name'].title()), '\n')

                print('     Name: {} \n     ID: {}'.format(user_pokemon['name'].title(), user_pokemon['id']))
                print('     Height: {} \n     Weight: {}'.format(user_pokemon['height'], user_pokemon['weight']))
                print('     Attack: {} \n     Speed: {} \n'.format(user_pokemon['attack'], user_pokemon['speed']))

                print('Your enemy Pokemon is: {}'.format(enemy_pokemon['name'].title()))  # .title() = Capital letter
                time.sleep(1)

                print("\n[ID]   [HEIGHT]   [WEIGHT]   [ATTACK]   [SPEED]")
                stat_choice = input('Which stat do you want to use? ').lower()
                time.sleep(0.5)

                user_stat = user_pokemon[stat_choice]
                enemy_stat = enemy_pokemon[stat_choice]

                print('\nYour pokemon {} is: {}'.format(stat_choice, user_stat))
                time.sleep(1)
                print('Your enemy pokemon {} is: {}'.format(stat_choice, enemy_stat), '\n')
                time.sleep(1)

                if user_stat > enemy_stat:
                    winner += 1
                    print('Your {} is higher.'.format(stat_choice))
                    print('Your the winner!')

                elif user_stat < enemy_stat:
                    loser += 1
                    print('Your {} is lower'.format(stat_choice))
                    print('Your the loser!')

                else:
                    winner += 1
                    loser += 1
                    print('Draw!')

            elif enter_random == 'enter':
                delay('\n\33[30m\33[43m        LOADING......          \33[0m')
                print('')
                user_choose = choose_pokemon()
                print('\nYou entered pokemon: {}'.format(user_choose['name'].title()), '\n')

                print('      Name: {} \n      ID: {} '.format(user_choose['name'].title(), user_choose['id']))
                print('      Height: {} \n      Weight: {} '.format(user_pokemon['height'], user_pokemon['weight']))
                print('      Attack: {} \n      Speed: {} \n'.format(user_choose['attack'], user_choose['speed']))

                print('Your enemy Pokemon is: {}'.format(enemy_pokemon['name'].title()), '\n')
                time.sleep(1)

                print("[ID]   [HEIGHT]   [WEIGHT]   [ATTACK]   [SPEED]")
                stat_choice = input('Which stat do you want to use? ').lower()
                time.sleep(0.5)

                user_stat = user_choose[stat_choice]
                enemy_stat = enemy_pokemon[stat_choice]

                print('\nYour pokemon {} is: {}'.format(stat_choice, user_stat))
                time.sleep(1)
                print('Your enemy pokemon {} is: {}'.format(stat_choice, enemy_stat), '\n')
                time.sleep(1)

                if user_stat > enemy_stat:
                    winner += 1
                    print('Your {} is higher.'.format(stat_choice))
                    print('Your the Winner!')

                elif user_stat < enemy_stat:
                    loser += 1
                    print('Your {} is lower.'.format(stat_choice))
                    print('Your enemy wins!')

                else:
                    winner += 1
                    loser += 1
                    print('Draw!')

        # The points are shown for the user and their enemy.
        print('\n\33[33m\33[40m Your points: {} | Enemy points: {} \33[0m'.format(winner, loser), '\n')
        time.sleep(1)

        print('Would you like to play again?')  # User can choose to keep playing.
        play_again = input('Please enter YES or NO: ').lower()  # User enters yes or no to play.

        with open('pokemon.txt', 'a+') as pokemon_file:  # stores the points in the file, 'pokemon_file'.
            pokemon_file.write('Your points are {}, Your enemy points {} '.format(winner, loser) + '\n')

        if play_again == 'yes':  # If player inputs yes, then a new game will start.
            print('\n\33[93m\33⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚\33[0m')
            print('              \33[30m\33[43m             NEW GAME               \33[0m                ')
            print('\33[93m\33⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚\33[0m')
            print('')
            time.sleep(0.5)
            continue  # continue = to carry on the while true loop, so the game starts again.

        elif play_again == 'no':  # If player inputs no, then the game ends
            print('\n\33[93m\33⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚\33[0m')
            print('              \33[30m\33[43m             GAME OVER               \33[0m                ')
            print('\33[93m\33⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚\33[0m')
            time.sleep(0.5)
            break  # Break = to end the loop so the game ends.


run()
