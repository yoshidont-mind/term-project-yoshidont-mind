"""
This module contains functions related to the battle system.
"""

import random
import time

import characters


def generate_pokemon(pokemon_number, level):
    """
    Generate a dictionary that represents a Pokémon.

    :param pokemon_number: a positive integer which is a key of characters.poke_dex()
    :param level: a positive integer
    :precondition: pokemon_number must be a positive integer
    :precondition: pokemon_number must be a key of characters.poke_dex()
    :precondition: level must be a positive integer
    :postcondition: a dictionary that represents a Pokémon is correctly generated
    :return: a dictionary that represents a Pokémon
    >>> doctest_pokemon = generate_pokemon(1, 5)
    >>> doctest_pokemon['Number']
    1
    >>> doctest_pokemon['Name']
    'Bulbasaur'
    >>> doctest_pokemon['Level']
    5
    >>> doctest_pokemon['Max HP']
    22
    >>> doctest_pokemon['HP']
    22
    >>> doctest_pokemon['Attack']
    12
    >>> doctest_pokemon['Defense']
    12
    >>> doctest_pokemon['Exp to next level']
    100
    >>> doctest_pokemon['Exp']
    0
    >>> doctest_pokemon = generate_pokemon(17, 50)
    >>> doctest_pokemon['Number']
    17
    >>> doctest_pokemon['Name']
    'Mew'
    >>> doctest_pokemon['Level']
    50
    >>> doctest_pokemon['Max HP']
    184
    >>> doctest_pokemon['HP']
    184
    >>> doctest_pokemon['Attack']
    128
    >>> doctest_pokemon['Defense']
    128
    >>> doctest_pokemon['Exp to next level']
    100000
    >>> doctest_pokemon['Exp']
    0
    """
    pokemon_status = {'Number': pokemon_number,
                      'Name': characters.poke_dex()[pokemon_number]['Name'],
                      'Level': level,
                      'Max HP': calculate_max_hp(pokemon_number, level),
                      'HP': calculate_max_hp(pokemon_number, level),
                      'Attack': calculate_attack(pokemon_number, level),
                      'Defense': calculate_defense(pokemon_number, level),
                      'Exp to next level': calculate_exp_to_next_level(level),
                      'Exp': 0}
    return pokemon_status


def append_pokemon(character, pokemon_number, level, hp):
    """
    Append a Pokémon to the character's Pokémon list.

    :param character: a dictionary that represents a character
    :param pokemon_number: a positive integer which is a key of characters.poke_dex()
    :param level: a positive integer
    :param hp: a positive integer which is less than or equal to the max HP of the Pokémon
    :precondition: character must be a dictionary that represents a character
    :precondition: pokemon_number must be a positive integer
    :precondition: pokemon_number must be a key of characters.poke_dex()
    :precondition: level must be a positive integer
    :precondition: hp must be a positive integer
    :precondition: hp must be less than or equal to the max HP of the Pokémon
    :postcondition: a Pokémon is correctly appended to the character's Pokémon list
    >>> doctest_character = {'Name': 'Red', 'Pokemon': []}
    >>> append_pokemon(doctest_character, 1, 5, 22)
    >>> doctest_character['Pokemon'][0]['Number']
    1
    >>> doctest_character['Pokemon'][0]['Name']
    'Bulbasaur'
    >>> doctest_character['Pokemon'][0]['Level']
    5
    >>> doctest_character['Pokemon'][0]['Max HP']
    22
    >>> doctest_character['Pokemon'][0]['HP']
    22
    >>> doctest_character['Pokemon'][0]['Attack']
    12
    >>> doctest_character['Pokemon'][0]['Defense']
    12
    >>> doctest_character['Pokemon'][0]['Exp to next level']
    100
    >>> doctest_character['Pokemon'][0]['Exp']
    0
    >>> doctest_character = {'Name': 'Red', 'Pokemon': []}
    >>> append_pokemon(doctest_character, 17, 50, 184)
    >>> doctest_character['Pokemon'][0]['Number']
    17
    >>> doctest_character['Pokemon'][0]['Name']
    'Mew'
    >>> doctest_character['Pokemon'][0]['Level']
    50
    >>> doctest_character['Pokemon'][0]['Max HP']
    184
    >>> doctest_character['Pokemon'][0]['HP']
    184
    >>> doctest_character['Pokemon'][0]['Attack']
    128
    >>> doctest_character['Pokemon'][0]['Defense']
    128
    >>> doctest_character['Pokemon'][0]['Exp to next level']
    100000
    >>> doctest_character['Pokemon'][0]['Exp']
    0
    """
    pokemon_dic = generate_pokemon(pokemon_number, level)
    pokemon_dic['HP'] = hp
    character['Pokemon'].append(pokemon_dic)


def calculate_max_hp(pokemon_number, level):
    """
    Calculate the max HP of a Pokémon.

    :param pokemon_number: a positive integer which is a key of characters.poke_dex()
    :param level: a positive integer
    :precondition: pokemon_number must be a positive integer
    :precondition: pokemon_number must be a key of characters.poke_dex()
    :precondition: level must be a positive integer
    :postcondition: the max HP of a Pokémon is correctly calculated
    :return: an integer which is the max HP of a Pokémon
    >>> calculate_max_hp(1, 5)
    22
    >>> calculate_max_hp(17, 50)
    184
    """
    base_stats = characters.poke_dex()[pokemon_number]['HP']
    max_hp = round((base_stats * 2 + 47) * level / 100 + 10 + level)
    return max_hp


def calculate_attack(pokemon_number, level):
    """
    Calculate the attack of a Pokémon.

    :param pokemon_number: a positive integer which is a key of characters.poke_dex()
    :param level: a positive integer
    :precondition: pokemon_number must be a positive integer
    :precondition: pokemon_number must be a key of characters.poke_dex()
    :precondition: level must be a positive integer
    :postcondition: the attack of a Pokémon is correctly calculated
    :return: an integer which is the attack of a Pokémon
    >>> calculate_attack(1, 5)
    12
    >>> calculate_attack(17, 50)
    128
    """
    base_stats = characters.poke_dex()[pokemon_number]['Attack']
    attack = round((base_stats * 2 + 47) * level / 100 + 5)
    return attack


def calculate_defense(pokemon_number, level):
    """
    Calculate the defense of a Pokémon.

    :param pokemon_number: a positive integer which is a key of characters.poke_dex()
    :param level: a positive integer
    :precondition: pokemon_number must be a positive integer
    :precondition: pokemon_number must be a key of characters.poke_dex()
    :precondition: level must be a positive integer
    :postcondition: the defense of a Pokémon is correctly calculated
    :return: an integer which is the defense of a Pokémon
    >>> calculate_defense(1, 5)
    12
    >>> calculate_defense(17, 50)
    128
    """
    base_stats = characters.poke_dex()[pokemon_number]['Defense']
    defense = round((base_stats * 2 + 47) * level / 100 + 5)
    return defense


def calculate_exp_to_next_level(level):
    """
    Calculate the exp to next level of a Pokémon.

    :param level: a positive integer
    :precondition: level must be a positive integer
    :postcondition: the exp to next level of a Pokémon is correctly calculated
    :return: an integer which is the exp to next level of a Pokémon
    >>> calculate_exp_to_next_level(5)
    100
    >>> calculate_exp_to_next_level(50)
    100000
    """
    return round((level ** 3) * 0.8)


def calculate_acquiring_exp(level):
    """
    Calculate the acquiring exp of a Pokémon.

    :param level: a positive integer
    :precondition: level must be a positive integer
    :postcondition: the acquiring exp is correctly calculated
    :return: an integer which is acquiring exp
    >>> calculate_acquiring_exp(5)
    107
    >>> calculate_acquiring_exp(50)
    1071
    """
    return round(level * 150 / 7)


def pokemon_catch(foe):
    """
    Determine whether the player successes to catch a Pokémon.

    :param foe: a dictionary that represents a Pokémon
    :precondition: foe must be a dictionary that represents a Pokémon
    :postcondition: whether the player successes to catch a Pokémon is correctly determined
    :return: True if the player successes to catch a Pokémon, False otherwise
    """
    random_number = random.randint(1, round(100 * foe['HP'] / foe['Max HP']))
    if random_number <= 10:
        return True
    else:
        return False


def run_success(my_pokemon, foe):
    """
    Determine whether the player successes to run from a Pokémon.

    :param my_pokemon: a dictionary that represents a Pokémon
    :param foe: a dictionary that represents a Pokémon
    :precondition: my_pokemon must be a dictionary that represents a Pokémon
    :precondition: foe must be a dictionary that represents a Pokémon
    :postcondition: whether the player successes to run from a Pokémon is correctly determined
    :return: True if the player successes to run from a Pokémon, False otherwise
    """
    random_number = random.randint(1, max(20, 100 - 20 * (my_pokemon['Level'] - foe['Level'])))
    if random_number <= 20:
        return True
    else:
        return False


def attacks(offense, defense):
    """
    Execute an attack.

    :param offense: a dictionary that represents a Pokémon
    :param defense: a dictionary that represents a Pokémon
    :precondition: offense must be a dictionary that represents a Pokémon
    :precondition: defense must be a dictionary that represents a Pokémon
    :postcondition: an attack is correctly executed
    :postcondition: the defense's HP is correctly updated
    >>> doctest_offense = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> doctest_defense = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> attacks(doctest_offense, doctest_defense)
    <BLANKLINE>
    Bulbasaur attacks Squirtle!
    The Squirtle is damaged by 5!
    HP of Squirtle: 17/22
    <BLANKLINE>
    >>> doctest_defense['HP']
    17
    >>> doctest_offense = {'Number': 17, 'Name': 'Mew', 'Level': 50, 'Max HP': 184, 'HP': 184, 'Attack': 128,
    ... 'Defense': 128, 'Exp to next level': 100000, 'Exp': 0}
    >>> doctest_defense = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> attacks(doctest_offense, doctest_defense)
    <BLANKLINE>
    Mew attacks Squirtle!
    The Squirtle is damaged by 207!
    HP of Squirtle: 0/22
    <BLANKLINE>
    >>> doctest_defense['HP']
    0
    """
    print(f"\n{offense['Name']} attacks {defense['Name']}!")
    move_power = 40
    damage = round((offense['Level'] * 2 / 5 + 2) * move_power * offense['Attack'] / defense['Defense'] / 50 + 2)
    print(f"The {defense['Name']} is damaged by {damage}!")
    defense['HP'] = max(defense['HP'] - damage, 0)
    print(f"HP of {defense['Name']}: {defense['HP']}/{defense['Max HP']}\n")


def is_alive(pokemon):
    """
    Determine whether a Pokémon is alive.

    :param pokemon: a dictionary that represents a Pokémon
    :precondition: pokemon must be a dictionary that represents a Pokémon
    :postcondition: whether a Pokémon is alive is correctly determined
    :return: True if a Pokémon is alive, False otherwise
    >>> doctest_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> is_alive(doctest_pokemon)
    True
    >>> doctest_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 0, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> is_alive(doctest_pokemon)
    False
    """
    if pokemon['HP'] > 0:
        return True
    else:
        return False


def check_alive_pokemon_remains(character):
    """
    Determine whether there are any alive Pokémon in the character's Pokémon list.

    :param character: a dictionary that represents a character
    :precondition: character must be a dictionary that represents a character
    :postcondition: whether there are any alive Pokémon in the character's Pokémon list is correctly determined
    :return: True if there are any alive Pokémon in the character's Pokémon list, False otherwise
    >>> doctest_character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
    ... 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}, {'Number': 2, 'Name': 'Squirtle',
    ... 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
    >>> check_alive_pokemon_remains(doctest_character)
    True
    >>> doctest_character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
    ... 'HP': 0, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}, {'Number': 2, 'Name': 'Squirtle',
    ... 'Level': 5, 'Max HP': 22, 'HP': 0, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
    >>> check_alive_pokemon_remains(doctest_character)
    False
    """
    for index in range(len(character['Pokemon'])):
        if character['Pokemon'][index]['HP'] > 0:
            return True
    return False


def next_pokemon(character):
    """
    Return the next alive Pokémon in the character's Pokémon list.

    :param character: a dictionary that represents a character
    :precondition: character must be a dictionary that represents a character
    :precondition: there must be any alive Pokémon in the character's Pokémon list
    :postcondition: the next alive Pokémon in the character's Pokémon list is correctly returned
    :return: a dictionary that represents the next alive Pokémon in the character's Pokémon list
    >>> doctest_character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
    ... 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}, {'Number': 2, 'Name': 'Squirtle',
    ... 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
    >>> doctest_next_pokemon = next_pokemon(doctest_character)
    >>> doctest_next_pokemon['Name']
    'Bulbasaur'
    >>> doctest_character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
    ... 'HP': 0, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}, {'Number': 2, 'Name': 'Squirtle',
    ... 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
    >>> doctest_next_pokemon = next_pokemon(doctest_character)
    >>> doctest_next_pokemon['Name']
    'Squirtle'
    """
    # 生きてるポケモンいることが前提条件
    # 生きてるポケモンのうち先頭のものを返す
    for index in range(len(character['Pokemon'])):
        if character['Pokemon'][index]['HP'] > 0:
            return character['Pokemon'][index]


def determine_level_up(pokemon):
    """
    Determine whether a Pokémon levels up.

    Keep leveling up until the Pokémon doesn't level up.

    :param pokemon: a dictionary that represents a Pokémon
    :precondition: pokemon must be a dictionary that represents a Pokémon
    :postcondition: whether a Pokémon levels up is correctly determined
    :postcondition: if a Pokémon levels up, the Pokémon's status is correctly updated
    :postcondition: if a Pokémon levels up, the Pokémon's status and difference are correctly printed
    :postcondition: if a Pokémon levels up, the Pokémon's ascii art is correctly printed
    :postcondition: Exp to next level of the Pokémon is bigger than 0
    >>> doctest_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> determine_level_up(doctest_pokemon)
    >>> doctest_pokemon['Level']
    5
    >>> doctest_pokemon['Exp to next level']
    5
    >>> doctest_pokemon['Exp']
    0
    >>> doctest_pokemon['Attack']
    11
    >>> doctest_pokemon['Defense']
    11
    >>> doctest_pokemon['Max HP']
    22
    >>> doctest_pokemon['HP']
    22
    >>> doctest_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': -20, 'Exp': 0}
    >>> determine_level_up(doctest_pokemon)
    <BLANKLINE>
    Congratulations! Bulbasaur raised to level 6!
    <BLANKLINE>
    Attack raised by 3.
    Defense raised by 3.
    Max HP raised by 2.
    <BLANKLINE>
    <BLANKLINE>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠈⡖⡤⠄⠀
    ⠀⠀⢀⡀⠀⠀⠀⡐⠁⠀⠀⠠⠐⠂⠀⠁⠀⠀⠀⠀
    ⠀⠰⡁⠐⢉⣉⣭⡍⠁⠂⠉⠘⡀⠀⠀⠀⠀⠂⠡⠀
    ⢀⣊⠀⡄⠻⠿⠋⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⢀
    ⡎⣾⠀⠁⣴⡆⠀⠡⢺⣿⣆⠀⢠⢱⣄⠀⠀⠀⠀⠈
    ⡑⠟⠀⠀⠀⠀⠀⢀⣸⡿⠟⠀⠀⠈⢿⣿⡦⡀⠀⡰
    ⠙⠔⠦⣤⣥⣤⣤⣤⡤⠆⠀⠀⠀⠀⢀⢀⠀⠈⠎⠀
    ⠀⠀⠈⣰⡋⢉⠉⠁⠒⠂⢇⢠⡆⠀⠸⢴⣿⠀⠘⠀
    ⠀⠀⠘⡿⠃⠀⠨⠒⢆⣸⣿⠁⠀⡠⡇⠈⠋⠀⠰⠀
    ⠀⠀⠀⠛⠒⠒⠁⠀⠈⠷⡤⠤⠐⠀⠘⠒⠒⠖⠁⠀
    Bulbasaur looks stronger!
    <BLANKLINE>
    >>> doctest_pokemon['Level']
    6
    >>> doctest_pokemon['Exp to next level']
    153
    >>> doctest_pokemon['Exp']
    20
    >>> doctest_pokemon['Attack']
    14
    >>> doctest_pokemon['Defense']
    14
    >>> doctest_pokemon['Max HP']
    24
    >>> doctest_pokemon['HP']
    24
    """
    level_up = False
    while pokemon['Exp to next level'] <= 0:
        level_up = True
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
    if level_up:
        print(f"{characters.poke_dex()[pokemon['Number']]['Ascii art']}")
        print(f"{pokemon['Name']} looks stronger!\n")


def see_pokemon(character, my_pokemon):
    """
    Print the character's Pokémon list.

    :param character: a dictionary that represents a character
    :param my_pokemon: a dictionary that represents a Pokémon
    :precondition: character must be a dictionary that represents a character
    :precondition: my_pokemon must be a dictionary that represents a Pokémon
    :precondition: this function must be invoked during a battle
    :postcondition: the character's Pokémon list is correctly printed
    >>> doctest_character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
    ... 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
    >>> doctest_my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> see_pokemon(doctest_character, doctest_my_pokemon)
    <BLANKLINE>
    ----------
    Now in battle: Bulbasaur
    <BLANKLINE>
    Pokemon:
    1) Bulbasaur
     - Level  : 5
     - HP     : 22 / 22
    <BLANKLINE>
    ----------
    <BLANKLINE>
    >>> doctest_character = {'Name': 'Red', 'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22,
    ... 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}, {'Number': 2, 'Name': 'Squirtle',
    ... 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11, 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
    >>> doctest_my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> see_pokemon(doctest_character, doctest_my_pokemon)
    <BLANKLINE>
    ----------
    Now in battle: Bulbasaur
    <BLANKLINE>
    Pokemon:
    1) Bulbasaur
     - Level  : 5
     - HP     : 22 / 22
    <BLANKLINE>
    2) Squirtle
     - Level  : 5
     - HP     : 22 / 22
    <BLANKLINE>
    ----------
    <BLANKLINE>
    """
    print(f"\n----------")
    print(f"Now in battle: {my_pokemon['Name']}")
    print("\nPokemon:")
    for index in range(len(character['Pokemon'])):
        print(f"{index + 1}) {character['Pokemon'][index]['Name']}")
        print(f" - Level  : {character['Pokemon'][index]['Level']}")
        print(f" - HP     : {character['Pokemon'][index]['HP']} / {character['Pokemon'][index]['Max HP']}\n")
    print(f"----------\n")


def execute_both_attacks(my_pokemon, foe_pokemon):
    """
    Execute both attacks.

    :param my_pokemon: a dictionary that represents a Pokémon
    :param foe_pokemon: a dictionary that represents a Pokémon
    :precondition: my_pokemon must be a dictionary that represents a Pokémon
    :precondition: foe_pokemon must be a dictionary that represents a Pokémon
    :postcondition: both attacks are correctly executed
    :postcondition: if my_pokemon defeats foe_pokemon, my_pokemon gets exp
    :postcondition: if my_pokemon defeats foe_pokemon, whether my_pokemon levels up is correctly determined
    :postcondition: if my_pokemon defeats foe_pokemon and my_pokemon levels up, my_pokemon's status is correctly updated
    :postcondition: turn_result is correctly determined
    :return: a string which is either of "continue", "win", or "lose"
    >>> doctest_my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> doctest_foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> execute_both_attacks(doctest_my_pokemon, doctest_foe_pokemon)
    <BLANKLINE>
    Bulbasaur attacks Squirtle!
    The Squirtle is damaged by 5!
    HP of Squirtle: 17/22
    <BLANKLINE>
    <BLANKLINE>
    Squirtle attacks Bulbasaur!
    The Bulbasaur is damaged by 5!
    HP of Bulbasaur: 17/22
    <BLANKLINE>
    'continue'
    >>> doctest_my_pokemon['HP']
    17
    >>> doctest_foe_pokemon['HP']
    17
    >>> doctest_my_pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> doctest_foe_pokemon = {'Number': 2, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 3, 'Attack': 11,
    ... 'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
    >>> execute_both_attacks(doctest_my_pokemon, doctest_foe_pokemon)
    <BLANKLINE>
    Bulbasaur attacks Squirtle!
    The Squirtle is damaged by 5!
    HP of Squirtle: 0/22
    <BLANKLINE>
    Bulbasaur beat Squirtle! Bulbasaur got 107exp.
    <BLANKLINE>
    <BLANKLINE>
    Congratulations! Bulbasaur raised to level 6!
    <BLANKLINE>
    Attack raised by 3.
    Defense raised by 3.
    Max HP raised by 2.
    <BLANKLINE>
    <BLANKLINE>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠈⡖⡤⠄⠀
    ⠀⠀⢀⡀⠀⠀⠀⡐⠁⠀⠀⠠⠐⠂⠀⠁⠀⠀⠀⠀
    ⠀⠰⡁⠐⢉⣉⣭⡍⠁⠂⠉⠘⡀⠀⠀⠀⠀⠂⠡⠀
    ⢀⣊⠀⡄⠻⠿⠋⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⢀
    ⡎⣾⠀⠁⣴⡆⠀⠡⢺⣿⣆⠀⢠⢱⣄⠀⠀⠀⠀⠈
    ⡑⠟⠀⠀⠀⠀⠀⢀⣸⡿⠟⠀⠀⠈⢿⣿⡦⡀⠀⡰
    ⠙⠔⠦⣤⣥⣤⣤⣤⡤⠆⠀⠀⠀⠀⢀⢀⠀⠈⠎⠀
    ⠀⠀⠈⣰⡋⢉⠉⠁⠒⠂⢇⢠⡆⠀⠸⢴⣿⠀⠘⠀
    ⠀⠀⠘⡿⠃⠀⠨⠒⢆⣸⣿⠁⠀⡠⡇⠈⠋⠀⠰⠀
    ⠀⠀⠀⠛⠒⠒⠁⠀⠈⠷⡤⠤⠐⠀⠘⠒⠒⠖⠁⠀
    Bulbasaur looks stronger!
    <BLANKLINE>
    'win'
    >>> doctest_my_pokemon['HP']
    24
    >>> doctest_foe_pokemon['HP']
    0
    """
    attacks(my_pokemon, foe_pokemon)
    turn_result = "continue"
    if is_alive(foe_pokemon):
        attacks(foe_pokemon, my_pokemon)
        if not is_alive(my_pokemon):
            print(f"{my_pokemon['Name']} is defeated!\n")
            turn_result = "lose"
    else:
        print(f"{my_pokemon['Name']} beat {foe_pokemon['Name']}!",
              f"{my_pokemon['Name']} got {calculate_acquiring_exp(foe_pokemon['Level'])}exp.\n")
        my_pokemon['Exp'] += calculate_acquiring_exp(foe_pokemon['Level'])
        my_pokemon['Exp to next level'] -= calculate_acquiring_exp(foe_pokemon['Level'])
        # determine level up
        determine_level_up(my_pokemon)
        turn_result = "win"
    return turn_result


def execute_catch(character, my_pokemon, foe_pokemon):
    """
    Execute catching a Pokémon.

    :param character: a dictionary that represents a character
    :param my_pokemon: a dictionary that represents a Pokémon
    :param foe_pokemon: a dictionary that represents a Pokémon
    :precondition: character must be a dictionary that represents a character
    :precondition: my_pokemon must be a dictionary that represents a Pokémon
    :precondition: foe_pokemon must be a dictionary that represents a Pokémon
    :precondition: this function must be invoked during a battle with a wild Pokémon
    :postcondition: if the character doesn't have any Poké Ball, the character is correctly notified
    :postcondition: if the character has six or more Pokémon, the character is correctly notified
    :postcondition: if the character has any Poké Ball and less than six Pokémon, number of Poké Ball is correctly
    subtracted by 1
    :postcondition: if the character has any Poké Ball and less than six Pokémon, whether the player successes to catch
    a Pokémon is correctly determined
    :postcondition: if the player successes to catch a Pokémon, the Pokémon is correctly appended to the character's
    Pokémon list
    :postcondition: turn_result is correctly determined
    :return: a string which is either of "continue", "win", or "lose"
    """
    turn_result = "continue"
    if character['Item']['Poke Ball'] <= 0:
        print("\nYou don't have any Poké Ball!")
    elif len(character['Pokemon']) >= 6:
        print("\nYou cannot bring more than six Pokémon!")
    else:
        print(f"\nYou threw a Poké Ball!\n")
        character['Item']['Poke Ball'] -= 1
        time.sleep(1)
        if pokemon_catch(foe_pokemon):
            append_pokemon(character, foe_pokemon['Number'], foe_pokemon['Level'], foe_pokemon['HP'])
            print(f"Congratulations! You've caught {foe_pokemon['Name']} successfully!")
            print(f"Remaining Poké Ball: {character['Item']['Poke Ball']}\n")
            turn_result = "win"
        else:
            print(f"Woops, you failed to catch {foe_pokemon['Name']}.")
            print(f"Remaining Poké Ball: {character['Item']['Poke Ball']}\n")
            attacks(foe_pokemon, my_pokemon)
            if not is_alive(my_pokemon):
                turn_result = "lose"
    return turn_result


def execute_run(my_pokemon, foe_pokemon):
    """
    Execute running away from a Pokémon.

    :param my_pokemon: a dictionary that represents a Pokémon
    :param foe_pokemon: a dictionary that represents a Pokémon
    :precondition: my_pokemon must be a dictionary that represents a Pokémon
    :precondition: foe_pokemon must be a dictionary that represents a Pokémon
    :precondition: this function must be invoked during a battle with a wild Pokémon
    :postcondition: whether the player successes to run from a Pokémon is correctly determined
    :postcondition: whether the player successes to run from a Pokémon is notified
    :postcondition: turn_result is correctly determined
    :return: a string which is either of "continue", "win", or "lose"
    """
    turn_result = "continue"
    if run_success(my_pokemon, foe_pokemon):
        print(f"\nYou've successfully run away from {foe_pokemon['Name']}!\n")
        turn_result = "win"
    else:
        print(f"\nWoops, you failed to run from {foe_pokemon['Name']}.")
        attacks(foe_pokemon, my_pokemon)
        if not is_alive(my_pokemon):
            turn_result = "lose"
    return turn_result


def execute_turn(user_input, character, my_pokemon, foe_pokemon, trainer_battle):
    """
    Execute a turn.

    :param user_input: a string which is either of "1", "2", "3", or "4"
    :param character: a dictionary that represents a character
    :param my_pokemon: a dictionary that represents a Pokémon
    :param foe_pokemon: a dictionary that represents a Pokémon
    :param trainer_battle: a boolean which is True if the battle is with a trainer, False otherwise
    :precondition: user_input must be a string which is either of "1", "2", "3", or "4"
    :precondition: character must be a dictionary that represents a character
    :precondition: my_pokemon must be a dictionary that represents a Pokémon
    :precondition: foe_pokemon must be a dictionary that represents a Pokémon
    :precondition: trainer_battle must be a boolean
    :postcondition: a turn is correctly executed
    :postcondition: turn_result is correctly determined
    :postcondition: if the user inputs "1", both attacks are correctly invoked
    :postcondition: if the user inputs "2", the character's Pokémon list is correctly printed
    :postcondition: if the user inputs "3" and trainer_battle is True, a message is printed
    :postcondition: if the user inputs "3" and trainer_battle is False, catching a Pokémon is correctly executed
    :postcondition: if the user inputs "4" and trainer_battle is True, a message is printed
    :postcondition: if the user inputs "4" and trainer_battle is False, running away from a Pokémon is correctly
    executed
    :return: a string which is either of "continue", "win", or "lose"
    """
    turn_result = "continue"
    if user_input == "1":
        turn_result = execute_both_attacks(my_pokemon, foe_pokemon)
    elif user_input == "2":
        see_pokemon(character, my_pokemon)
    elif user_input == "3":
        if trainer_battle:
            print("\nYou cannot catch a pokemon in battle with a trainer!")
        else:
            turn_result = execute_catch(character, my_pokemon, foe_pokemon)
    elif user_input == "4":
        if trainer_battle:
            print("\nYou cannot run away from a trainer!")
        else:
            turn_result = execute_run(my_pokemon, foe_pokemon)
    return turn_result


def pokemon_battle(character, my_pokemon, foe_pokemon, trainer_battle):
    """
    Execute a battle with a Pokémon.

    :param character: a dictionary that represents a character
    :param my_pokemon: a dictionary that represents a Pokémon
    :param foe_pokemon: a dictionary that represents a Pokémon
    :param trainer_battle: a boolean which is True if the battle is with a trainer, False otherwise
    :precondition: character must be a dictionary that represents a character
    :precondition: my_pokemon must be a dictionary that represents a Pokémon
    :precondition: foe_pokemon must be a dictionary that represents a Pokémon
    :precondition: trainer_battle must be a boolean
    :postcondition: a battle with a Pokémon is correctly executed
    :postcondition: if my_pokemon is defeated or not is correctly determined
    :return: False if my_pokemon is defeated, True otherwise
    """
    turn_result = "continue"
    while turn_result == "continue":
        user_input = input("\nWhat do you do?: 1) Fight, 2) See Pokémon, 3) Catch, 4) Run\n")
        numbers_expected = ["1", "2", "3", "4"]
        if user_input in numbers_expected:
            turn_result = execute_turn(user_input, character, my_pokemon, foe_pokemon, trainer_battle)
            if turn_result == "lose":
                return False
            elif turn_result == "win":
                return True
        else:
            print("\nYou're choice is not valid. Please try it again.\n")


def battle_with_trainer(character, trainer):
    """
    Execute a battle with a trainer.

    :param character: a dictionary that represents a character
    :param trainer: a dictionary that represents a trainer
    :precondition: character must be a dictionary that represents a character
    :precondition: trainer must be a dictionary that represents a trainer
    :postcondition: a battle with a trainer is correctly executed
    :postcondition: whether the player wins or loses is correctly determined
    :return: True if the player wins, False otherwise
    """
    print(f"\nTrainer {trainer['Name']} has challenged you to a battle!\n")
    index = 0
    my_pokemon_changed = True
    foe_pokemon_changed = True
    while index <= len(trainer['Pokemon']):
        my_pokemon = next_pokemon(character)
        foe_pokemon = trainer['Pokemon'][index]
        foe_pokemon_ascii_art = characters.poke_dex()[foe_pokemon['Number']]['Ascii art']
        if foe_pokemon_changed:
            print(f"Remaining foe Pokémon: {len(trainer['Pokemon']) - index}\n")
            print(foe_pokemon_ascii_art)
            print(f"Trainer {trainer['Name']} sent out {foe_pokemon['Name']} (Lv.{foe_pokemon['Level']})!\n")
            foe_pokemon_changed = False
        if my_pokemon_changed:
            print(f"Let's go, {my_pokemon['Name']}!\n")
            foe_pokemon_changed = False
        my_pokemon_wins = pokemon_battle(character, my_pokemon, foe_pokemon, True)
        if my_pokemon_wins:
            foe_pokemon_changed = True
            index += 1
            if not check_alive_pokemon_remains(trainer):
                print(f"You defeated {trainer['Name']}!\n")
                return True
        else:
            my_pokemon_changed = True
            if not check_alive_pokemon_remains(character):
                print(f"You are defeated by {trainer['Name']}!\n")
                return False
