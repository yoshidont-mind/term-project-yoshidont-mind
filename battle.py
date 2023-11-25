import random

import characters


def generate_pokemon(pokemon_number, level):
    pokemon_dic = {'Number': pokemon_number,
                   'Name': characters.poke_dex()[pokemon_number]['Name'],
                   'Level': level,
                   'Max HP': calculate_max_hp(pokemon_number, level),
                   'HP': calculate_max_hp(pokemon_number, level),
                   'Attack': calculate_attack(pokemon_number, level),
                   'Defense': calculate_defense(pokemon_number, level),
                   'Exp to next level': calculate_exp_to_next_level(level),
                   'Exp': 0}
    return pokemon_dic


def append_pokemon(character, pokemon_number, level, hp):
    pokemon_dic = generate_pokemon(pokemon_number, level)
    pokemon_dic['HP'] = hp
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
