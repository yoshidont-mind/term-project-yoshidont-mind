import time
import random

import characters
import battle
import event


def append_pokemon(character, pokemon_number, level, hp):
    pokemon_dic = {'Number': pokemon_number,
                   'Name': characters.poke_dex()[pokemon_number]['Name'],
                   'Level': level,
                   'Max HP': calculate_max_hp(pokemon_number, level),
                   'HP': hp,
                   'Attack': calculate_attack(pokemon_number, level),
                   'Defense': calculate_defense(pokemon_number, level),
                   'Exp to next level': calculate_exp_to_next_level(level),
                   'Exp': 0}
    character['Pokemon'].append(pokemon_dic)


def calculate_max_hp(pokemon_number, level):
    base_stats = characters.poke_dex()[pokemon_number]['HP']
    max_hp = round((base_stats * 2 + 47) * level / 100 + 10 + level)
    return max_hp


def calculate_attack(pokemon_number, level):
    base_stats = characters.poke_dex()[pokemon_number]['Attack']
    attack = round((base_stats * 2 + 47) * level / 100 + 5)
    return attack


def calculate_defense(pokemon_number, level):
    base_stats = characters.poke_dex()[pokemon_number]['Defense']
    defense = round((base_stats * 2 + 47) * level / 100 + 5)
    return defense


def calculate_exp_to_next_level(level):
    return round((level ** 3) * 0.8)


def calculate_acquiring_exp(level):
    return round(level * 150 / 7)


# events > events
def adventure_preparation(map_dic, character):
    print(f"\nDr.Chris \"Hi {character['Name']}!",
          "         The outside is full of pokemons. They sometimes attack you!",
          "         So, you should bring your own pokemon.",
          "         Now, I give you a pokemon.",
          "         Which one do you choose?\"", sep="\n")
    numbers_expected = ["1", "2", "3", "4"]
    make_decision = False
    while not make_decision:
        print("\nHere are four pokemons: 1) Bulbasaur, 2) Charmander, 3) Squirtle, 4) Pikachu\n")
        user_input = input("Please enter your choice:\n")
        if user_input in numbers_expected:
            pokemon_ascii_art = characters.poke_dex()[int(user_input)]['Ascii art']
            print(pokemon_ascii_art)
            print(f"Are you sure to choose {characters.poke_dex()[int(user_input)]['Name']}?")
            print("1) Yes 2) No\n")
            user_confirm = input("Please enter your choice:\n")
            if user_confirm == "1":
                print(f"\nDr.Chris \"Good choice! {character['Name']}!\"")
                append_pokemon(character, int(user_input), 5, calculate_max_hp(int(user_input), 5))
                print(f"You've gotten {characters.poke_dex()[int(user_input)]['Name']}!\n")
                make_decision = True
                update_map_char(map_dic, character['Location'], " ")
                update_map_value(map_dic, character['Location'], "")
            else:
                continue
        else:
            print("\nYou're choice is not valid. Please try it again.\n")


def lion_gate_bridge(character):
    print("\nFor now, you cannot proceed further.\n",
          "Please look forward to future developments.\n")
    character["Location"] = (5, 8)


def lonsdale_quay():
    print("\n\"Here is 'Lonsdale Quay', the north shore terminal of 'SeaBus'.\"")
    print("Clerk at the gate \"Sorry, the SeaBus is out of service, now.\"\n")


def mount_cypress(character):
    print("\n\"Here is 'Cypress Mountain', where top pokemon trainers gather.\"")
    print("For now, you cannot proceed further.\n")
    character["Location"] = (1, 5)


# events
def check_for_wild_pokemon():
    random_number = random.randint(1, 100)
    if random_number <= 25:
        return True
    else:
        return False


def determine_wild_pokemon():
    pokemon_number = random.randint(1, 4)
    return pokemon_number


def pokemon_catch(foe):
    random_number = random.randint(1, round(100 * foe['HP'] / foe['Max HP']))
    if random_number <= 10:
        return True
    else:
        return False


def run_success(my_pokemon, foe):
    random_number = random.randint(1, min(1, 100 - 20 * (my_pokemon['Level'] - foe['Level'])))
    if random_number <= 20:
        return True
    else:
        return False


def attacks(offense, defense):
    print(f"\n{offense['Name']} attacks {defense['Name']}!")
    move_power = 40
    damage = round((offense['Level'] * 2 / 5 + 2) * move_power * offense['Attack'] / defense['Defense'] / 50 + 2)
    print(f"The {defense['Name']} is damaged by {damage}!")
    defense['HP'] = max(defense['HP'] - damage, 0)
    print(f"HP of {defense['Name']}: {defense['HP']}/{defense['Max HP']}")


def is_alive(pokemon):
    if pokemon['HP'] > 0:
        return True
    else:
        return False


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


def check_alive_pokemon_remains(character):
    for index in range(len(character['Pokemon'])):
        if character['Pokemon'][index]['HP'] > 0:
            return True
    return False


def next_pokemon(character):
    # 生きてるポケモンいることが前提条件
    # 生きてるポケモンのうち先頭のものを返す
    for index in range(len(character['Pokemon'])):
        if character['Pokemon'][index]['HP'] > 0:
            return character['Pokemon'][index]
    return False


def determine_level_up(pokemon):
    while pokemon['Exp to next level'] <= 0:
        pokemon['Level'] += 1
        print(f"\nCongratulations! {pokemon['Name']} raised to level {pokemon['Level']}!\n")
        pokemon['Exp'] = -pokemon['Exp to next level']
        pokemon['Exp to next level'] = calculate_exp_to_next_level(pokemon['Level']) - pokemon['Exp']

        new_attack = calculate_attack(pokemon['Number'], pokemon['Level'])
        print(f"Attack raised by {new_attack - pokemon['Attack']}.")
        pokemon['Attack'] = new_attack

        new_defense = calculate_defense(pokemon['Number'], pokemon['Level'])
        print(f"Defense raised by {new_defense - pokemon['Defense']}.")
        pokemon['Defense'] = new_defense

        new_max_hp = calculate_max_hp(pokemon['Number'], pokemon['Level'])
        max_hp_difference = new_max_hp - pokemon['Max HP']
        print(f"Max HP raised by {max_hp_difference}.\n")
        pokemon['Max HP'] = new_max_hp

        pokemon['HP'] += max_hp_difference


def see_pokemons(character, my_pokemon):
    print(f"\n----------")
    print(f"Now in battle: {my_pokemon['Name']}")
    print("\nPokemon:")
    for index in range(len(character['Pokemon'])):
        print(f"{index + 1}) {character['Pokemon'][index]['Name']}")
        print(f" - Level  : {character['Pokemon'][index]['Level']}")
        print(f" - HP     : {character['Pokemon'][index]['HP']} / {character['Pokemon'][index]['Max HP']}\n")
    print(f"----------\n")


def event_wilderness(character):
    if check_for_wild_pokemon():
        pokemon_number = determine_wild_pokemon()
        my_pokemon = next_pokemon(character)
        foe_level = random.randint(2, my_pokemon['Level'] + 2)
        foe = {'Number': pokemon_number,
               'Name': characters.poke_dex()[pokemon_number]['Name'],
               'Level': foe_level,
               'Max HP': calculate_max_hp(pokemon_number, foe_level),
               'HP': calculate_max_hp(pokemon_number, foe_level),
               'Attack': calculate_attack(pokemon_number, foe_level),
               'Defense': calculate_defense(pokemon_number, foe_level)}
        pokemon_ascii_art = characters.poke_dex()[pokemon_number]['Ascii art']
        print(pokemon_ascii_art)
        print(f"Wild {foe['Name']} (Lv. {foe['Level']}) appeared!")
        print(f"\nLet's go, {my_pokemon['Name']}!")
        event_in_progress = True
        while event_in_progress:
            user_input = input("\nWhat do you do?: 1) Fight, 2) Catch, 3) See pokemons, 4) Run\n")
            numbers_expected = ["1", "2", "3", "4"]
            if user_input in numbers_expected:
                if user_input == "1":
                    attacks(my_pokemon, foe)
                    if is_alive(foe):
                        attacks(foe, my_pokemon)
                        if not is_alive(my_pokemon):
                            print(f"\n{my_pokemon['Name']} is defeated!")
                            if check_alive_pokemon_remains(character):
                                my_pokemon = next_pokemon(character)
                                print(f"\nLet's go, {my_pokemon['Name']}!")
                            else:
                                print("All pokemons are defeated.",
                                      "You rush home...", sep="\n")
                                time.sleep(2)
                                event_in_progress = False
                                go_home(character)
                    else:
                        print(f"\n{my_pokemon['Name']} beat {foe['Name']}!",
                              f"\n{my_pokemon['Name']} got {calculate_acquiring_exp(foe_level)}exp.\n")
                        my_pokemon['Exp'] += calculate_acquiring_exp(foe_level)
                        my_pokemon['Exp to next level'] -= calculate_acquiring_exp(foe_level)

                        # determine level up
                        determine_level_up(my_pokemon)
                        event_in_progress = False
                elif user_input == "2":
                    if len(character['Pokemon']) >= 6:
                        print("\nYou cannot bring more than six pokemons!")
                    elif pokemon_catch(foe):
                        append_pokemon(character, pokemon_number, foe_level, foe['HP'])
                        print(f"Congratulations! You've caught {foe['Name']} successfully!\n")
                        event_in_progress = False
                    else:
                        print(f"Woops, you failed to catch {foe['Name']}.")
                        attacks(foe, my_pokemon)
                        if not is_alive(my_pokemon):
                            print(f"\n{my_pokemon['Name']} is defeated!")
                            if check_alive_pokemon_remains(character):
                                my_pokemon = next_pokemon(character)
                                print(f"\nLet's go, {my_pokemon['Name']}!")
                            else:
                                print("All pokemons are defeated.",
                                      "You rush home...", sep="\n")
                                time.sleep(2)
                                event_in_progress = False
                                go_home(character)
                elif user_input == "3":
                    see_pokemons(character, my_pokemon)
                elif user_input == "4":
                    if run_success(my_pokemon, foe):
                        print(f"You've successfully run away from {foe['Name']}!\n")
                        event_in_progress = False
                    else:
                        print(f"Woops, you failed to run from {foe['Name']}.")
                        attacks(foe, my_pokemon)
                        if not is_alive(my_pokemon):
                            print(f"\n{my_pokemon['Name']} is defeated!")
                            if check_alive_pokemon_remains(character):
                                my_pokemon = next_pokemon(character)
                                print(f"\n Let's go, {my_pokemon['Name']}!")
                            else:
                                print("All pokemons are defeated.",
                                      "You rush home...", sep="\n")
                                time.sleep(2)
                                event_in_progress = False
                                go_home(character)
            else:
                print("\nYou're choice is not valid. Please try it again.\n")


def event(map_dic, character):
    if character['Location'] == (17, 4):
        adventure_preparation(map_dic, character)
    elif character['Location'] == (14, 6):
        lonsdale_quay()
    elif character['Location'] == (5, 9):
        lion_gate_bridge(character)
    elif character['Location'] == (1, 4):
        mount_cypress(character)
    else:
        pass


def event_information(character):
    if character['Location'] == (5, 8):
        print("\n\"Here is 'Lion Gate Bridge'. The gateway to the world.\"\n")
    elif character['Location'] == (12, 4):
        print("\n\"Here is 'Grouse Mountain'. Be careful for strong pokemons.\"\n")


def event_home(character):
    print(f"\nMom \"Welcome home, {character['Name']}.",
          f"        You look tired. Take a rest.\"", sep="\n")
    time.sleep(1)
    if character['Pokemon']:
        for pokemon in character['Pokemon']:
            pokemon['HP'] = pokemon['Max HP']
        print(f"\nPokemons have been healed!")
    print(f"\nMom \"Take care, {character['Name']}.\"\n", sep="\n")


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
                value = [char, event_wilderness]
            elif char == '!':
                value = [char, event]
            elif char == 'i':
                value = [char, event_information]
            elif char == 'H':
                value = [char, event_home]
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


def execute_event(map_dic, character):
    event_function = map_dic[character['Location']][1]
    need_map_and_character = [event]
    need_map = []
    need_character = [event_home, event_wilderness, event_information]

    if event_function in need_map_and_character:
        event_function(map_dic, character)
    elif event_function in need_map:
        event_function(map_dic)
    elif event_function in need_character:
        event_function(character)
    else:
        event_function()


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
                execute_event(map_dic, character)
                describe_current_location(map_dic, character)
        else:
            print("\nYou cannot go this way. Please try it again.\n")
            describe_current_location(map_dic, character)


def main():
    game()


if __name__ == '__main__':
    main()
