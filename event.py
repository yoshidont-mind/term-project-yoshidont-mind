import random
import time

import battle
import characters


def event(character):
    if character['Location'] == (17, 4):
        adventure_preparation(character)
    elif character['Location'] == (14, 6):
        lonsdale_quay(character)
    elif character['Location'] == (5, 9):
        lion_gate_bridge(character)
    elif character['Location'] == (1, 4):
        mount_cypress(character)
    elif character['Location'] == (14, 14):
        waterfront(character)
    elif character['Location'] == (14, 16):
        bcit_pokemon_gym(character)
    elif character['Location'] == (19, 18):
        science_world(character)
    elif character['Location'] == (12, 20):
        burrard_street_bridge(character)
    elif character['Location'] == (15, 21):
        granville_island(character)
    elif character['Location'] == (1, 1):
        cypress_top(character)
    else:
        pass


def event_information(character, user_choice):
    if character['Location'] == (5, 8):
        print("\n\"Here is 'Lion Gate Bridge'. The gateway to the world.\"\n")
        input("Press Enter to continue.\n")
    elif character['Location'] == (12, 4):
        if user_choice == "1":
            print("\n\"Here is 'Grouse Mountain'. Be careful for strong Pokémon.\"\n")
            input("Press Enter to continue.\n")
    elif character['Location'] == (5, 10):
        if user_choice == "2":
            print("\n\"Here is 'Stanley Park'. Many Pokémon are living here.\"\n")
            input("Press Enter to continue.\n")
    elif character['Location'] == (16, 17):
        print("\n\"Here is 'BC Place'. Winter Olympic was held here in 2010.\"\n")
        input("Press Enter to continue.\n")
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
    print(f"\nMon \"Take care of yourself, {character['Name']}.\"\n")
    input("\nPress Enter to continue.\n")


def go_home(character):
    character['Location'] = (15, 1)
    print(f"\nMon \"Take care of yourself, {character['Name']}.\"")
    for pokemon in character['Pokemon']:
        pokemon['HP'] = pokemon['Max HP']
    print(f"\nPokémon have been healed!\n")
    print(f"\nMon \"Take care of yourself, {character['Name']}.\"\n")
    input("\nPress Enter to continue.\n")


def event_bush(character):
    if battle.check_for_wild_pokemon():
        foe_pokemon_number = random.randint(1, character['Trainer rank'] * 3)
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
                    input("\nPress Enter to continue.\n")
                    go_home(character)
                    event_continues = False
    input("\nPress Enter to continue.\n")


def event_path(character):
    number = random.randint(1, 100)
    if number <= 10:
        print("\nYou found a 'Potion'!")
        character['Item']['Potion'] += 1
        input("\nPress Enter to continue.\n")
    elif number <= 20:
        print("\nYou found a 'Poke Ball'!")
        character['Item']['Poke Ball'] += 1
        input("\nPress Enter to continue.\n")
    else:
        pass


# invoked by event()
def adventure_preparation(character):
    if character['Trainer rank'] >= 1:
        print(f"\nDr.Nabil \"Hi {character['Name']}!\"")
    else:
        print(f"\nDr.Nabil \"Hi {character['Name']}!",
              "         The outside is full of Pokémon. They sometimes attack you!",
              "         So, you should bring your own Pokémon.",
              "         Now, I give you a Pokémon.",
              "         Which one do you choose?\"", sep="\n")
        input("\nPress Enter to continue.\n")
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
                    battle.append_pokemon(character, int(user_input), 5,
                                          battle.calculate_max_hp(int(user_input), 5))
                    print(f"You've gotten {characters.poke_dex()[int(user_input)]['Name']}!\n")
                    make_decision = True
                else:
                    continue
            else:
                print("\nYou're choice is not valid. Please try it again.\n")
        input("\nPress Enter to continue.\n")
        print(f"\nDr.Nabil \"Take these, too.\"")
        character['Item']['Potion'] = 3
        print(f"You've gotten three 'Potion'!")
        character['Item']['Poke Ball'] = 5
        print(f"You've gotten five 'Poke Ball'!")
        print(f"\nDr.Nabil \"You can use 'Potion' to heal your Pokémon.",
              f"         'Poke Ball' is used to catch wild Pokémon during battle.",
              f"         However, to catch a Pokémon for sure, you need to weaken it before throwing a Poké Ball\"\n",
              sep="\n")
        input("Press Enter to continue...\n")
        print(f"\nDr.Nabil \"Now, you're ready to go on an adventure!\"\n",
              f"         \"To go to BCIT Pokémon Gym, you should pass through Lion Gate Bridge.\"\n",
              f"         \"The construction worker at the bridge wouldn't let you pass through unless you have at least "
              f"three Pokémon with you.\"\n")
        input("\nPress Enter to continue.\n")
        character['Trainer rank'] = 1
        print(f"Your trainer rank has increased to {character['Trainer rank']}!")
        character['Next goal'] = "Let's catch two more Pokémon and go to Lion Gate Bridge!"
        print(f"\nYour next goal has been updated to '{character['Next goal']}'!\n")
        input("\nPress Enter to continue.\n")


def lonsdale_quay(character):
    print("\n\"Here is 'Lonsdale Quay', the north shore terminal of 'SeaBus'.\"")
    if 'SeaBus Ticket' in character['Item']:
        print("Clerk at the gate \"Welcome to SeaBus!\"",
              "                \"The SeaBus is departing soon. Come on, get on board!\"\n")
        input("\nPress Enter to continue.\n")
        character["Location"] = (14, 14)
    else:
        print("Clerk at the gate \"Sorry, the SeaBus is out of service, now.\"\n")
        input("\nPress Enter to continue.\n")


def lion_gate_bridge(character):
    if character['Trainer rank'] >= 2:
        print(f"\nConstruction Worker Sam \"Hi {character['Name']}!\"")
        input("\nPress Enter to continue.\n")
    elif len(character['Pokemon']) < 3:
        print(f"\nConstruction Worker Sam \"Sorry, you cannot proceed unless you have at least three Pokémon with "
              f"you.\"")
        input("\nPress Enter to continue.\n")
        character["Location"] = (5, 8)
    else:
        print(f"\nConstruction Worker Sam \"If you can defeat me, I'll let you pass through this way!\"")
        sam = {'Name': 'Construction Worker Sam',
               'Pokemon': [battle.generate_pokemon(5, 7),
                           battle.generate_pokemon(6, 8)]}
        win_battle = battle.battle_with_trainer(character, sam)
        if win_battle:
            print("\nConstruction Worker Sam \"Passable!\n",
                  "                      Now, you can go to BCIT Pokémon Gym!\n",
                  "                     The Gym Leader there is tough,"
                  " and won't accept a challenge unless you have six Pokémon with you.\n",
                  "                     Make sure to train enough before you go.\"\n")
            input("Press Enter to continue.\n")
            print(f"Construction Worker Sam \"Take this, too.\"")
            character['Item']['SeaBus Ticket'] = 1
            print(f"\nYou've gotten 'SeaBus Ticket'!")
            input("\nPress Enter to continue.\n")
            print(f"\nConstruction Worker Sam \"With this ticket, you can take SeaBus for free as many times as you "
                  f"want.\n")
            print(f"               If you hop on the SeaBus, it's a quick trip between Waterfront and Lonsdale "
                  f"Quay.\"\n")
            input("Press Enter to continue.\n")
            character['Trainer rank'] = 2
            print(f"Your trainer rank has increased to {character['Trainer rank']}!\n",
                  f"the variety of Pokémon appearing in the tall grass has increased!\n")
            character["Next goal"] = "Let's go to BCIT Pokémon Gym!"
            print(f"Your next goal has been updated to '{character['Next goal']}'!\n")
            input("Press Enter to continue.\n")
        else:
            go_home(character)


def mount_cypress(character):
    print("\nGate keeper \"Here is 'Cypress Mountain', where top Pokémon trainers gather.")
    if 'BCIT Gym Badge' in character['Item']:
        print(f"        You can proceed pass through the gate.\"\n")
        input("\nPress Enter to continue.\n")
    else:
        print(f"        For now, you cannot proceed further.\"\n")
        print(f"        Come back after you've gotten 'BCIT Gym Badge'.\"\n")
        input("\nPress Enter to continue.\n")
        character["Location"] = (1, 5)


def waterfront(character):
    print("\n\"Here is 'Waterfront', the south shore terminal of 'SeaBus'.\"")
    if 'SeaBus Ticket' in character['Item']:
        print("Clerk at the gate \"Welcome to SeaBus!\"",
              "                \"The SeaBus is departing soon. Come on, get on board!\"\n")
        input("\nPress Enter to continue.\n")
        character["Location"] = (14, 6)
    else:
        print("Clerk at the gate \"Sorry, the SeaBus is out of service, now.\"\n")
        input("\nPress Enter to continue.\n")


def bcit_pokemon_gym(character):
    if 'BCIT Gym Badge' in character['Item']:
        print(f"\nGym Leader Rahul \"Hey {character['Name']}, how are you doing?\"")
        input("\nPress Enter to continue.\n")
    elif len(character['Pokemon']) < 6:
        print(f"\nReceptionist \"You need to have six Pokémon with you to challenge the Gym Leader.\"")
        input("\nPress Enter to continue.\n")
    else:
        print(f"\nGym Leader Rahul \"Welcome to the BCIT Pokémon Gym. I'm Rahul, the Gym Leader.\"",
              f"                \"If you can defeat me, I'll give you a Gym Badge. Let's battle!\"")
        rahul = {'Name': 'Gym Leader Rahul',
                 'Pokemon': [battle.generate_pokemon(11, 12),
                             battle.generate_pokemon(10, 12),
                             battle.generate_pokemon(9, 14)]}
        win_battle = battle.battle_with_trainer(character, rahul)
        if win_battle:
            print("\nGym Leader Rahul \"I'm totally defeated. Please take this Gym Badge.\"")
            print(f"\nYou've gotten 'BCIT Gym Badge'!")
            character['Item']['BCIT Gym Badge'] = 1
            input("\nPress Enter to continue.\n")
            print(f"\nGym Leader Rahul \"With this Gym Badge, you can go to all the places on the map.\"")
            print(f"               \"Good luck, young Pokémon trainer!\"\n")
            input("\nPress Enter to continue.\n")
            character['Trainer rank'] = 3
            print(f"\nYour trainer rank has increased to {character['Trainer rank']}!")
            print(f"\nthe variety of Pokémon appearing in the tall grass has increased!")
            character['Next goal'] = "Let's explore this world, and eventually go to Cypress Mountain!"
            print(f"\nYour next goal has been updated to '{character['Next goal']}'!\n")
            input("\nPress Enter to continue.\n")
        else:
            go_home(character)


def science_world(character):
    print("\n\"Here is 'Science World'. Everyone can enjoy science here.\"\n")
    if ['BCIT Gym Badge'] not in character['Item']:
        print(f"\nConstruction Worker \"Sorry, you cannot proceed further unless you have 'BCIT Gym Badge'.\"\n")
        character["Location"] = (19, 17)


def burrard_street_bridge(character):
    print("\n\"Here is 'Burrard Street Bridge'. The oldest bridge in Vancouver, boasting a history of 100 years.\"")
    if ['BCIT Gym Badge'] not in character['Item']:
        print(f"\nConstruction Worker \"Sorry, you cannot proceed further unless you have 'BCIT Gym Badge'.\"\n")
        character["Location"] = (12, 19)


def granville_island(character):
    print("\n\"Here is 'Granville Island'. You can enjoy shopping here.\"\n")
    if ['BCIT Gym Badge'] not in character['Item']:
        print(f"\nConstruction Worker \"Sorry, you cannot proceed further unless you have 'BCIT Gym Badge'.\"\n")
        character["Location"] = (15, 20)


def cypress_top(character):
    print("\nTats \"Hi, I'm Tats. I'm the strongest Pokémon trainer in Vancouver.\"",
          "      \"You made it here, impressive. Let's battle right away!\"")
    tats = {'Name': 'Tats',
            'Pokemon': [battle.generate_pokemon(12, 24),
                        battle.generate_pokemon(13, 26),
                        battle.generate_pokemon(14, 28),
                        battle.generate_pokemon(15, 30),
                        battle.generate_pokemon(16, 36),
                        battle.generate_pokemon(17, 40)]}
    win_battle = battle.battle_with_trainer(character, tats)
    if win_battle:
        print("\nTats \"Unbelievable! Thank you so much for playing!\"")
        input("\nPress Enter to continue.\n")
        if character['Trainer rank'] <= 3:
            character['Trainer rank'] = 4
            print(f"\nYour trainer rank has increased to {character['Trainer rank']}!")
            character['Next goal'] = "You've completed the game! Congratulations!"
            print(f"\nYour next goal has been updated to '{character['Next goal']}'!\n")
            input("\nPress Enter to continue.\n")
    else:
        go_home(character)
