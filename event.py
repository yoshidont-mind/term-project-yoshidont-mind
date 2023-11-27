import random
import time

import battle
import characters


def event(map_dic, character):
    if character['Location'] == (17, 4):
        adventure_preparation(map_dic, character)
    elif character['Location'] == (14, 6):
        lonsdale_quay()
    elif character['Location'] == (5, 9):
        lion_gate_bridge(map_dic, character)
    elif character['Location'] == (1, 4):
        mount_cypress(character)
    elif character['Location'] == (14, 14):
        waterfront()
    elif character['Location'] == (14, 16):
        bcit_pokemon_gym(character)
    elif character['Location'] == (19, 18):
        science_world()
    elif character['Location'] == (12, 20):
        burrard_street_bridge()
    elif character['Location'] == (15, 21):
        granville_island()
    elif character['Location'] == (1, 1):
        cypress_top()
    else:
        pass


def event_information(character):
    if character['Location'] == (5, 8):
        print("\n\"Here is 'Lion Gate Bridge'. The gateway to the world.\"\n")
    elif character['Location'] == (12, 4):
        print("\n\"Here is 'Grouse Mountain'. Be careful for strong Pokémon.\"\n")
    elif character['Location'] == (5, 10):
        print("\n\"Here is 'Stanley Park'. Many Pokémon are living here.\"\n")
    elif character['Location'] == (16, 17):
        print("\n\"Here is 'BC Place'. Winter Olympic was held here in 2010.\"\n")
    else:
        pass


# events > events
def event_home(character):
    print(f"\nMom \"Welcome home, {character['Name']}.",
          f"        You look tired. Take a rest.\"", sep="\n")
    time.sleep(1)
    if character['Pokemon']:
        for pokemon in character['Pokemon']:
            pokemon['HP'] = pokemon['Max HP']
        print(f"\nPokémon have been healed!")
    print(f"\nMom \"Take care, {character['Name']}.\"\n", sep="\n")


def go_home(character):
    character['Location'] = (15, 1)
    print(f"\nMon \"Take care of yourself, {character['Name']}.\"")
    for pokemon in character['Pokemon']:
        pokemon['HP'] = pokemon['Max HP']
    print(f"\nPokémon have been healed!\n")


def event_bush(character):
    if battle.check_for_wild_pokemon():
        foe_pokemon_number = random.randint(1, len(characters.poke_dex()))
        foe_level = random.randint(2, battle.next_pokemon(character)['Level'])
        foe_pokemon = battle.generate_pokemon(foe_pokemon_number, foe_level)
        foe_pokemon_ascii_art = characters.poke_dex()[foe_pokemon_number]['Ascii art']
        print(foe_pokemon_ascii_art)
        print(f"Wild {foe_pokemon['Name']} (Lv. {foe_pokemon['Level']}) appeared!")
        event_continues = True
        while event_continues:
            my_pokemon = battle.next_pokemon(character)
            print(f"\nLet's go, {my_pokemon['Name']}!")
            my_pokemon_wins = battle.pokemon_battle(character, my_pokemon, foe_pokemon, False)
            if my_pokemon_wins:
                event_continues = False
            else:
                if not battle.check_alive_pokemon_remains(character):
                    print(f"\nAll of your Pokémon are defeated!")
                    print(f"\nYou rush your home...")
                    go_home(character)
                    event_continues = False
    else:
        print("\nYou walk through the bush, but nothing happens.\n")


def adventure_preparation(map_dic, character):
    print(f"\nDr.Nabil \"Hi {character['Name']}!",
          "         The outside is full of Pokémon. They sometimes attack you!",
          "         So, you should bring your own Pokémon.",
          "         Now, I give you a Pokémon.",
          "         Which one do you choose?\"", sep="\n")
    numbers_expected = ["1", "2", "3", "4"]
    make_decision = False
    while not make_decision:
        print("\nHere are four Pokémon: 1) Bulbasaur, 2) Charmander, 3) Squirtle, 4) Pikachu\n")
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
                map_dic[character['Location']] = " "  # update map character
            else:
                continue
        else:
            print("\nYou're choice is not valid. Please try it again.\n")
    print(f"\nDr.Nabil \"Now, you're ready to go on an adventure!\"\n")


# invoked by event()
def lonsdale_quay():
    print("\n\"Here is 'Lonsdale Quay', the north shore terminal of 'SeaBus'.\"")
    print("Clerk at the gate \"Sorry, the SeaBus is out of service, now.\"\n")


def lion_gate_bridge(map_dic, character):
    if len(character['Pokemon']) < 6:
        print(f"\nConstruction Worker Sam \"Sorry, you cannot proceed unless you have at least three Pokémon with "
              f"you.\"")
        character["Location"] = (5, 8)
    else:
        print(f"\nConstruction Worker Sam \"If you can defeat me, I'll let you pass through this way!\"")
        print("\nConstruction Worker Sam has challenged you to a battle!")
        sam = {'Name': 'Construction Worker Sam',
               'Pokemon': [battle.generate_pokemon(5, 7),
                           battle.generate_pokemon(6, 8)]}
        win_battle = battle.battle_with_trainer(character, sam)
        if win_battle:
            print("\nConstruction Worker Sam \"Passable!\"")
            map_dic[character['Location']] = " "  # update map character
        else:
            go_home(character)


def mount_cypress(character):
    print("\n\"Here is 'Cypress Mountain', where top Pokémon trainers gather.\"")
    print("For now, you cannot proceed further.\n")
    character["Location"] = (1, 5)


def waterfront():
    print("\n\"Here is 'Waterfront', the south shore terminal of 'SeaBus'.\"")
    print("Clerk at the gate \"Sorry, the SeaBus is out of service, now.\"\n")


def bcit_pokemon_gym(character):
    if 'BCIT Gym Badge' in character['Item']:
        print(f"\nGym Leader Rahul \"Hey {character['Name']}, how are you doing?\"")
    elif len(character['Pokemon']) < 6:
        print(f"\nReceptionist \"You need to have six Pokémon with you to challenge the Gym Leader.\"")
    else:
        print(f"\nGym Leader Rahul \"Welcome to the BCIT Pokémon Gym. I'm Rahul, the Gym Leader.\"",
              f"                \"If you can defeat me, I'll give you a Gym Badge. Let's battle!\"")
        print("\nGym Leader Rahul has challenged you to a battle!")
        rahul = {'Name': 'Gym Leader Rahul',
                 'Pokemon': [battle.generate_pokemon(11, 12),
                             battle.generate_pokemon(10, 12),
                             battle.generate_pokemon(9, 14)]}
        win_battle = battle.battle_with_trainer(character, rahul)
        if win_battle:
            print("\nGym Leader Rahul \"I'm totally defeated. Please take this Gym Badge.\"")
            print(f"\nYou've gotten 'BCIT Gym Badge'!")
            character['Item']['BCIT Gym Badge'] = 1
            print(f"\nGym Leader Rahul \"With this badge, you'll be allowed to enter Cypress Mountain.\"",
                  f"                \"There's an incredibly strong Pokémon trainer at the peak.\"")
            print(f"\nGym Leader Rahul \"Take this, too.\"")
            character['Item']['SeaBus Ticket'] = 1
            print(f"\nYou've gotten 'SeaBus Ticket'!")
            print(f"\nGym Leader Rahul \"With this ticket, you can take SeaBus for free as many times as you want.\"")
            print(f"               \"SeaBus takes you from Waterfront to Lonsdale Quay in no time.\"")
            print(f"               \"Good luck, young Pokémon trainer!\"\n")
        else:
            go_home(character)


def science_world():
    pass


def burrard_street_bridge():
    pass


def granville_island():
    pass


def cypress_top():
    pass
