"""
This module contains functions that are invoked when the player moves to a specific location.
"""
import random
import time

import battle
import characters


def event(character):
    """
    Invoke an event function according to the character's location.

    :param character: a dictionary that contains the player's information
    :precondition: character must be a dictionary that represents the character
    :precondition: the letter on the map corresponding to the character's location must be "!"
    :postcondition: the function corresponding to the character's location is correctly invoked
    """
    event_dic = {
        (17, 4): adventure_preparation,
        (14, 6): lonsdale_quay,
        (5, 9): lion_gate_bridge,
        (1, 4): mount_cypress,
        (14, 14): waterfront,
        (14, 16): bcit_pokemon_gym,
        (19, 18): science_world,
        (12, 20): burrard_street_bridge,
        (15, 21): granville_island,
        (1, 1): cypress_top
    }
    event_function = event_dic.get(character['Location'])
    if event_function:
        event_function(character)


def event_information(character, user_choice):
    """
    Print information about the location.

    Some information is printed only when the player visits the location from a specific direction.

    :param character: a dictionary that represents the character
    :param user_choice: a string which is either of "1", "2", "3", or "4"
    :precondition: character must be a dictionary that represents the character
    :precondition: user_choice must be either of "1", "2", "3", or "4"
    :postcondition: information about the location is correctly printed when the condition is met
    """
    location_information = {
        (5, 8): "\n\"Here is 'Lion Gate Bridge'. The gateway to the world.\"\n",
        (12, 4): "\n\"Here is 'Grouse Mountain'. Be careful for strong Pokémon.\"\n" if user_choice == "1" else None,
        (5, 10): "\n\"Here is 'Stanley Park'. Many Pokémon are living here.\"\n" if user_choice == "2" else None,
        (16, 17): "\n\"Here is 'BC Place'. Winter Olympic was held here in 2010.\"\n"
    }

    info = location_information.get(character['Location'])
    if info:
        print(info)
        input("Press Enter to continue.\n")


# events > events
def event_home(character):
    """
    Execute an event when the player visits home.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the letter on the map corresponding to the character's location must be "H"
    :postcondition: the event is correctly executed
    :postcondition: the player's Pokémon are healed
    :postcondition: the player is asked to press Enter
    """
    print(f"\nMom \"Welcome home, {character['Name']}.\n",
          f"        You look tired. Take a rest.\"\n")
    time.sleep(1)
    if character['Pokemon']:
        for pokemon in character['Pokemon']:
            pokemon['HP'] = pokemon['Max HP']
        print(f"Pokémon have been healed!\n")
    print(f"Mon \"Take care of yourself, {character['Name']}.\"\n")
    input("Press Enter to continue.\n")


def go_home(character):
    """
    Execute an event when the player loses a battle.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the player must lose a battle
    :postcondition: the event is correctly executed
    :postcondition: the player's Potion and Poké Ball are lost
    :postcondition: the player's location is changed to (15, 1)
    :postcondition: the player's Pokémon are healed
    :postcondition: the player is asked to press Enter
    """
    input("Press Enter to continue.\n")
    print(f"You lost your items being shocked...")
    character['Item']['Potion'] = 0
    character['Item']['Poke Ball'] = 0
    print(f"You rush your home...\n")
    time.sleep(1)
    character['Location'] = (15, 1)
    print(f"\nMon \"Take care of yourself, {character['Name']}.\"\n")
    for pokemon in character['Pokemon']:
        pokemon['HP'] = pokemon['Max HP']
    print(f"Pokémon have been healed!\n")
    print(f"Mon \"Take care of yourself, {character['Name']}.\"\n")
    input("Press Enter to continue.\n")


def check_for_wild_pokemon():
    """
    Determine whether the player encounters a wild Pokémon.

    :precondition: the character must be in a bush
    :precondition: event_bush() must be invoked
    :postcondition: whether the player encounters a wild Pokémon is correctly determined
    :return: a boolean value that represents whether the player encounters a wild Pokémon
    """
    random_number = random.randint(1, 100)
    if random_number <= 25:
        return True
    else:
        return False


def event_bush(character):
    """
    Execute an event when the player visits a bush.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the letter on the map corresponding to the character's location must be "."
    :postcondition: the event is correctly executed
    :postcondition: whether the player encounters a wild Pokémon is correctly determined
    :postcondition: whether the player lost a battle is correctly determined if the player encounters a wild Pokémon
    :postcondition: go_home() is correctly invoked if the player loses a battle
    :postcondition: the player is asked to press Enter if the player encounters a wild Pokémon and don't lose
    """
    if check_for_wild_pokemon():
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
                input("Press Enter to continue.\n")
            else:
                if not battle.check_alive_pokemon_remains(character):
                    print(f"\nAll of your Pokémon are defeated!\n")
                    go_home(character)
                    event_continues = False


def event_path(character):
    """
    Execute an event when the player visits a path.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the letter on the map corresponding to the character's location must be " "
    :postcondition: the event is correctly executed
    :postcondition: whether the character finds a Potion is correctly determined
    :postcondition: number of is incremented by 1 if the character finds a Potion
    :postcondition: whether the character finds a Poké Ball is correctly determined
    :postcondition: number of is incremented by 1 if the character finds a Poké Ball
    """
    number = random.randint(1, 100)
    if number <= 10:
        print("\nYou found a 'Potion'!\n")
        character['Item']['Potion'] += 1
    elif number <= 20:
        print("\nYou found a 'Poke Ball'!\n")
        character['Item']['Poke Ball'] += 1
    else:
        pass


"""
following functions are invoked by event()
"""


def gather_user_choice_for_fist_pokemon():
    """
    Gather user's choice for the first Pokémon.

    Keep asking the user for the choice until the user enters a valid choice.
    :postcondition: the user's choice is correctly gathered
    :return: a string which is either of "1", "2", "3", or "4"
    """
    numbers_expected = ["1", "2", "3", "4"]
    while True:
        print("Here are four Pokémon:\n1) Bulbasaur\n2) Charmander\n3) Squirtle\n4) Pikachu\n")
        user_input = input("Please enter your choice:\n")
        if user_input in numbers_expected:
            pokemon_ascii_art = characters.poke_dex()[int(user_input)]['Ascii art']
            print(pokemon_ascii_art)
            print(f"Are you sure to choose {characters.poke_dex()[int(user_input)]['Name']}?")
            print("1) Yes 2) No\n")
            user_confirm = input("Please enter your choice:\n")
            if user_confirm == "1":
                return user_input
            else:
                continue
        else:
            print("\nYou're choice is not valid. Please try it again.\n")


def adventure_preparation(character):
    """
    Execute an event when the player visits the entrance of the town.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (17, 4)
    :precondition: the trainer rank of the character must be 0
    :postcondition: the event is correctly executed
    :postcondition: if trainer rank of the character is 0, the first Pokémon the user chooses is correctly appended to
    the
    character's Pokémon
    :postcondition: if trainer rank of the character is 0, number of thc character's Potion is correctly incremented
    by 3
    :postcondition: if trainer rank of the character is 0, number of thc character's Poké Ball is correctly
    incremented by 5
    :postcondition: if trainer rank of the character is 0, the trainer rank of the character is incremented to 1
    :postcondition: if trainer rank of the character is 0, the next goal of the character has changed to "Let's
    catch two more Pokémon and go to Lion Gate"
    :postcondition: if trainer rank of the character is 1 or bigger, a message from Dr.Nabil is correctly printed
    :postcondition: the player is asked to press Enter
    """
    if character['Trainer rank'] >= 1:
        print(f"\nDr.Nabil \"Hi {character['Name']}!\"\n")
    else:
        print(f"\nDr.Nabil \"Hi {character['Name']}!\n",
              "         The outside of the town is full of Pokémon. They sometimes attack you!\n",
              "         So, you should bring your own Pokémon.\n",
              "         Now, I give you a Pokémon. Which one do you choose?\"\n")
        input("Press Enter to continue.\n")
        chosen_pokemon = gather_user_choice_for_fist_pokemon()
        print(f"\nDr.Chris \"Good choice! {character['Name']}!\"")
        battle.append_pokemon(character, int(chosen_pokemon), 5,
                              battle.calculate_max_hp(int(chosen_pokemon), 5))
        print(f"You've gotten {characters.poke_dex()[int(chosen_pokemon)]['Name']}!\n")
        input("Press Enter to continue.\n")
        print(f"Dr.Nabil \"Take these, too.\"\n")
        character['Item']['Potion'] = 3
        print(f"You've gotten three 'Potion'!")
        character['Item']['Poke Ball'] = 5
        print(f"You've gotten five 'Poke Ball'!\n")
        print(f"Dr.Nabil \"You can use 'Potion' to heal your Pokémon.\n",
              f"         'Poke Ball' is used to catch wild Pokémon during battle.\n",
              f"         However, to catch a Pokémon for sure, you need to weaken it before throwing a Poké Ball\"\n")
        input("Press Enter to continue...\n")
        print(f"Dr.Nabil \"Now, you're ready to go on an adventure!\"\n",
              f"         \"To go to BCIT Pokémon Gym, you should pass through Lion Gate Bridge.\"\n",
              f"         \"The construction worker at the bridge wouldn't let you pass through unless you have at least"
              f" three Pokémon with you.\"\n")
        input("Press Enter to continue.\n")
        character['Trainer rank'] = 1
        print(f"Your trainer rank has increased to {character['Trainer rank']}!")
        character['Next goal'] = "Let's catch two more Pokémon and go to Lion Gate Bridge!"
        print(f"Your next goal has been updated to '{character['Next goal']}'!\n")
        input("Press Enter to continue.\n")


def lonsdale_quay(character):
    """
    Execute an event when the player visits Lonsdale Quay.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (14, 6)
    :postcondition: the event is correctly executed
    :postcondition: if the character has SeaBus Ticket, the location of the character is changed to (14, 14)
    :postcondition: if the character has not SeaBus Ticket, a message from the clerk is correctly printed
    :postcondition: the player is asked to press Enter
    """
    print("\n\"Here is 'Lonsdale Quay', the north shore terminal of 'SeaBus'.\"\n")
    if 'SeaBus Ticket' in character['Item']:
        print("Clerk at the gate \"Welcome to SeaBus!\"\n",
              "                \"The SeaBus is departing soon. Come on, get on board!\"\n")
        time.sleep(2)
        character["Location"] = (14, 14)
        print("Announcement \"The SeaBus arrived at Waterfront.\"\n")
    else:
        print("Clerk at the gate \"Sorry, the SeaBus is out of service, now.\"\n")
    input("Press Enter to continue.\n")


def lion_gate_bridge(character):
    """
    Execute an event when the player visits Lion Gate Bridge.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (5, 9)
    :postcondition: the event is correctly executed
    :postcondition: if the character's trainer rank is 2 or bigger, the message from the construction worker is
    correctly printed
    :postcondition: if the character's trainer rank is less than 2 and the character has less than 3 Pokémon, the
    location of the character is changed to (5, 8)
    :postcondition: if the character's trainer rank is less than 2 and the character has 3 or more Pokémon, whether
    the character wins a battle with the construction worker is correctly determined
    :postcondition: if the character wins a battle with the construction worker, SeaBus Ticket is correctly appended
    to the character's item
    :postcondition: if the character wins a battle with the construction worker, the character's trainer rank is
    correctly incremented to 2
    :postcondition: if the character wins a battle with the construction worker, the character's next goal is correctly
    updated to "Let's go to BCIT Pokémon Gym!"
    :postcondition: if the character loses a battle with the construction worker, go_home() is correctly invoked
    """
    if character['Trainer rank'] >= 2:
        print(f"\nConstruction Worker Sam \"Hi {character['Name']}!\"\n")
    elif len(character['Pokemon']) < 3:
        print(f"\nConstruction Worker Sam \"Sorry, you cannot proceed unless you have at least three Pokémon with "
              f"you.\"\n")
        input("Press Enter to continue.\n")
        character["Location"] = (5, 8)
    else:
        print(f"\nConstruction Worker Sam \"If you can defeat me, I'll let you pass through this way!\"")
        sam = {'Name': 'Construction Worker Sam',
               'Pokemon': [battle.generate_pokemon(5, 7),
                           battle.generate_pokemon(6, 8)]}
        win_battle = battle.battle_with_trainer(character, sam)
        if win_battle:
            print("\nConstruction Worker Sam \"Passable! Now, you can go to BCIT Pokémon Gym!\n",
                  "                     The Gym Leader there is tough,"
                  " and won't accept a challenge unless you bring five or more Pokémon with you.\n",
                  "                     Make sure to train enough before you go.\"\n")
            input("Press Enter to continue.\n")
            print(f"Construction Worker Sam \"Take this, too.\"\n")
            character['Item']['SeaBus Ticket'] = 1
            print(f"You've gotten 'SeaBus Ticket'!\n")
            input("Press Enter to continue.\n")
            print(f"Construction Worker Sam \"With this ticket, you can take SeaBus for free as many times as you "
                  f"want.\n",
                  f"                        If you hop on the SeaBus, it's a quick trip between Waterfront and Lonsdale"
                  f" Quay.\"\n")
            input("Press Enter to continue.\n")
            character['Trainer rank'] = 2
            character["Next goal"] = "Let's go to BCIT Pokémon Gym!"
            print(f"Your trainer rank has increased to {character['Trainer rank']}!\n",
                  f"The variety of Pokémon appearing in the bush has increased!\n",
                  f"Your next goal has been updated to '{character['Next goal']}'!\n", sep="")
            input("Press Enter to continue.\n")
        else:
            go_home(character)


def mount_cypress(character):
    """
    Execute an event when the player visits Mount Cypress.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (1, 4)
    :postcondition: the event is correctly executed
    :postcondition: if the character has BCIT Gym Badge, the message from the gatekeeper is correctly printed
    :postcondition: if the character has not BCIT Gym Badge, the location of the character is changed to (1, 5)
    :postcondition: the player is asked to press Enter
    """
    print("\nGatekeeper \"Here is 'Cypress Mountain', where top Pokémon trainers gather.")
    if 'BCIT Gym Badge' in character['Item']:
        print(f"            You can proceed pass through the gate.\"\n")
    else:
        print(f"        For now, you cannot proceed further.\"\n")
        print(f"        Come back after you've gotten 'BCIT Gym Badge'.\"\n")
        character["Location"] = (1, 5)
    input("Press Enter to continue.\n")


def waterfront(character):
    """
    Execute an event when the player visits Waterfront.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (14, 14)
    :postcondition: the event is correctly executed
    :postcondition: if the character has SeaBus Ticket, the location of the character is changed to (14, 6)
    :postcondition: if the character has not SeaBus Ticket, a message from the clerk is correctly printed
    :postcondition: the player is asked to press Enter
    """
    print("\n\"Here is 'Waterfront', the south shore terminal of 'SeaBus'.\"\n")
    if 'SeaBus Ticket' in character['Item']:
        print("Clerk at the gate \"Welcome to SeaBus!\"\n",
              "                \"The SeaBus is departing soon. Come on, get on board!\"\n")
        character["Location"] = (14, 6)
        time.sleep(2)
        print("Announcement \"The SeaBus arrived at Lonsdale Quay.\"\n")
    else:
        print("Clerk at the gate \"Sorry, the SeaBus is out of service, now.\"\n")
    input("Press Enter to continue.\n")


def bcit_pokemon_gym(character):
    """
    Execute an event when the player visits BCIT Pokémon Gym.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (14, 16)
    :postcondition: the event is correctly executed
    :postcondition: if the character has BCIT Gym Badge, the message from the gym leader is correctly printed
    :postcondition: if the character has not BCIT Gym Badge and the character has less than 5 Pokémon, a message from
    the receptionist is correctly printed
    :postcondition: if the character has not BCIT Gym Badge and the character has 5 or more Pokémon, whether the
    character wins a battle with the gym leader is correctly determined
    :postcondition: if the character wins a battle with the gym leader, BCIT Gym Badge is correctly appended to the
    character's item
    :postcondition: if the character wins a battle with the gym leader, the character's trainer rank is correctly
    incremented to 3
    :postcondition: if the character wins a battle with the gym leader, the character's next goal is correctly updated
    to "Let's explore this world, and eventually go to Cypress Mountain!"
    :postcondition: if the character loses a battle with the gym leader, go_home() is correctly invoked
    """
    if 'BCIT Gym Badge' in character['Item']:
        print(f"\nGym Leader Rahul \"Hey {character['Name']}, how are you doing?\"\n")
    elif len(character['Pokemon']) < 5:
        print(f"\nReceptionist \"You need to bring at least five Pokémon with you to challenge the Gym Leader.\"\n")
        input("Press Enter to continue.\n")
    else:
        print(f"\nGym Leader Rahul \"Welcome to the BCIT Pokémon Gym. I'm Rahul, the Gym Leader.\n",
              f"                If you can defeat me, I'll give you a Gym Badge. Let's battle!\"\n")
        rahul = {'Name': 'Gym Leader Rahul',
                 'Pokemon': [battle.generate_pokemon(11, 10),
                             battle.generate_pokemon(10, 10),
                             battle.generate_pokemon(9, 12)]}
        win_battle = battle.battle_with_trainer(character, rahul)
        if win_battle:
            print("Gym Leader Rahul \"I'm totally defeated. Please take this Gym Badge.\"\n")
            print(f"You've gotten 'BCIT Gym Badge'!\n")
            character['Item']['BCIT Gym Badge'] = 1
            input("Press Enter to continue.\n")
            print(f"Gym Leader Rahul \"With this Gym Badge, you can go to all the places on the map.\"\n",
                  f"               \"Good luck, young Pokémon trainer!\"\n")
            input("Press Enter to continue.\n")
            character['Trainer rank'] = 3
            character['Next goal'] = "Let's explore this world, and eventually go to Cypress Mountain!"
            print(f"Your trainer rank has increased to {character['Trainer rank']}!\n",
                  f"The variety of Pokémon appearing in the bush has increased!\n",
                  f"Your next goal has been updated to '{character['Next goal']}'!\n", sep="")
            input("Press Enter to continue.\n")
        else:
            go_home(character)


def science_world(character):
    """
    Execute an event when the player visits Science World.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (19, 18)
    :postcondition: the event is correctly executed
    :postcondition: if the character has BCIT Gym Badge, the information about Science World is correctly printed
    :postcondition: if the character has not BCIT Gym Badge, the location of the character is changed to (19, 17)
    :postcondition: if the character has not BCIT Gym Badge, the player is asked to press Enter
    """
    print("\n\"Here is 'Science World'. Everyone can enjoy science here.\"\n")
    if 'BCIT Gym Badge' not in character['Item']:
        print(f"Construction Worker \"Sorry, you cannot proceed further unless you have 'BCIT Gym Badge'.\"\n")
        character["Location"] = (19, 17)
        input("Press Enter to continue.\n")


def burrard_street_bridge(character):
    """
    Execute an event when the player visits Burrard Street Bridge.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (12, 20)
    :postcondition: the event is correctly executed
    :postcondition: if the character has BCIT Gym Badge, the information about Burrard Street Bridge is correctly
    :postcondition: if the character has not BCIT Gym Badge, the location of the character is changed to (12, 19)
    :postcondition: if the character has not BCIT Gym Badge, the player is asked to press Enter
    """
    print("\n\"Here is 'Burrard Street Bridge'. The oldest bridge in Vancouver, boasting a history of 100 years.\"\n")
    if 'BCIT Gym Badge' not in character['Item']:
        print(f"Construction Worker \"Sorry, you cannot proceed further unless you have 'BCIT Gym Badge'.\"\n")
        character["Location"] = (12, 19)
        input("Press Enter to continue.\n")


def granville_island(character):
    """
    Execute an event when the player visits Granville Island.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (15, 21)
    :postcondition: the event is correctly executed
    :postcondition: if the character has BCIT Gym Badge, the information about Granville Island is correctly printed
    :postcondition: if the character has not BCIT Gym Badge, the location of the character is changed to (15, 20)
    :postcondition: if the character has not BCIT Gym Badge, the player is asked to press Enter
    """
    print("\n\"Here is 'Granville Island'. You can enjoy shopping here.\"\n")
    if 'BCIT Gym Badge' not in character['Item']:
        print(f"Construction Worker \"Sorry, you cannot proceed further unless you have 'BCIT Gym Badge'.\"\n")
        character["Location"] = (15, 20)
        input("Press Enter to continue.\n")


def cypress_top(character):
    """
    Execute an event when the player visits the top of Cypress Mountain.

    :param character: a dictionary that represents the character
    :precondition: character must be a dictionary that represents the character
    :precondition: the location of the character must be (1, 1)
    :postcondition: the event is correctly executed
    :postcondition: whether the character wins a battle with Tats is correctly determined
    :postcondition: if the character wins a battle with Tats, the character's trainer rank is correctly incremented to 4
    :postcondition: if the character wins a battle with Tats, the character's next goal is correctly updated to
    "You've completed the game! Congratulations! Thank you so much for playing!"
    :postcondition: if the character wins a battle with Tats, the player is asked to press Enter
    :postcondition: if the character wins a battle with Tats, characters.print_thank_you_for_playing() is correctly
    invoked
    :postcondition: if the character loses a battle with Tats, go_home() is correctly invoked
    """
    print("\nTats \"Hi, I'm Tats. I'm the strongest Pokémon trainer in Vancouver.\n",
          "      You made it here, impressive. Let's battle right away!\"")
    tats = {'Name': 'Tats',
            'Pokemon': [battle.generate_pokemon(12, 12),
                        battle.generate_pokemon(13, 12),
                        battle.generate_pokemon(14, 14),
                        battle.generate_pokemon(15, 14),
                        battle.generate_pokemon(16, 16),
                        battle.generate_pokemon(17, 18)]}
    win_battle = battle.battle_with_trainer(character, tats)
    if win_battle:
        print("\nTats \"Unbelievable! The world of Pokémon is still full of mysteries. Continue enjoying your "
              "adventure!\"\n")
        input("Press Enter to continue.\n")
        if character['Trainer rank'] <= 3:
            character['Trainer rank'] = 4
            character['Next goal'] = "You've completed the game! Congratulations! Thank you so much for playing!"
            print(f"\nYour trainer rank has increased to {character['Trainer rank']}!\n",
                  f"The variety of Pokémon appearing in the bush has increased!\n",
                  f"\nYour next goal has been updated to '{character['Next goal']}'!\n", sep="")
            characters.print_thank_you_for_playing()
            input("Press Enter to continue.\n")
    else:
        go_home(character)
