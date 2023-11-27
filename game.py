import time

import event
import characters


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
            option_menu += ", 8) Change Pokémon order, 9) Escape Pokémon"
    numbers_expected += ["0"]
    option_menu += "\n0) Save game and quit"
    while True:
        user_input = input("\nPlease enter direction:\n1) Up, 2) Down, 3) Left, 4) Right\n"
                           f"\nYou can also choose these:\n5) Open map, 6) Check status{option_menu}\n")
        if user_input in numbers_expected:
            return user_input
        else:
            print("\nYou're choice is not valid. Please try it again.\n")


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
        for x in range(max_x + 1):
            if (x, y) == character['Location']:
                print("★ ", end='')
            else:
                char = map_dic[(x, y)][0]  # 各マスの文字を取得
                print(char * 2, end='')  # 同じ行の文字を連続して表示
        print()  # 行の終わりに改行を追加
    print(f"Now, you are at \"★\".\n")
    input("Hit 'enter' to close the map.\n")


def check_status(character):
    print(f"\n----------")
    print(f"Name: {character['Name']}")
    print(f"Trainer rank: {character['Trainer rank']}")
    print(f"Item:")
    for item in character['Item']:
        print(f" - {item}: {character['Item'][item]}")
    print(f"----------")
    print("\nPokemon:")
    for index in range(len(character['Pokemon'])):
        print(f"{index + 1}) {character['Pokemon'][index]['Name']}")
        print(f" - Level  : {character['Pokemon'][index]['Level']}")
        print(f" - Exp    : {character['Pokemon'][index]['Exp']} / "
              f"{character['Pokemon'][index]['Exp to next level'] + character['Pokemon'][index]['Exp']}")
        print(f" - HP     : {character['Pokemon'][index]['HP']} / {character['Pokemon'][index]['Max HP']}")
        print(f" - Attack : {character['Pokemon'][index]['Attack']}")
        print(f" - Defense: {character['Pokemon'][index]['Defense']}\n")
    print(f"----------\n")
    input("Hit 'enter' to close status.\n")


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
        print(f" - HP     : {character['Pokemon'][index]['HP']} / {character['Pokemon'][index]['Max HP']}")
    selected_number_str = input("Which Pokémon do you want to heal?:\n")
    expected = [str(number) for number in range(1, len(character['Pokemon']) + 1)]
    if selected_number_str in expected:
        selected_number_int = int(selected_number_str)
        return selected_number_int
    else:
        return 0


def game():
    character_name = input("\nPlease enter your name:\n")
    character = {'Name': character_name, 'Location': (15, 1), 'Pokemon': [], 'Item': {'Potion': 0, 'Poke Ball': 0},
                 'Trainer rank': 0, 'Next goal': 'Let\'s receive a Pokémon from Dr. Nabil and embark on an adventure!'}
    map_dic = generate_map_dictionary()
    print("\nWelcome to Pokémon's world!\n"
          "In this world, many Pokémon are living with humans.\n"
          "Enjoy your adventure!\n")
    time.sleep(2)
    print(f"Mom \"Good morning, {character['Name']}.",
          f"    Take care.\"\n", sep="\n")
    continue_game = True
    while continue_game:
        describe_current_location(map_dic, character)
        user_choice = get_user_choice(character)
        if user_choice in ["1", "2", "3", "4"]:
            if validate_move(map_dic, character, user_choice):
                move_character(character, user_choice)
                describe_current_location(map_dic, character)
                if map_dic[character['Location']] == '.':
                    event.event_bush(character)
                if map_dic[character['Location']] == '!':
                    event.event(map_dic, character)
                if map_dic[character['Location']] == 'i':
                    event.event_information(character)
                if map_dic[character['Location']] == 'H':
                    event.event_home(character)
                if map_dic[character['Location']] == ' ':
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
        elif user_choice == "8":
            selected_number = gather_user_choice_to_change_order(character)
            if selected_number:
                index = selected_number - 1
                change_order(character, index)
                print(f"\nYou brought {character['Pokemon'][0]['Name']} to the top.")
                print(characters.poke_dex()[character['Pokemon'][0]['Number']]['Ascii art'])
                print(f"\n{character['Pokemon'][0]['Name']} looks happy!")
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


def main():
    game()


if __name__ == '__main__':
    main()
