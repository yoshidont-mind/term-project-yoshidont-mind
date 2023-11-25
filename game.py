import time

import event
import helper


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
▓@@@. ..@@@@@@@@@@@@▓
▓@@.. ......@@@@@@@@▓
▓@@.. ....@@@@@@@@  ▓
▓@@..  .@@@@@@@@   #▓
▓@@@..        !  #  ▓
▓@@@@.. #### # #   !▓
▓@@@@@@       !   @ ▓
▓@@@@@@@ ### # #i@@ ▓
▓@@@@@@@         @@ ▓
▓@@@@@@@@@@@ @@ @@@ ▓
▓@@@@@@@@@@@ @@ @@@ ▓
▓@@@@@      !@ ! @@ ▓
▓@@@@               ▓ 
▓@                  ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"""

    # マップデータを行に分割
    map_lines = map_data.strip().split('\n')

    # 各マスに対する情報を格納する辞書
    map_dict = {}

    # 各行と列をループして辞書を作成
    for y, line in enumerate(map_lines):
        for x, char in enumerate(line):
            map_dict[(x, y)] = char

    return map_dict


def introduction(character):
    print("\nWelcome to Pokémon's world!\n"
          "In this world, many Pokémon are living with humans.\n"
          "Enjoy your adventure!\n")
    time.sleep(2)

    print(f"Mom \"Good morning, {character['Name']}.",
          f"    Take care.\"\n", sep="\n")


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
        if len(character['Pokemon']) >= 2:
            numbers_expected += ["7", "8"]
            option_menu += ", 7) Change Pokémon order, 8) Escape Pokémon"
    while True:
        user_input = input("\nPlease enter direction: 1) Up, 2) Down, 3) Left, 4) Right\n"
                           f"You can also choose these: 5) Open map, 6) Check status{option_menu}\n")
        if user_input in numbers_expected:
            return user_input
        else:
            print("\nYou're choice is not valid. Please try it again.\n")


def validate_move(map_dic, character, direction):
    new_location = helper.calculate_new_location(character, direction)
    if new_location in map_dic:
        if map_dic[new_location][0] != '#' and map_dic[new_location][0] != '@':
            return True
        else:
            return False
    else:
        return False


def move_character(character, direction):
    new_location = helper.calculate_new_location(character, direction)
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


def game():
    character_name = input("\nPlease enter your name:\n")
    character = {'Name': character_name, 'Location': (15, 1), 'Pokemon': [], 'Item': []}
    map_dic = generate_map_dictionary()
    introduction(character)
    continue_game = True
    while continue_game:
        describe_current_location(map_dic, character)
        user_choice = get_user_choice(character)
        if user_choice in ["1", "2", "3", "4"]:
            if validate_move(map_dic, character, user_choice):
                move_character(character, user_choice)
                describe_current_location(map_dic, character)
                if map_dic[character['Location']] in ['#', '▓']:
                    pass
                if map_dic[character['Location']] == '@':
                    pass
                if map_dic[character['Location']] == '.':
                    event.event_bush(character)
                if map_dic[character['Location']] == '!':
                    event.event(map_dic, character)
                if map_dic[character['Location']] == 'i':
                    event.event_information(character)
                if map_dic[character['Location']] == 'H':
                    event.event_home(character)
                else:
                    pass
            else:
                print("\nYou cannot go this way. Please try it again.\n")
        elif user_choice == "5":
            open_map(map_dic, character)
        elif user_choice == "6":
            check_status(character)
        elif user_choice == "7":
            selected_number = gather_user_choice_to_change_order(character)
            if selected_number:
                index = selected_number - 1
                change_order(character, index)
                print(f"\nYou brought {character['Pokemon'][0]['Name']} to the top.")
            else:
                print("\nYour choice is not valid. The request to change order is canceled.")
        elif user_choice == "8":
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
