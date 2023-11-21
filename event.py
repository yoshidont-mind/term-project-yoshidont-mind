import random
import time

import battle
import characters
import game


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
                battle.append_pokemon(character, int(user_input), 5, battle.calculate_max_hp(int(user_input), 5))
                print(f"You've gotten {characters.poke_dex()[int(user_input)]['Name']}!\n")
                make_decision = True
                map_dic[character['Location']][0] = " "  # update map character
                map_dic[character['Location']][1] = ""  # update map value
            else:
                continue
        else:
            print("\nYou're choice is not valid. Please try it again.\n")


def event_home(character):
    print(f"\nMom \"Welcome home, {character['Name']}.",
          f"        You look tired. Take a rest.\"", sep="\n")
    time.sleep(1)
    if character['Pokemon']:
        for pokemon in character['Pokemon']:
            pokemon['HP'] = pokemon['Max HP']
        print(f"\nPokemons have been healed!")
    print(f"\nMom \"Take care, {character['Name']}.\"\n", sep="\n")


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
    
    
# wilderness
def event_wilderness(character):
    if battle.check_for_wild_pokemon():
        pokemon_number = battle.determine_wild_pokemon()
        my_pokemon = battle.next_pokemon(character)
        foe_level = random.randint(2, my_pokemon['Level'] + 2)
        foe = {'Number': pokemon_number,
               'Name': characters.poke_dex()[pokemon_number]['Name'],
               'Level': foe_level,
               'Max HP': battle.calculate_max_hp(pokemon_number, foe_level),
               'HP': battle.calculate_max_hp(pokemon_number, foe_level),
               'Attack': battle.calculate_attack(pokemon_number, foe_level),
               'Defense': battle.calculate_defense(pokemon_number, foe_level)}
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
                    battle.attacks(my_pokemon, foe)
                    if battle.is_alive(foe):
                        battle.attacks(foe, my_pokemon)
                        if not battle.is_alive(my_pokemon):
                            print(f"\n{my_pokemon['Name']} is defeated!")
                            if battle.check_alive_pokemon_remains(character):
                                my_pokemon = battle.next_pokemon(character)
                                print(f"\nLet's go, {my_pokemon['Name']}!")
                            else:
                                print("All pokemons are defeated.",
                                      "You rush home...", sep="\n")
                                time.sleep(2)
                                event_in_progress = False
                                game.go_home(character)
                    else:
                        print(f"\n{my_pokemon['Name']} beat {foe['Name']}!",
                              f"\n{my_pokemon['Name']} got {battle.calculate_acquiring_exp(foe_level)}exp.\n")
                        my_pokemon['Exp'] += battle.calculate_acquiring_exp(foe_level)
                        my_pokemon['Exp to next level'] -= battle.calculate_acquiring_exp(foe_level)

                        # determine level up
                        battle.determine_level_up(my_pokemon)
                        event_in_progress = False
                elif user_input == "2":
                    if len(character['Pokemon']) >= 6:
                        print("\nYou cannot bring more than six pokemons!")
                    elif battle.pokemon_catch(foe):
                        battle.append_pokemon(character, pokemon_number, foe_level, foe['HP'])
                        print(f"Congratulations! You've caught {foe['Name']} successfully!\n")
                        event_in_progress = False
                    else:
                        print(f"Woops, you failed to catch {foe['Name']}.")
                        battle.attacks(foe, my_pokemon)
                        if not battle.is_alive(my_pokemon):
                            print(f"\n{my_pokemon['Name']} is defeated!")
                            if battle.check_alive_pokemon_remains(character):
                                my_pokemon = battle.next_pokemon(character)
                                print(f"\nLet's go, {my_pokemon['Name']}!")
                            else:
                                print("All pokemons are defeated.",
                                      "You rush home...", sep="\n")
                                time.sleep(2)
                                event_in_progress = False
                                game.go_home(character)
                elif user_input == "3":
                    battle.see_pokemons(character, my_pokemon)
                elif user_input == "4":
                    if battle.run_success(my_pokemon, foe):
                        print(f"You've successfully run away from {foe['Name']}!\n")
                        event_in_progress = False
                    else:
                        print(f"Woops, you failed to run from {foe['Name']}.")
                        battle.attacks(foe, my_pokemon)
                        if not battle.is_alive(my_pokemon):
                            print(f"\n{my_pokemon['Name']} is defeated!")
                            if battle.check_alive_pokemon_remains(character):
                                my_pokemon = battle.next_pokemon(character)
                                print(f"\n Let's go, {my_pokemon['Name']}!")
                            else:
                                print("All pokemons are defeated.",
                                      "You rush home...", sep="\n")
                                time.sleep(2)
                                event_in_progress = False
                                game.go_home(character)
            else:
                print("\nYou're choice is not valid. Please try it again.\n")
