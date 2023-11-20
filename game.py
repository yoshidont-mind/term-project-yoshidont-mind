import time

import event


def go_home(character):
    character['Location'] = (15, 1)
    print(f"\nMon \"Take care of yourself, {character['Name']}.\"")
    for pokemon in character['Pokemon']:
        pokemon['HP'] = pokemon['Max HP']
    print(f"\nPokemons have been healed!\n")


def change_order(character, index):
    # 選択されたindexのpokemonを先頭に持ってくる
    selected_pokemon = character['Pokemon'].pop(index)
    top_pokemon = character['Pokemon'].pop(0)
    character['Pokemon'].insert(0, selected_pokemon)
    character['Pokemon'].insert(index, top_pokemon)


def escape_pokemon(character, index):
    character['Pokemon'].pop(index)
    

def collect_name():
    character_name = input("\nPlease enter your name:\n")
    return character_name


def make_character(character_name):
    return {'Name': character_name, 'Location': (15, 1), 'Pokemon': [], 'Item': []}


def introduction(character):
    print("\nWelcome to Pokemon's world!\n"
          "In this world, many Pokemons are living with humans.\n"
          "Enjoy your adventure!\n")
    time.sleep(2)

    print(f"Mom \"Good morning, {character['Name']}.",
          f"    Take care.\"\n", sep="\n")


def generate_map_dictionary():
    # マップデータを文字列として定義
    map_data = """
#####################
#!  #.........#H    #
### #.........### ###
#   #.........#     #
#!##########i####!###
#                   #
#.... ........!.....#
#@@@@ @@@@@@@@@@@@@@#
#@@@@i@@@@@@@@@@@@@@#
#@@@@!@@@@@@@@@@@@@@#
#@@@. ..@@@@@@@@@@@@#
#@@.. ......@@@@@@@@#
#@@.. ....@@@@@@@@  #
#@@..  .@@@@@@@@   ##
#@@@..        !  #  #
#@@@@.. #### # #   !#
#@@@@@@       !   @ #
#@@@@@@@ ### # #i@@ #
#@@@@@@@         @@ #
#@@@@@@@@@@@ @@ @@@ #
#@@@@@@@@@@@ @@ @@@ #
#@@@@@      !@ ! @@ #
#@@@@               #
#@                  #
#####################"""

    # マップデータを行に分割
    map_lines = map_data.strip().split('\n')

    # 各マスに対する情報を格納する辞書
    map_dict = {}

    # 各行と列をループして辞書を作成
    for y, line in enumerate(map_lines):
        for x, char in enumerate(line):
            if char == '#':
                value = [char, ""]
            elif char == '@':
                value = [char, ""]
            elif char == '.':
                value = [char, event.event_wilderness]
            elif char == '!':
                value = [char, event]
            elif char == 'i':
                value = [char, event.event_information]
            elif char == 'H':
                value = [char, event.event_home]
            else:
                value = [char, ""]

            map_dict[(x, y)] = value

    return map_dict


def update_map_char(map_dic, coordinates, char):
    map_dic[coordinates][0] = char


def update_map_value(map_dic, coordinates, value):
    map_dic[coordinates][1] = value


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
    option_menu = []
    if character['Pokemon']:
        if len(character['Pokemon']) >= 2:
            numbers_expected.append("7")
            numbers_expected.append("8")
            option_menu.append(", 7) Change pokemon order")
            option_menu.append(", 8) Escape pokemon")
    string_to_add = ""
    for string in option_menu:
        string_to_add += string
    while True:
        user_input = input("\nPlease enter direction: 1) Up, 2) Down, 3) Left, 4) Right\n"
                           f"You can also choose these: 5) Open map, 6) Check status{string_to_add}\n")
        if user_input in numbers_expected:
            return user_input
        else:
            print("\nYou're choice is not valid. Please try it again.\n")


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


def calculate_new_location(character, direction):
    coordinate_changes = {"1": (0, -1), "2": (0, 1), "3": (-1, 0), "4": (1, 0)}
    new_x_coordinate = character['Location'][0] + coordinate_changes[direction][0]
    new_y_coordinate = character['Location'][1] + coordinate_changes[direction][1]
    return new_x_coordinate, new_y_coordinate


def validate_move(map_dic, character, direction):
    new_location = calculate_new_location(character, direction)
    if new_location in map_dic:
        if map_dic[new_location][0] != '#' and map_dic[new_location][0] != '@':
            return True
        else:
            return False
    else:
        return False


def get_destination_mark(map_dic, character, direction):
    new_location = calculate_new_location(character, direction)
    destination_mark = map_dic[new_location][0]
    return destination_mark


def move_character(character, direction):
    new_location = calculate_new_location(character, direction)
    character['Location'] = new_location


def game():
    character_name = collect_name()
    character = make_character(character_name)
    map_dic = generate_map_dictionary()
    introduction(character)
    describe_current_location(map_dic, character)
    alive_pokemon = True
    while alive_pokemon:
        user_choice = get_user_choice(character)
        if user_choice == "5":
            open_map(map_dic, character)
            describe_current_location(map_dic, character)
        elif user_choice == "6":
            check_status(character)
            describe_current_location(map_dic, character)
        elif user_choice == "7":
            pokemon_list = ""
            for index in range(len(character['Pokemon'])):
                pokemon_list += f" {index + 1}) {character['Pokemon'][index]['Name']},"
            print(f"\nNow, you're bringing:{pokemon_list}")
            selected_number_str = input("Which pokemon do you move to the top?:\n")
            numbers_expected = [str(number) for number in range(2, len(character['Pokemon']) + 1)]
            if selected_number_str in numbers_expected:
                selected_number_int = int(selected_number_str)
                change_order(character, selected_number_int - 1)
                print(f"\nYou brought {character['Pokemon'][0]['Name']} to the top.")
            else:
                print("\nYour choice is not valid. The request to change order is canceled.")
        elif user_choice == "8":
            pokemon_list = ""
            for index in range(len(character['Pokemon'])):
                pokemon_list += f" {index + 1}) {character['Pokemon'][index]['Name']},"
            print(f"\nNow, you're bringing:{pokemon_list}")
            selected_number_str = input("Which pokemon do you want to escape?:\n")
            numbers_expected = [str(number) for number in range(2, len(character['Pokemon']) + 1)]
            if selected_number_str in numbers_expected:
                selected_number_int = int(selected_number_str)
                print(f"\nYou escaped {character['Pokemon'][selected_number_int - 1]['Name']}."
                      f" By-bye, {character['Pokemon'][selected_number_int - 1]['Name']}!")
                escape_pokemon(character, selected_number_int - 1)
            else:
                print("\nYour choice is not valid. The request to escape pokemon is canceled.")
        elif validate_move(map_dic, character, user_choice):
            move_character(character, user_choice)
            describe_current_location(map_dic, character)
            if map_dic[character['Location']][1]:
                event.execute_event(map_dic, character)
                describe_current_location(map_dic, character)
        else:
            print("\nYou cannot go this way. Please try it again.\n")
            describe_current_location(map_dic, character)


def main():
    game()


if __name__ == '__main__':
    main()
