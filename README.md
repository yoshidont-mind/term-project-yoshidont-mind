[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ECKgeadS)
# COMP-1510-202330-Term-Project

Every program needs a README.md

This is written in markdown. Read about markdown here: [markdowncheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Your name:

Tatsuya Yoshida

## Your student number:

A01361712

## Your GitHub username:

yoshidont-mind

## Any important comments you'd like to make about your work:

For commits prior to 'COPY code from pokemon-in-vancouver!', please refer to the other repository (pokemon-in-vancouver).
https://github.com/yoshidont-mind/pokemon-in-vancouver

## About this game:

### __0. Overview：__
I grew up with Pokémon. I still remember, as if it were yesterday,
how excited I was when I got my first Pokémon game for Christmas when I was six years old.

Driven by the thought, "How it would be fun if there were Pokémon in Vancouver!" I created this game. Once the game 
starts, please enter "5" to open the map and take a look.

![map_in_this_game](images/map_in_this_game.png)

The top-left of the map corresponds to Cypress Mountain, bottom-left to UBC, bottom-right to Mount Pleasant, and 
top-right to Deep Cove. The symbols on the map have the following meanings:
- "#": Obstacle (impassable)
- "@": Sea (impassable)
- ".": Bush (wild Pokémon randomly appear)
- " ": Road (items are sometimes found)
- "i": Information board
- "!": Events occur
- "H": Home (Pokémon get healed)

Doesn't it somewhat resemble a map of the Vancouver area?

The player starts from their home in North Vancouver, catches and raises Pokémon, and goes through some events, 
aiming for the BCIT Pokémon Gym. Your goal is to defeat the Gym Leader, to earn the Gym Badge. <br> <br> 

### __1. How the Game Progresses:__
At the beginning of each iteration, the map around the character is displayed, and the player chooses an action. <br> <br>  

#### __1-1. Players' options：__
- 1 ~ 4: Move up, down, left, or right
- 5: Open map 
  - You can see the entire game map.
- 6: Check status 
  - You can check your Trainer rank, Next goal, list of items, and list of Pokémon.
- 7: Heal Pokémon 
  - Select one Pokémon from your list and use a Potion to fully restore its HP.
- 8: Change Pokémon order 
  - Select one Pokémon from your list to swap with the one at the top of the list.
- 9: Escape Pokémon 
  - Select one Pokémon from your list to release it.
- 0: Save game and quit 
  - Save your data and exit the game.

#### __1-2. Event Occurrence:__
When character moves, events corresponding to the new location occur. <br> <br> 
#### __1-3. When events end:__
Once an event ends, the map around the character is displayed again, and the player chooses an action. <br> <br> 
#### __1-4. To complete the game:__
While the character aims for the BCIT Pokémon Gym and clear events, the trainer rank increases and the Next goal 
changes accordingly. Finally, when you defeat the Gym Leader and get the Gym Badge, the Trainer rank reaches 3, 
and the game gracefully ends.
However, you know what? the Trainer rank actually can be up to 4, and you can revoke the game to enjoy the rest of the 
story!
(Of course, if you are interested.(Please say yes..!)) <br> <br> 

### __2. Some other things to note:__
#### __Battle with wild Pokémon__
When the character enters a bush, a wild Pokémon randomly appears and a battle starts. The character can choose from 
the following actions each turn:
- 1: Attack 
  - Your Pokémon and then the wild Pokémon attack in turn. 
  - Damage is calculated based on each one's attack and defense, and HP is reduced accordingly.
- 2: See Pokémon 
  - Check the remaining HP of all your Pokémon.
- 3: Catch Pokémon 
  - You can throw a Poké Ball to catch the wild Pokémon.
  - The more weakened the wild Pokémon has been, the higher the chance of capturing it.
  - If the capture fails, the opponent Pokémon attacks yours.
- 4: Run 
  - The stronger the opponent Pokémon, the lower the chance of escaping. 
  - If you fail to escape, the opponent Pokémon attacks yours.  <br> 
  
The battle ends when you defeat or capture the wild Pokémon, or successfully run away. <br>  <br> 

#### __Battle with Pokémon trainer__
At some places with "!", you might battle Pokémon trainers. Trainers will send out several Pokémon in 
succession. Defeating all of them ends the battle. <br> <br> 

#### __What happens when you lose a battle__
If all your Pokémon are defeated in battle, the battle ends. In this case, you are returned to your home and lose 
all your Potions and Poké Balls. <br> <br> 

That's all for now. I hope you enjoy the game!
























