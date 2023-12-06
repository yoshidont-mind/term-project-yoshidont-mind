"""
This module is the main module of this game.
Ths module contains main(), game(), and some functions directly related to game().
"""

import time
import json

import event
import characters


def load_save_data():
    """
    Load save data from save_data.json.

    :raises FileNotFoundError: if save_data.json is not found
    :raises json.JSONDecodeError: if save_data.json is corrupted
    :postcondition: save_data is converted from json to dictionary or error is raised
    :return: save_data converted from json to dictionary
    """
    try:
        with open('save_data.json', 'r') as file_object:
            save_data = json.load(file_object)
            save_data['Location'] = tuple(save_data['Location'])  # jsonではタプルを保存できないため、リストに変換している
        return save_data
    except FileNotFoundError:
        print("\nSave data not found. Starting a new game...\n")
        return None
    except json.JSONDecodeError:
        print("\nSave data is corrupted. Starting a new game...\n")
        return None


def generate_map_dictionary():
    """
    Generate a dictionary containing tuples of coordinates as keys and characters as values.

    :postcondition: a dictionary that represents the map is generated
    :return: a dictionary that represents the map
    >>> doctest_map = generate_map_dictionary()
    >>> doctest_map[(0, 0)]
    '▓'
    >>> doctest_map[(15, 1)]
    'H'
    >>> doctest_map[(16, 17)]
    'i'
    """
    # マップデータを文字列として定義
    map_data = """
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓!  #.........#H    ▓
▓## #.........### ##▓
▓   #.........#     ▓
▓!##########i####!##▓
▓                   ▓
▓.... ........!.....▓
▓@@@@ @@@@@@@@@@@@@@▓
▓@@@@i@@@@@@@@@@@@@@▓
▓@@@@!@@@@@@@@@@@@@@▓
▓@@@.i..@@@@@@@@@@@@▓
▓@@.........@@@@@@@@▓
▓@@.......@@@@@@@@  ▓
▓@@.....@@@@@@@@   #▓
▓@@@..        !  #  ▓
▓@@@@.. #### # #    ▓
▓@@@@@@       !   @ ▓
▓@@@@@@@ ### # #i@@ ▓
▓@@@@@@@         @@!▓
▓@@@@@@@@@@@ @@ @@@ ▓
▓@@@@@@@@@@@!@@ @@@ ▓
▓@@@@@.....  @ ! @@ ▓
▓@@@@....           ▓ 
▓@....              ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"""

    # マップデータを行に分割
    map_lines = map_data.strip().split('\n')

    # 各マスに対する情報を格納する辞書
    map_dic = {}

    # 各行と列をループして辞書を作成
    for y, line in enumerate(map_lines):
        for x, char in enumerate(line):
            map_dic[(x, y)] = char

    return map_dic


def describe_current_location(map_dic, character):
    """
    Display the current location of the character along with the surrounding area.

    :param map_dic: a dictionary that represents the map
    :param character: a dictionary that represents the character
    :precondition: map_dic must be a dictionary that represents the map
    :precondition: character must be a dictionary that represents the character
    :precondition: the current location of the character must be in map_dic
    :postcondition: the current location of the character along with the surrounding area is displayed
    >>> doctest_character = {'Location': (15, 1)}
    >>> doctest_map = generate_map_dictionary()
    >>> describe_current_location(doctest_map, doctest_character)
    ▓▓▓▓▓▓▓▓▓▓▓▓▓
    ......#★    ▓
    ......### ##▓
    ......#     ▓
    ####i####!##▓
    Now, you are at "★".
    >>> doctest_character = {'Location': (2, 1)}
    >>> doctest_map = generate_map_dictionary()
    >>> describe_current_location(doctest_map, doctest_character)
    ▓▓▓▓▓▓▓▓▓
    ▓!★ #....
    ▓## #....
    ▓   #....
    ▓!#######
    Now, you are at "★".
    """
    max_x = max(coord[0] for coord in map_dic.keys())
    max_y = max(coord[1] for coord in map_dic.keys())
    for y in range(max(0, character['Location'][1] - 4), min(max_y + 1, character['Location'][1] + 4)):
        for x in range(max(0, character['Location'][0] - 7), min(max_x + 1, character['Location'][0] + 7)):
            if (x, y) == character['Location']:
                print("★", end='')
            elif (x, y) in map_dic:
                char = map_dic[(x, y)][0]
                print(char, end='')
        print()
    print(f"Now, you are at \"★\".")


def get_user_choice(character):
    """
    Get user's choice of direction or action.

    Keep asking for user's choice until the user enters a valid choice.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :postcondition: user's choice of direction or action is gathered
    :return: user's choice of direction or action
    """
    numbers_expected = ["1", "2", "3", "4", "5", "6"]
    option_menu = ""
    if character['Pokemon']:
        numbers_expected += ["7"]
        option_menu += "\n7) Heal Pokémon"
        if len(character['Pokemon']) >= 2:
            numbers_expected += ["8", "9"]
            option_menu += "\n8) Change Pokémon order\n9) Escape Pokémon"
    numbers_expected += ["0"]
    option_menu += "\n0) Save game and quit"
    while True:
        user_input = input("\nPlease enter direction:\n1) Up, 2) Down, 3) Left, 4) Right\n"
                           f"\nYou can also choose these:\n5) Open map\n6) Check status{option_menu}\n")
        if user_input in numbers_expected:
            return user_input
        else:
            print("\nYou're choice is not valid. Please try it again.\n")


def validate_move(map_dic, character, direction):
    """
    Validate if the character can move to the direction.

    :param map_dic: a dictionary that represents the map
    :param character: a dictionary that represents the character
    :param direction: a string which is either of "1", "2", "3", or "4"
    :precondition: map_dic must be a dictionary that represents the map
    :precondition: character must be a dictionary that represents the character
    :precondition: direction must be a string which is either of "1", "2", "3", or "4"
    :postcondition: True or False of whether the character can move to the direction is determined
    :return: True if the character can move to the direction, False otherwise
    >>> doctest_character = {'Location': (15, 1)}
    >>> doctest_map = generate_map_dictionary()
    >>> validate_move(doctest_map, doctest_character, "1")
    False
    >>> validate_move(doctest_map, doctest_character, "4")
    True
    """
    coordinate_changes = {"1": (0, -1), "2": (0, 1), "3": (-1, 0), "4": (1, 0)}
    estimated_x_coordinate = character['Location'][0] + coordinate_changes[direction][0]
    estimated_y_coordinate = character['Location'][1] + coordinate_changes[direction][1]
    new_location = (estimated_x_coordinate, estimated_y_coordinate)
    if new_location in map_dic:
        if map_dic[new_location][0] not in ['#', '▓', '@']:
            return True
        else:
            return False
    else:
        return False


def move_character(character, direction):
    """
    Move the character to the direction.

    :param character: a dictionary that represents the character
    :param direction: a string which is either of "1", "2", "3", or "4"
    :precondition: character must be a dictionary that represents the character
    :precondition: direction must be a string which is either of "1", "2", "3", or "4"
    :precondition: the result of validate_move(map_dic, character, direction) must be True
    :postcondition: the location of the character is correctly updated
    >>> doctest_character = {'Location': (15, 1)}
    >>> move_character(doctest_character, "4")
    >>> doctest_character['Location']
    (16, 1)
    >>> doctest_character = {'Location': (17, 1)}
    >>> move_character(doctest_character, "2")
    >>> doctest_character['Location']
    (17, 2)
    """
    coordinate_changes = {"1": (0, -1), "2": (0, 1), "3": (-1, 0), "4": (1, 0)}
    new_x_coordinate = character['Location'][0] + coordinate_changes[direction][0]
    new_y_coordinate = character['Location'][1] + coordinate_changes[direction][1]
    new_location = (new_x_coordinate, new_y_coordinate)
    character['Location'] = new_location


def open_map(map_dic, character):
    """
    Display the whole map and the current location of the character on it.

    :param map_dic: a dictionary that represents the map
    :param character: a dictionary that represents the character
    :precondition: map_dic must be a dictionary that represents the map
    :precondition: character must be a dictionary that represents the character
    :postcondition: the whole map and the current location of the character on it are displayed
    :postcondition: the user is asked to press Enter to close the map
    """
    # define the size of the map
    max_x = max(coord[0] for coord in map_dic.keys())
    max_y = max(coord[1] for coord in map_dic.keys())

    # loop through each row and column
    for y in range(max_y + 1):
        for x in range(max_x):
            if (x, y) == character['Location']:
                print("★ ", end='')
            else:
                char = map_dic[(x, y)]  # retrieve the character at each coordinates
                print(char * 2, end='')  # print the character twice to make it square
        print()  # add a new line at the end of each row
    print(f"Now, you are at \"★\".\n")
    input("Press Enter to close map.\n")


def check_status(character):
    """
    Display the status of the character.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :postcondition: the status of the character is displayed
    """
    print(f"\n--------------------")
    print(f"Name        : {character['Name']}")
    print(f"Trainer rank: {character['Trainer rank']}")
    print(f"Next goal   : {character['Next goal']}")
    print(f"\nItem:")
    for item in character['Item']:
        print(f" - {item}: {character['Item'][item]}")
    print(f"\n--------------------")
    print("Pokemon:")
    for index in range(len(character['Pokemon'])):
        print(f"{index + 1}) {character['Pokemon'][index]['Name']}")
        print(f" - Level  : {character['Pokemon'][index]['Level']}")
        print(f" - Exp    : {character['Pokemon'][index]['Exp']} / "
              f"{character['Pokemon'][index]['Exp to next level'] + character['Pokemon'][index]['Exp']}")
        print(f" - HP     : {character['Pokemon'][index]['HP']} / {character['Pokemon'][index]['Max HP']}")
        print(f" - Attack : {character['Pokemon'][index]['Attack']}")
        print(f" - Defense: {character['Pokemon'][index]['Defense']}\n")
    print(f"--------------------\n")
    input("Press Enter to close status.\n")


def gather_user_choice_to_heal_pokemon(character):
    """
    Gather user's choice of Pokémon to heal.

    Return 0 if the user's choice is not valid.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: character must have at least 1 Pokémon
    :postcondition: user's choice of Pokémon to heal is gathered
    :return: user's choice of Pokémon to heal, or 0 if the user's choice is not valid
    """
    print("\nNow you're bringing:")
    for index in range(len(character['Pokemon'])):
        print(f"{index + 1}) {character['Pokemon'][index]['Name']}")
        print(f" - Level  : {character['Pokemon'][index]['Level']}")
        print(f" - HP     : {character['Pokemon'][index]['HP']} / {character['Pokemon'][index]['Max HP']}\n")
    selected_number_str = input("Which Pokémon do you want to heal?:\n")
    expected = [str(number) for number in range(1, len(character['Pokemon']) + 1)]
    if selected_number_str in expected:
        selected_number_int = int(selected_number_str)
        return selected_number_int
    else:
        return 0


def gather_user_choice_to_change_order(character):
    """
    Gather user's choice of Pokémon to move to the top of the list.

    Return 0 if the user's choice is not valid.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: character must have at least 2 Pokémon
    :postcondition: user's choice of Pokémon to move to the top of the list is gathered
    :return: user's choice of Pokémon to move to the top of the list, or 0 if the user's choice is not valid
    """
    pokemon_list = ""
    for index in range(len(character['Pokemon'])):
        pokemon_list += f"{index + 1}) {character['Pokemon'][index]['Name']}\n"
    print(f"\nNow, you're bringing:\n{pokemon_list}")
    selected_number_str = input("Which Pokémon do you move to the top?:\n")
    expected = [str(number) for number in range(2, len(character['Pokemon']) + 1)]
    if selected_number_str in expected:
        selected_number_int = int(selected_number_str)
        return selected_number_int
    else:
        return 0


def change_order(character, index):
    """
    Change the order of the Pokémon in the list.

    :param character: a dictionary that represents the character
    :param index: a positive integer which is the index of the Pokémon to move to the top of the list
    :precondition: character must be a dictionary that represents the character
    :precondition: character must have at least 2 Pokémon
    :precondition: index must be an integer
    :precondition: index must be positive
    :precondition: index must be less than the length of character['Pokemon']
    :postcondition: the order of the Pokémon in the list is correctly changed
    >>> doctest_character = {'Pokemon': [{'Name': 'Bulbasaur', 'Level': 5, 'Number': 1, 'Exp': 0,
    ...  'Exp to next level': 5, 'HP': 20, 'Max HP': 20, 'Attack': 5, 'Defense': 5}, {'Name': 'Charmander',
    ... 'Level': 5, 'Number': 4, 'Exp': 0, 'Exp to next level': 5, 'HP': 20, 'Max HP': 20, 'Attack': 5, 'Defense':
    ... 5}, {'Name': 'Squirtle', 'Level': 5, 'Number': 7, 'Exp': 0, 'Exp to next level': 5, 'HP': 20, 'Max HP': 20,
    ... 'Attack': 5, 'Defense': 5}]}
    >>> change_order(doctest_character, 2)
    >>> doctest_character['Pokemon'][0]['Name']
    'Squirtle'
    >>> change_order(doctest_character, 1)
    >>> doctest_character['Pokemon'][0]['Name']
    'Charmander'
    """
    # 選択されたindexのpokemonを先頭に持ってくる
    selected_pokemon = character['Pokemon'].pop(index)
    top_pokemon = character['Pokemon'].pop(0)
    character['Pokemon'].insert(0, selected_pokemon)
    character['Pokemon'].insert(index, top_pokemon)


def gather_user_choice_to_escape_pokemon(character):
    """
    Gather user's choice of Pokémon to escape.

    Return 0 if the user's choice is not valid.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: character must have at least 2 Pokémon
    :postcondition: user's choice of Pokémon to escape is gathered
    :return: user's choice of Pokémon to escape, or 0 if the user's choice is not valid
    """
    pokemon_list = ""
    for index in range(len(character['Pokemon'])):
        pokemon_list += f"{index + 1}) {character['Pokemon'][index]['Name']}\n"
    print(f"\nNow, you're bringing:\n{pokemon_list}")
    selected_number_str = input("Which Pokémon do you want to escape?:\n")
    expected = [str(number) for number in range(1, len(character['Pokemon']) + 1)]
    if selected_number_str in expected:
        selected_number_int = int(selected_number_str)
        return selected_number_int
    else:
        return 0


def save_data_as_json(character):
    """
    Save character data as json file.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :postcondition: character data is saved as json file
    """
    with open('save_data.json', 'w') as file_object:
        json.dump(character, file_object)


def game():
    """
    Execute the game.
    """
    save_data = load_save_data()
    if save_data:
        character = save_data
        print(f"\nSave data found. Loading...\n")
        time.sleep(1)
        characters.print_title()
        print(f"Welcome back, {character['Name']}!\n")
        input("Press Enter to continue.\n")
    else:
        time.sleep(1)
        characters.print_title()
        character_name = input("Please enter your name:\n")
        character = {'Name': character_name, 'Location': (15, 1), 'Pokemon': [],
                     'Item': {'Potion': 0, 'Poke Ball': 0}, 'Trainer rank': 0,
                     'Next goal': 'Let\'s receive a Pokémon from Dr. Nabil and embark on an adventure!',
                     'End roll': False}
        print("\nWelcome to Pokémon's world!\n"
              "In this world, creatures known as Pokémon live everywhere!\n"
              "Now, your goal is to catch Pokémon, train them through battles, "
              "and defeat the BCIT Pokémon Gym leader to collect Gym Badge!\n"
              "Enjoy your adventure!\n")
        input("Press Enter to continue.\n")
        time.sleep(1)
        print(f"Mom \"Good morning, {character['Name']}.\n"
              f"       Today is finally the day you embark on your Pokémon adventure!\n"
              f"       Oh, Dr. Nabil wanted to see you before you leave. He's waiting at the entrance of the town.\n"
              f"       Take care, and have a nice journey.\"\n")
        input("Press Enter to continue.\n")
    map_dic = generate_map_dictionary()
    continue_game = True
    while continue_game:
        describe_current_location(map_dic, character)
        user_choice = get_user_choice(character)
        if user_choice in ["1", "2", "3", "4"]:
            if validate_move(map_dic, character, user_choice):
                move_character(character, user_choice)
                if map_dic[character['Location']] == '!':
                    event.event(character)
                elif map_dic[character['Location']] == 'i':
                    event.event_information(character, user_choice)
                elif map_dic[character['Location']] == 'H':
                    event.event_home(character)
                elif map_dic[character['Location']] == '.':
                    event.event_bush(character)
                elif map_dic[character['Location']] == ' ':
                    event.event_path(character)
                else:
                    pass
            else:
                print("\nYou cannot go this way. Please try it again.\n")
        elif user_choice == "5":
            open_map(map_dic, character)
        elif user_choice == "6":
            check_status(character)
        elif user_choice == "7":
            if character['Item']['Potion'] <= 0:
                print("\nYou don't have any Potion!\n")
            else:
                selected_number = gather_user_choice_to_heal_pokemon(character)
                if selected_number:
                    index = selected_number - 1
                    selected_pokemon = character['Pokemon'][index]
                    if selected_pokemon['HP'] == selected_pokemon['Max HP']:
                        print(f"\n{selected_pokemon['Name']} is already in full health!")
                    else:
                        selected_pokemon['HP'] = selected_pokemon['Max HP']
                        character['Item']['Potion'] -= 1
                        print(f"\nYou healed {selected_pokemon['Name']}!")
                        print(characters.poke_dex()[selected_pokemon['Number']]['Ascii art'])
                        print(f"{selected_pokemon['Name']} looks happy!")
                        print(f"Remaining Potion: {character['Item']['Potion']}\n")
                        input("Press Enter to continue.\n")
        elif user_choice == "8":
            selected_number = gather_user_choice_to_change_order(character)
            if selected_number:
                index = selected_number - 1
                change_order(character, index)
                print(f"\nYou brought {character['Pokemon'][0]['Name']} to the top.")
                print(characters.poke_dex()[character['Pokemon'][0]['Number']]['Ascii art'])
                print(f"\n{character['Pokemon'][0]['Name']} looks happy!\n")
                input("Press Enter to continue.\n")
            else:
                print("\nYour choice is not valid. The request to change order is canceled.\n")
        elif user_choice == "9":
            selected_number = gather_user_choice_to_escape_pokemon(character)
            if selected_number:
                index = selected_number - 1
                selected_pokemon = character['Pokemon'][index]
                print(f"\nYou escaped {selected_pokemon['Name']}."
                      f" By-bye, {selected_pokemon['Name']}!")
                character['Pokemon'].pop(index)  # escape Pokémon
                input("Press Enter to continue.\n")
            else:
                print("\nYour choice is not valid. The request to escape Pokémon is canceled.\n")
        elif user_choice == "0":
            save_data_as_json(character)
            print("\nYour data is saved. See you again!\n")
            continue_game = False
        else:
            print("\nWhoops, something went wrong. Please try it again.\n")
        if character['Trainer rank'] == 3 and not character['End roll']:
            characters.print_congratulations()
            print("\nCongratulations! You achieved your goal in this game. With this, the game comes to an end.\n",
                  "\nNow, the program will save your data and close, but if you're interested, you can restart the "
                  "game and explore this world a bit more.\n",
                  "There are still places you haven't visited, right?\n",
                  "For instance, how about going to Cypress Mountain?\n",
                  "It seems there is an incredibly strong Pokémon trainer at the top of the mountain...?\n",
                  "\nAnyway, thank you so much for playing this game so far!\n",
                  "I hope you enjoyed it, and I'm looking forward to seeing you again soon!\n", sep='')
            character['End roll'] = True
            save_data_as_json(character)
            continue_game = False


def main():
    """
    Execute the game.
    """
    game()


if __name__ == '__main__':
    main()
