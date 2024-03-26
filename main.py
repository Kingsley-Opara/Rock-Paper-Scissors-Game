from difflib import get_close_matches
import secrets

print("Welcome to the Rock-Paper-Scissors game")
print('----------------------------------------')
print(" Enter R for 'Rock', P for 'Paper', and S for 'Scissors' ")

# The list of valid options or players 
possible_options = ['R', 'P', 'S']

# To Allow the user to pick a player 
user_input = input('Please, pick a player from the folowing options: \n').upper()

# The computer randomly choose a player
computer_version = secrets.SystemRandom().choice(possible_options)

# checks if the user input is close to the list of options
checks_list = get_close_matches(user_input, possible_options, n=1, cutoff=0.2)
if checks_list is not None:
    if not user_input in checks_list:
        print(f'Do you mean to pick player {checks_list}')
    else:
        print('Thanks for choosing a valid player!! Best of luck')

# A function that checks if the user input is valid and determines who wins
def test(*args, **kwargs):
    if user_input in possible_options:
        list_of_players = {
            f'Player({user_input})':f"CPU({computer_version})"
        }
        print(list_of_players)
        if user_input == computer_version:
            print('There was a tire')
        elif user_input == 'S' and computer_version == 'P':
            print('Hurray!! Player S won')
        elif user_input == 'P' and computer_version == 'S':
            print('Hurray!! Player S won')
        elif user_input == 'R' and computer_version == 'S':
            print('Hurray!! Player R won')
        elif user_input == 'S' and computer_version == 'R':
            print('Hurray!! Player R won')
        elif user_input == 'P' and computer_version == 'R':
            print('Hurray!! Player P won')
        elif user_input == 'R' and computer_version == 'P':
            print('Hurray!! Player P won')

    while not user_input in possible_options:
        print('An Error has Occured!! The Error is as a result of an Invalid Option OR A Tire in the game, please try again')
        try_again = input('Please, pick a player from the folowing options: \n').upper()
       
        if try_again in possible_options:
            print('Thanks for choosing a valid player!! Best of luck')
            list_of_players = {
                f'Player({try_again})': f'CPU({computer_version})'
            }

            print(list_of_players)
            if try_again == computer_version:
                print('There was a tire')
                continue
            elif try_again == 'S' and computer_version == 'P':
                print('Hurray!! Player S won')
            elif try_again == 'P' and computer_version == 'S':
                print('Hurray!! Player S won')
            elif try_again == 'R' and computer_version == 'S':
                print('Hurray!! Player R won')
            elif try_again == 'S' and computer_version == 'R':
                print('Hurray!! Player R won')
            elif try_again == 'P' and computer_version == 'R':
                print('Hurray!! Player P won')
            elif try_again == 'R' and computer_version == 'P':
                print('Hurray!! Player P won')

            
            break
        else:
            continue


test()




