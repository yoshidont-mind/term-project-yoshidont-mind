import time
import json

import event
import characters


def load_save_data():
    try:
        with open('save_data.json', 'r') as file_object:
            save_data = json.load(file_object)
            save_data['Location'] = tuple(save_data['Location'])  # jsonではタプルを保存できないため、リストに変換している
        return save_data
    except FileNotFoundError:
        print("\nSave data not found. Starting a new game.\n")
        return None
    except json.JSONDecodeError:
        print("\nSave data is corrupted. Starting a new game.\n")
        return None


def generate_map_dictionary():
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
▓@@.. ......@@@@@@@@▓
▓@@.. ....@@@@@@@@  ▓
▓@@..  .@@@@@@@@   #▓
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


def save_data_as_json(character):
    with open('save_data.json', 'w') as f:
        json.dump(character, f)


def validate_move(map_dic, character, direction):
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
    coordinate_changes = {"1": (0, -1), "2": (0, 1), "3": (-1, 0), "4": (1, 0)}
    new_x_coordinate = character['Location'][0] + coordinate_changes[direction][0]
    new_y_coordinate = character['Location'][1] + coordinate_changes[direction][1]
    new_location = (new_x_coordinate, new_y_coordinate)
    character['Location'] = new_location


def open_map(map_dic, character):
    # マップの幅と高さを決定
    max_x = max(coord[0] for coord in map_dic.keys())
    max_y = max(coord[1] for coord in map_dic.keys())

    # 各行と列に対してループし、文字を取得して表示
    for y in range(max_y + 1):
        for x in range(max_x):
            if (x, y) == character['Location']:
                print("★ ", end='')
            else:
                char = map_dic[(x, y)]  # 各マスの文字を取得
                print(char * 2, end='')  # 同じ行の文字を連続して表示
        print()  # 行の終わりに改行を追加
    print(f"Now, you are at \"★\".\n")
    input("Press Enter to close map.\n")


def check_status(character):
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


def gather_user_choice_to_change_order(character):
    pokemon_list = ""
    for index in range(len(character['Pokemon'])):
        pokemon_list += f" {index + 1}) {character['Pokemon'][index]['Name']},"
    print(f"\nNow, you're bringing:{pokemon_list}")
    selected_number_str = input("Which Pokémon do you move to the top?:\n")
    expected = [str(number) for number in range(2, len(character['Pokemon']) + 1)]
    if selected_number_str in expected:
        selected_number_int = int(selected_number_str)
        return selected_number_int
    else:
        return 0


def change_order(character, index):
    # 選択されたindexのpokemonを先頭に持ってくる
    selected_pokemon = character['Pokemon'].pop(index)
    top_pokemon = character['Pokemon'].pop(0)
    character['Pokemon'].insert(0, selected_pokemon)
    character['Pokemon'].insert(index, top_pokemon)


def gather_user_choice_to_escape_pokemon(character):
    pokemon_list = ""
    for index in range(len(character['Pokemon'])):
        pokemon_list += f" {index + 1}) {character['Pokemon'][index]['Name']},"
    print(f"\nNow, you're bringing:{pokemon_list}")
    selected_number_str = input("Which Pokémon do you want to escape?:\n")
    expected = [str(number) for number in range(1, len(character['Pokemon']) + 1)]
    if selected_number_str in expected:
        selected_number_int = int(selected_number_str)
        return selected_number_int
    else:
        return 0


def gather_user_choice_to_heal_pokemon(character):
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


def game():
    save_data = load_save_data()
    if save_data:
        character = save_data
        print(f"\nSave data found. Loading...")
        time.sleep(1)
        print(f"\nWelcome back, {character['Name']}!")
        input("\nPress Enter to continue...\n")
    else:
        character_name = input("\nPlease enter your name:\n")
        character = {'Name': character_name, 'Location': (15, 1), 'Pokemon': [],
                     'Item': {'Potion': 0, 'Poke Ball': 0}, 'Trainer rank': 0,
                     'Next goal': 'Let\'s receive a Pokémon from Dr. Nabil and embark on an adventure!',
                     'End roll': False}
        print("\nWelcome to Pokémon's world!\n"
              "In this world, many Pokémon are living with humans.\n"
              "Enjoy your adventure!\n")
        time.sleep(2)
        print(f"Mom \"Good morning, {character['Name']}.",
              f"    Take care.\"\n", sep="\n")
    map_dic = generate_map_dictionary()
    continue_game = True
    while continue_game:
        describe_current_location(map_dic, character)
        user_choice = get_user_choice(character)
        if user_choice == "0":
            save_data_as_json(character)
            print("\nYour game is saved. See you again!\n")
            continue_game = False
        elif user_choice in ["1", "2", "3", "4"]:
            if validate_move(map_dic, character, user_choice):
                move_character(character, user_choice)
                if map_dic[character['Location']] == '.':
                    event.event_bush(character)
                elif map_dic[character['Location']] == '!':
                    event.event(character)
                elif map_dic[character['Location']] == 'i':
                    event.event_information(character, user_choice)
                elif map_dic[character['Location']] == 'H':
                    event.event_home(character)
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
                print("\nYou don't have any Potion!")
            else:
                selected_number = gather_user_choice_to_heal_pokemon(character)
                if selected_number:
                    index = selected_number - 1
                    if character['Pokemon'][index]['HP'] == character['Pokemon'][index]['Max HP']:
                        print(f"\n{character['Pokemon'][index]['Name']} is already in full health!")
                    else:
                        character['Pokemon'][index]['HP'] = character['Pokemon'][index]['Max HP']
                        character['Item']['Potion'] -= 1
                        print(f"\nYou healed {character['Pokemon'][index]['Name']}!")
                        print(characters.poke_dex()[character['Pokemon'][index]['Number']]['Ascii art'])
                        print(f"{character['Pokemon'][index]['Name']} looks happy!")
                        print(f"Remaining Potion: {character['Item']['Potion']}")
                        input("\nPress Enter to continue.\n")
        elif user_choice == "8":
            selected_number = gather_user_choice_to_change_order(character)
            if selected_number:
                index = selected_number - 1
                change_order(character, index)
                print(f"\nYou brought {character['Pokemon'][0]['Name']} to the top.")
                print(characters.poke_dex()[character['Pokemon'][0]['Number']]['Ascii art'])
                print(f"\n{character['Pokemon'][0]['Name']} looks happy!")
                input("\nPress Enter to continue.\n")
            else:
                print("\nYour choice is not valid. The request to change order is canceled.")
        elif user_choice == "9":
            selected_number = gather_user_choice_to_escape_pokemon(character)
            if selected_number:
                index = selected_number - 1
                print(f"\nYou escaped {character['Pokemon'][index]['Name']}."
                      f" By-bye, {character['Pokemon'][index]['Name']}!")
                character['Pokemon'].pop(index)  # escape Pokémon
            else:
                print("\nYour choice is not valid. The request to escape Pokémon is canceled.")
        else:
            print("\nWhoops, something went wrong. Please try it again.\n")
        if character['Trainer rank'] == 3 and not character['End roll']:
            print("\nCongratulations! You achieved your goal in this game. With this, the game comes to an end.\n",
                  "\nNow, the program will save your data and close, but if you're interested, you can restart the "
                  "game and explore this world a bit more.\n",
                  "There are still places you haven't visited, right?\n",
                  "For instance, how about going to Cypress Mountain?\n",
                  "It seems there is an incredibly strong Pokémon trainer at the top of the mountain...?\n",
                  "\n Anyway, thank you so much for playing this game so far!\n",
                  "I hope you enjoyed it, and I'm looking forward to seeing you again soon!\n")
            character['End roll'] = True
            save_data_as_json(character)
            continue_game = False


def main():
    game()


if __name__ == '__main__':
    main()
