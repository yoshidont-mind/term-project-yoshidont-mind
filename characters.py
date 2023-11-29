"""
This module contains poke_dex() function which is used to store information of Pokémon.
"""


def poke_dex():
    pokemon_dic = {1: {'Name': 'Bulbasaur', 'HP': 45, 'Attack': 49, 'Defense': 49},
                   2: {'Name': 'Charmander', 'HP': 39, 'Attack': 52, 'Defense': 43},
                   3: {'Name': 'Squirtle', 'HP': 44, 'Attack': 48, 'Defense': 65},
                   4: {'Name': 'Pikachu', 'HP': 35, 'Attack': 55, 'Defense': 30},
                   5: {'Name': 'Eevee', 'HP': 55, 'Attack': 55, 'Defense': 50},
                   6: {'Name': 'Psyduck', 'HP': 50, 'Attack': 52, 'Defense': 48},
                   7: {'Name': 'Chikorita', 'HP': 45, 'Attack': 49, 'Defense': 65},
                   8: {'Name': 'Jigglypuff', 'HP': 115, 'Attack': 45, 'Defense': 20},
                   9: {'Name': 'Polygon', 'HP': 65, 'Attack': 60, 'Defense': 70},
                   10: {'Name': 'Chameleon', 'HP': 58, 'Attack': 64, 'Defense': 58},
                   11: {'Name': 'Rowlet', 'HP': 68, 'Attack': 55, 'Defense': 55},
                   12: {'Name': 'Raichu', 'HP': 60, 'Attack': 90, 'Defense': 55},
                   13: {'Name': 'Eifie', 'HP': 65, 'Attack': 65, 'Defense': 60},
                   14: {'Name': 'Lapras', 'HP': 130, 'Attack': 85, 'Defense': 80},
                   15: {'Name': 'Snorlax', 'HP': 160, 'Attack': 110, 'Defense': 65},
                   16: {'Name': 'Charizard', 'HP': 78, 'Attack': 84, 'Defense': 78},
                   17: {'Name': 'Mew', 'HP': 100, 'Attack': 100, 'Defense': 100},
                   }

    pokemon_dic[1]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠈⡖⡤⠄⠀
⠀⠀⢀⡀⠀⠀⠀⡐⠁⠀⠀⠠⠐⠂⠀⠁⠀⠀⠀⠀
⠀⠰⡁⠐⢉⣉⣭⡍⠁⠂⠉⠘⡀⠀⠀⠀⠀⠂⠡⠀
⢀⣊⠀⡄⠻⠿⠋⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⢀
⡎⣾⠀⠁⣴⡆⠀⠡⢺⣿⣆⠀⢠⢱⣄⠀⠀⠀⠀⠈
⡑⠟⠀⠀⠀⠀⠀⢀⣸⡿⠟⠀⠀⠈⢿⣿⡦⡀⠀⡰
⠙⠔⠦⣤⣥⣤⣤⣤⡤⠆⠀⠀⠀⠀⢀⢀⠀⠈⠎⠀
⠀⠀⠈⣰⡋⢉⠉⠁⠒⠂⢇⢠⡆⠀⠸⢴⣿⠀⠘⠀
⠀⠀⠘⡿⠃⠀⠨⠒⢆⣸⣿⠁⠀⡠⡇⠈⠋⠀⠰⠀
⠀⠀⠀⠛⠒⠒⠁⠀⠈⠷⡤⠤⠐⠀⠘⠒⠒⠖⠁⠀"""
    pokemon_dic[2]['Ascii art'] = """
⠀⠀⠀⣀⠔⠒⠒⠂⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⢅⠀⠀⢀⣤⢄⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⡆⠀⠀⠀⢸⠼⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⢗⠂⠀⠀⡀⠈⢉⠅⠇⠀⠀⠀⠀⠀⠀⢠⣄⠀
⠀⠈⠢⣓⠔⣲⠖⡫⠊⡘⠀⠀⠀⠀⠀⠀⠲⡟⠙⡆
⠀⢀⢀⠠⠘⣇⠖⢄⠀⠉⠐⠠⢄⣀⡀⠀⠜⠀⠀⣁
⠘⣏⣀⣀⣀⠃⠀⠀⠑⣀⣀⣀⣰⠼⠇⠈⠄⠀⠈⡻
⠀⠁⠀⠀⢰⠀⠀⠀⠀⠠⠀⠡⡀⠀⠀⠀⠈⡖⠚⠀
⠀⠀⠀⡠⠘⠀⠀⠀⠀⢀⠆⠀⠐⡀⠀⡠⠊⣠⠀⠀
⠀⠀⢐⠀⠀⠁⡀⠀⠀⢀⠀⠀⠀⢨⠀⡠⡴⠂⠀⠀
⠀⢀⣨⣤⠀⠀⠐⠃⠐⠚⠢⠀⠀⠈⠑⠊⠀⠀⠀⠀
⠀⠘⠓⠋⠉⠁⠀⠀⠀⠀⠀⠓⢶⡾⠗⠀⠀⠀⠀⠀"""
    pokemon_dic[3]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠐⠒⠒⠂⠠⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⡠⢠⠂⠀⠀⠀⠡⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⢰⣷⣾⠀⠀⠀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠜⢨⠢⠔⡀⠀⠠⠘⠛⠛⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⢀⣀⣀⠀⠀⠀⠰⠀⠀⠀⠀⠡⡀⠀⠈⠀⠒⠂⠄⡀⢀⠀⡀⠀
⠀⡴⠊⠀⠀⠀⠉⢆⠀⡔⢣⠀⠀⠀⠀⠐⡤⣀⠀⠀⠀⠀⠀⣀⠄⠀⠀
⢸⠀⠀⠀⢠⠀⠀⠈⣼⠀⠀⠣⠀⠀⠀⡰⡀⠀⠉⠀⠀⠰⠉⠀⠁⠠⢄
⢰⠀⠀⠀⠀⠇⠀⢀⢿⠀⢀⠇⡐⠀⠈⠀⠈⠐⠠⠤⠤⠤⠀⠀⠀⠀⢨
⠀⢓⠤⠤⠊⠀⠀⢸⠀⠣⠀⡰⠁⠀⠀⡀⠀⠀⠀⠸⠀⢰⠁⠐⠂⠈⠁
⠀⠀⠑⢀⠀⠀⠀⠈⣄⠖⠉⠑⢄⠠⠊⠀⠢⢄⣠⣃⣀⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⠠⢀⣀⠎⠀⠀⠀⠈⡄⠀⠀⠀⢠⢃⠠⠃⠐⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⢀⠯⠉⠤⢴⡃⠁⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠰⡁⠀⠀⠀⠠⠂⠀⠀⠀⠀⠑⢄⠀⠀⢀⠲⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠒⠑⠔⠁⠀⠀⠀⠀⠀⠀⠀⠁⠉⠀⠀⠀⠀⠀⠀"""
    pokemon_dic[4]['Ascii art'] = """
⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋"""
    pokemon_dic[5]['Ascii art'] = """
⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠠⣵⡍⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⣖⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣹⣿⣿⡔⡆⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⣀⠀⠀⠀
⠀⠫⡿⣿⣷⣽⡻⠍⠿⠗⢶⡄⡀⠀⡀⠄⣒⣤⣯⣵⣾⢟⡦⠁⠀⠀
⠀⠀⠉⢛⡟⡉⠀⠀⠀⠀⠀⡈⢳⣮⣴⣿⣿⣿⣿⢟⡵⠋⠀⣐⠯⡄
⠀⠀⠀⠸⢃⣤⡴⢂⠐⡈⣐⠠⢈⢹⣛⣿⣯⣭⡼⣭⠠⠔⠊⠁⠀⢣
⠀⠀⠀⣼⢸⣿⡇⠠⠂⠔⣼⣽⡇⣼⠇⣠⠞⣍⠲⠤⢭⡐⢎⠀⠀⠈
⠀⡠⠊⠹⡀⠍⣄⡲⢁⡈⠿⠿⢡⠿⡴⣇⠫⠴⣉⠞⣢⢙⡌⢠⡀⠀
⠠⡅⠀⠀⡨⠒⠤⣄⣩⣁⣦⠵⠊⠀⠈⣯⣗⢧⣍⡚⣤⣋⣼⢳⡓⠀
⠐⢷⡀⡈⠀⠊⠀⠀⠀⠂⠆⢱⠀⠀⢰⠇⢻⡽⣮⡽⢶⣛⣾⠝⠁⠀
⠀⠀⠉⢥⡈⡀⠀⠀⠀⠀⣸⡘⣀⠤⢣⠘⠤⡟⠑⠋⠛⠂⠁⠀⠀⠀
⠀⠀⠀⠀⢷⡲⢄⠀⣀⡴⢏⣹⣥⣾⠁⡊⢥⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣗⠉⢻⠃⡘⢤⣿⣿⣿⡇⠐⡰⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡛⡀⡼⠀⠐⡼⠽⠋⡧⣠⡲⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠁⠘⠲⠎⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    pokemon_dic[6]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣆⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣷⣮⣿⣿⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡠⠒⠉⠀⠀⠀⠀⠀⠀⠈⠁⠲⢖⠒⡀⠀⠀
⠀⠀⠀⡠⠴⣏⠀⢀⡀⠀⢀⡀⠀⠀⠀⡀⠀⠀⡀⠱⡈⢄⠀
⠀⠀⢠⠁⠀⢸⠐⠁⠀⠄⠀⢸⠀⠀⢎⠀⠂⠀⠈⡄⢡⠀⢣
⠀⢀⠂⠀⠀⢸⠈⠢⠤⠤⠐⢁⠄⠒⠢⢁⣂⡐⠊⠀⡄⠀⠸
⠀⡘⠀⠀⠀⢸⠀⢠⠐⠒⠈⠀⠀⠀⠀⠀⠀⠈⢆⠜⠀⠀⢸
⠀⡇⠀⠀⠀⠀⡗⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡄⢀⠎
⠀⢃⠀⠀⠀⢀⠃⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠷⡃⠀
⠀⠈⠢⣤⠀⠈⠀⠀⠑⠠⠤⣀⣀⣀⣀⣀⡀⠤⠒⠁⠀⢡⠀
⡀⣀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠀
⠑⢄⠉⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀
⠀⠀⠑⠢⢱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀
⠀⠀⠀⠀⢀⠠⠓⠢⠤⣀⣀⡀⠀⠀⣀⣀⡀⠤⠒⠑⢄⠀⠀
⠀⠀⠀⠰⠥⠤⢄⢀⡠⠄⡈⡀⠀⠀⣇⣀⠠⢄⠀⠒⠤⠣⠀
⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀"""
    pokemon_dic[7]['Ascii art'] = """
⠀⠀⠀⢀⡤⠔⠒⠚⠉⢙⣒⣒⡤⣀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⠔⠁⠀⠀⠀⢠⠊⠁⢠⠊⠉⠁⠀⡤⢌⢢⠀⠀⠀⠀⠀⠀⠀
⢀⠏⠀⠠⠀⠀⠀⡇⠀⠀⢸⡶⠀⠀⠸⢷⠈⢣⠱⡀⠀⠀⠀⠀⠀
⢸⠀⡰⠁⠀⠀⡜⠀⠀⠀⢸⣇⠇⠀⣀⡙⠓⠁⠀⠱⠀⠀⠀⠀⠀
⢸⢠⠃⠀⢀⠜⠀⠀⠀⠀⢈⡆⠀⠹⠤⠃⠀⠀⠀⣀⣿⠀⠀⠀⠀
⢸⣸⠀⣠⠋⠀⠀⠀⢀⠠⠬⠃⣾⡆⣠⣄⠀⣴⣦⠛⠻⡀⠀⠀⠀
⠀⢿⣰⠁⠀⢰⠒⠖⠁⠀⠀⠀⠀⠀⠙⠋⠀⠈⠁⠀⠀⠈⢦⠀⠀
⠀⠈⠷⠀⠀⢸⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⢱⣄
⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀⢄⠀⠀⠀⡀⡠⠊⠑⠢⠤⠤⠭⠟
⠀⠀⠀⠀⢸⠀⠀⢀⡔⠒⠤⣤⠬⢦⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠒⠓⠉⠀⠀⠀⠀⠉⠉⠑⠤⣔⣳⠄⠀⠀⠀⠀⠀⠀"""
    pokemon_dic[8]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡠⠖⢉⣌⢆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠚⠉⠀⠈⠉⠲⣿⣿⡜⡀⠀⠀⠀⠀
⡔⢉⣙⣓⣒⡲⠮⡇⠀⠀⠀⠀⠀⠀⠘⡿⡇⡇⠀⠀⠀⠀
⡇⠘⣿⣿⣿⠏⠀⠀⠠⣀⡀⠀⠀⠀⠀⡇⠈⠳⡄⠀⠀⠀
⢹⠀⢻⣿⠇⠀⠀⣀⣀⠀⡍⠃⠀⠀⣠⣷⡟⢳⡜⡄⠀⠀
⠈⣆⠀⠋⢀⢔⣵⣿⠋⠹⣿⠒⠒⠚⠁⣿⣿⣾⣷⢸⠤⡄
⠀⡇⠀⠀⢸⢸⣿⣿⣶⣾⡏⡇⠀⠀⢀⡘⣝⠿⡻⢸⡰⠁
⠀⢳⠀⠀⠈⢆⠻⢿⡿⠟⡱⠁⠰⠛⢿⡇⠀⠉⠀⡸⠁⠀
⠀⠈⢆⠀⠀⠀⠉⠒⠒⣉⡀⠀⠀⢇⠀⡇⠀⠀⢠⠃⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⢉⡱⠀⠀⠉⠀⢀⡴⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠓⠦⣀⣉⡉⠁⢀⣀⣠⠤⠒⠥⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⣉⣀⣀⡠⠭⠛⠀⠀⠑⠒⠤⠤⠷⠀⠀⠀"""
    pokemon_dic[9]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠤⠛⠋⠉⠉⠉⠛⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠶⠓⠂⠀⠀⠠⠤⠤⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⡠⢤⠀
⠀⠀⢀⢖⡃⠀⠀⠀⠀⢰⠀⣤⡄⠀⠀⠀⣹⠀⠀⠀⠀⢠⠔⠁⣼⠇
⢀⡞⠉⠀⠑⣄⠀⠀⠀⠘⠀⠀⠀⠐⠀⣠⠋⠀⠀⢠⠖⠉⠀⢰⠏⠀
⠈⠻⢄⣀⡀⢀⡇⠀⠀⠀⠀⠀⢀⡠⠟⠛⢤⣀⠜⠋⠀⠀⢠⠃⠀⠀
⠀⣠⣴⠁⢉⣽⠟⠶⠶⠶⠾⡿⠁⡇⠀⠀⠀⠀⠳⣤⠀⢠⠇⠀⠀⠀
⠰⣏⠈⠢⡎⠒⣄⠀⠀⢀⠶⢁⡠⠃⠀⠀⠀⠀⠀⢸⣄⠎⠀⠀⠀⠀
⠀⠈⠑⣤⣧⠀⠈⠑⡄⣾⣴⢋⡔⢫⡉⠉⠉⠉⠉⠙⣦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⣄⠀⡞⢃⡴⠋⠀⠀⢙⠦⠤⠤⠤⠤⠤⢽⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⢹⣿⣀⠀⢀⡴⠋⠀⠀⠀⠀⣀⣤⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠈⣶⠊⠀⠀⣀⣠⠤⠒⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢤⣟⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    pokemon_dic[10]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡧⠚⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠗⡠⢄⠉⠉⢙⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡴⠦⠝⠋⢌⠀⠀⠱⡀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡠⣊⠄⠒⠩⡩⠂⠒⡑⡄⠀⠘⡀⠀⡘⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡄⡣⡀⠀⡇⠃⠀⣶⣾⢰⠀⠀⡇⡀⠭⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠹⡛⢾⣦⣥⠡⣀⣩⢌⠌⠀⢀⡣⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠂⠍⡻⠎⠀⠈⡁⢀⣠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡨⠗⠁⠊⠿⠻⠉⠓⡲⠦⠤⢤⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡠⠊⠀⢀⠆⠀⠀⢧⡀⣠⡽⠤⠀⠒⣉⣀⡀⠀⠀⠀
⠀⠀⡠⠊⠀⢀⠴⡙⠖⣉⠻⣋⠳⢡⢝⣄⠄⠁⣀⣀⠈⠑⢆⠀
⠰⣿⡤⠐⠊⠀⠀⢏⡎⠀⠓⠁⠈⠃⠀⡇⢠⠊⠤⡀⠑⡄⠀⢃
⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⠀⠀⠀⠀⠀⢇⠈⠢⠄⠃⢀⠃⠀⢸
⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⡰⠚⢦⡀⠀⠀⠁⠒⠀⠒⠁⠀⢠⠇
⠀⠀⠀⠀⠀⠰⠶⠙⣀⢀⠇⠀⠸⠍⢂⡤⢀⢀⣀⠀⠤⠒⠁⠀"""
    pokemon_dic[11]['Ascii art'] = """
⠀⠀⠀⠀⣠⡤⠖⠛⠉⠉⠉⠙⠒⠦⣄⠀⠀⠀⠀
⠀⠀⣠⡾⠛⠉⠙⢲⣴⠚⠉⠉⠛⠦⡈⠓⣄⠀⠀
⠀⣼⠟⢀⣠⡀⣰⠋⠉⣆⠀⣠⡀⠀⠘⣆⠈⢧⠀
⢸⡟⠀⣼⣿⣷⡇⠀⠀⢸⢰⣿⣿⡄⠀⢹⠀⠘⡇
⡟⢷⠀⠹⣿⠟⢷⣦⣴⣾⠘⢿⡿⠁⠀⣾⠀⠀⢹
⡇⠘⢧⡀⠀⠀⠘⢿⣟⠁⠀⠀⠀⢀⡼⠃⠀⠀⢸
⣧⠀⠀⠉⢓⣶⣞⡉⠈⣹⣶⣶⠒⠋⠀⠀⠀⢀⣼
⢹⣷⣠⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⣦⣤⣶⣶⣿⡿
⠀⢻⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⢿⣿⣿⣿⣿⣿⠃
⠀⠀⠙⢿⡀⠂⠀⠀⠀⠀⠀⠀⠀⠉⠹⣿⡿⠃⠀
⠀⠀⠀⢀⣽⣷⣤⣤⣴⡶⠦⣤⣤⣴⣿⡁⠀⠀⠀
⠀⠀⠀⢸⠟⣿⡿⠋⠁⠀⠐⣿⠟⠻⣿⠃⠀⠀⠀"""
    pokemon_dic[12]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠄⠐⢒⡲⠶⠚⠛⠒⠀⠀⣀⣀⠠⠤⠄⡴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⣠⡶⠖⠒
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠊⠁⠀⠀⠀⡴⠋⠀⠀⠀⣀⠤⠒⣉⡁⠤⢤⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠉⢀⠴⠊⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣃⠤⠒⠒⠒⠒⠒⠓⠢⢤⠔⢋⡤⠒⠉⠀⠀⠀⣎⠀⠀⠀⠀⠀⠀⠀⢀⠴⠋⠀⠀⠀⡼⠁⠀⠀⣀⣀⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣥⠀⠀⠀⢀⣠⣀⠀⠀⡏⢰⠋⠀⠀⠀⣀⡀⠤⠼⢗⢦⠀⠀⠀⢀⠞⣁⠴⠒⠒⣦⠀⠉⢒⡹⠝⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⠛⣷⢿⣤⣀⠀⠹⣦⡿⠀⠀⠉⠉⠉⢻⠉⠀⠀⠀⢿⣤⣼⠟⠀⠀⣰⡷⠋⠀⠀⢀⣴⢋⡤⠚⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡦⣄⣟⠄⠸⣶⠿⢿⣴⠆⠀⡴⠉⠉⢦⡀⠀⠀⢣⣀⡠⢤⠀⠀⠀⠀⠀⠼⠋⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠀⠘⢿⠀⠀⠙⠓⠚⠁⠀⠀⠙⠤⠤⠞⠀⣀⠴⠺⣅⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣇⣀⠜⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠘⢆⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡇⢠⠗⠋⠉⠑⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⡏⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⣀⠤⠄⠠⠤⡀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣇⠀⠀⠀⠀⠀⠀⠀⠀⢣⡠⠊⠀⠀⠀⠀⢀⣨⣔⣁⣇⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⠘⡄⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠉⢀⡤⢺⡀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢉⣇⠀⣀⣀⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣄⠀⠀⠈⠳⢄⡀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠲⣄⠀⠀⠀⠉⢲⠤⠄⣀⣀⣳⡄⠀⠀⠀⠀⡠⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠟⠀⠀⠀⡰⠋⠀⠀⠀⢀⠜⠁⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡠⠞⠁⠀⠀⣠⠞⠀⠀⠀⢀⡴⠋⣀⡠⣀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡤⠾⠅⣠⠤⢒⡶⠊⠁⠀⠀⢀⡴⠛⠒⠊⠁⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡴⠇⠀⠀⢀⡤⠒⠉⠀⠀⠀⠀⢠⠋⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠙⠓⠒⠈⠁⠀⠀⠀⠀⠀⠀⠀⢳⡇⢰⢀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    pokemon_dic[13]['Ascii art'] = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠶⠶⣄⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣀⣀⡀⠘⠻⣄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢣⣄⠘⢳⡄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠾⢛⠛⣛⡟⠀⣿⠀⠀⠀
    ⠀⠀⠀⢀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⢀⡦⠟⠛⠛⠛⢦⡃⢸⡇⠀⠀
    ⠀⠀⠀⣾⠓⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠋⠀⠀⠀⠀⠀⢸⡇⢸⡇⠀⠀
    ⠀⠀⠀⣿⢧⡄⠙⠛⢦⡀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡼⢻⡄⠀⠸⣁⠹⡀⠀
    ⠀⠀⠀⠛⣿⣿⠤⠜⠛⠛⠒⢢⣤⠤⠖⠚⠛⠀⣉⣈⣀⡼⠂⠀⠀⢫⡄⢳⡄
    ⠀⠀⠀⠀⢹⡏⣜⣢⠀⠀⠀⠈⠉⢀⣤⣴⣶⣾⣿⣿⠟⠁⠀⠀⠀⢸⣇⢸⡇
    ⠀⢀⣀⡾⣯⡅⠙⠋⢁⡠⣤⡤⠐⢺⣿⣿⣿⠯⠟⠁⠀⠀⠀⠀⣸⠯⡙⡾⠃
    ⢠⢟⣩⡕⣏⣡⠄⠀⠾⣧⠿⠃⠀⠈⠉⠛⢯⡀⣀⡠⠤⢤⡤⣒⣏⣼⠝⠁⠀
    ⠀⠈⠉⠙⠚⠑⢤⣄⣀⣀⠀⢀⣶⡀⣤⡀⠀⢹⣉⠁⠀⠀⠀⠉⠙⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠉⢹⡯⣐⠪⢩⡕⠛⠑⠒⣤⣿⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣼⢱⠒⠋⠉⠀⠀⠀⠀⠀⣄⣤⣤⣄⠀⠀⠀⢸⣇⠀⠀
    ⠀⠀⠀⠀⢀⣴⠒⠚⣅⣚⣿⣶⣠⠀⠀⠀⣶⡿⠿⣿⣿⣿⣷⣤⡄⠀⠘⣧⠀
    ⠀⠀⠀⠠⡼⢳⣰⡾⠞⠋⠀⠈⣿⠀⢀⡴⠋⠀⠀⢸⣿⣿⠋⠀⢸⠁⠀⣿⠀
    ⠀⠀⠀⠈⢻⣦⠏⠀⠀⠀⠀⢰⠉⠀⣶⠁⠀⠀⣠⣾⣿⡟⠁⢠⡟⠁⢰⠋⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡆⢰⠋⠀⠀⠀⠉⠉⠉⠀⠀⠈⠑⢳⠋⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⡤⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    pokemon_dic[14]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠶⠟⢛⣻⠟⣛⡷⢾⣿⣄⣀⡾⠛⠛⠛⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡶⠏⠉⠰⠇⠀⠸⠉⢴⣏⣷⠈⢹⡏⠉⢀⣰⠶⣇⠈⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣧⣿⣿⣿⣧⣤⣀⡀⠈⠉⠉⠉⠉⠁⠀⣼⣿⣄⣈⣠⣼⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⣿⣿⣿⣿⣿⣶⣆⡀⠀⠀⠀⠀⠀⠘⠛⣿⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⣿⣿⣿⣿⣿⣿⡷⠤⣄⣀⠀⢠⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⡿⣿⣿⣿⣿⠃⠀⠀⢸⢀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⣿⣿⣿⡿⠿⠋⠀⠀⠀⠀⣼⣼⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣯⣭⣉⠁⠀⠀⠀⠀⠀⡴⣻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⣀⡗⣿⠀⠀⠀⠀⠀⠀⣀⡶⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠉⠀⠀⠀⠀⠀⣏⠁⣿⠀⠀⠀⣤⣤⣼⡏⠁⣼⣿⠀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠛⠀⠀⠀⠀⠀⢸⡇⠀⣿⣛⠛⠃⣀⠜⠃⠀⡄⠹⣿⡛⠧⢿⣀⣀⣀⡶⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡿⠀⠀⠀⠀⠀⠀⢸⠣⠀⢸⣿⠷⣆⣥⢀⠰⠀⠁⠀⠈⠁⠀⠈⠹⠿⣏⣁⣼⠿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠃⠀⠀⠀⠀⠀⠀⢸⠀⠈⠂⢹⡧⣭⣹⢻⣄⡀⠀⠀⠀⠀⠀⣄⣠⠘⠈⣤⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣞⠃⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠘⠷⣆⠻⢶⡘⣷⡆⠀⠀⠀⠀⠛⢻⡆⠀⠛⣷⠶⣆⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⣿⣶⡄⠿⣦⠸⢧⡍⣿⢠⣤⣤⡄⣸⣿⣥⣤⡄⢩⣼⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣶⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⢻⣿⡇⠀⣑⣀⠘⣷⣍⢻⣾⣷⣶⣻⣶⣶⣾⣟⣻⣾⣇⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⡄⠀⠀⢀⠒⡿⠿⠀⠀⠙⠶⠶⠶⠶⠏⢰⣶⡇⠉⠹⢶⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣀⣠⣤⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣣⢜⣠⣞⣬⣦⣤⣤⣤⣤⣤⣀⣀⣀⠘⡋⠁⠀⠘⠛⣷⣤⣄⣀⠀⠀⠀⠀
⢀⣀⣀⡶⠿⠛⠃⠀⠁⢻⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠺⡀⠛⢙⠀⠀⠀⠀⠀⠘⠉⠛⢻⠾⢇⣀⡀⠀⠀⠀⠀⠋⠻⠶⠶⣆⠀
⠸⢿⡍⠁⠀⠀⠀⠀⡤⠮⠬⠷⣦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠈⠉⠷⢿⠷⣧⡤⠤⢤⣤⣤⡿⠂
⠀⠈⠙⠛⣧⣾⣤⣤⣤⣤⣾⠛⠛⠛⠛⢳⣤⣤⣤⣀⣀⣀⣀⣀⣙⣧⣤⣀⣀⣈⣓⠒⠒⠒⠒⠒⠚⢀⣀⣀⣤⣼⠛⠛⠛⠉⠉⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠈⠉⠉⠉⠙⣶⣶⣶⣶⣶⣶⡾⠉⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    pokemon_dic[15]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣶⣦⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣶⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡀⣄⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠉⠀⢀⣀⠀⠀⠈⠉⠀⠀⣀⣀⠀⠀⠙⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣶⣿⣿⣿⣾⣇⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⣼⡏⠀⠀⠀⣀⣀⣉⠉⠩⠭⠭⠭⠥⠤⢀⣀⣀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣿⠷⠒⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠒⠼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣶⣤⣄⣠⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⠀⠀⣀⠀⢸⡿⠿⣿⡿⠋⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠻⠿⠟⠉⢙⣿⣿⣿⣿⣿⣿⡇
⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⢿⡿⣿⠳⠀
⠀⠀⡞⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⡀⠀⠀
⢀⣸⣀⡀⠀⠀⠀⠀⣠⣴⣾⣿⣷⣆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⢿⣿⠿⠃⠀
⠘⢿⡿⠃⠀⠀⠀⣸⣿⣿⣿⣿⣿⡿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⡸⠁⠀⠀⠀
⠀⠀⠳⣄⠀⠀⠀⠹⣿⣿⣿⡿⠛⣠⠾⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠳⣄⠙⠛⠿⠿⠛⠉⠀⠀⣀⠜⠁⠀⠀⠀⠀
⠀⠀⠀⠈⠑⠢⠤⠤⠬⠭⠥⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠢⠤⠤⠤⠒⠊⠁⠀⠀⠀⠀⠀⠀"""
    pokemon_dic[16]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠖⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⢤⡀⠀⠀⠀⠀⢸⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠈⠢⡀⠀⠀⢀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⡔⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⡹⠀⠀⠘⢄⠀⠈⠲⢖⠈⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠈⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠁⢠⠞⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠉⠑⠢⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠚⠁⠀⠀⠀⡇⠀⠀⠀⠀⠀⢀⠇⠀⡤⡀⠀⠀⠀⢀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢠⣾⣿⣷⣶⣤⣄⣉⠑⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠞⢁⣴⣾⣿⣿⡆⢇⠀⠀⠀⠀⠀⠸⡀⠀⠂⠿⢦⡰⠀⠀⠋⡄⠀⠀⠀⠀⠀⠀⠀⢰⠁⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡴⢁⣴⣿⣿⣿⣿⣿⣿⡘⡄⠀⠀⠀⠀⠀⠱⣔⠤⡀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⡜⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⢣⠀⠀⠀⠀⠀
⠀⠀⠀⡼⢠⣾⣿⣿⣿⣿⣿⣿⣿⣧⡘⢆⠀⠀⠀⠀⠀⢃⠑⢌⣦⠀⠩⠉⠀⡜⠀⠀⠀⠀⠀⠀⢠⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣣⡀⠀⠀⠀
⠀⠀⢰⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠱⡀⠀⠀⠀⢸⠀⠀⠓⠭⡭⠙⠋⠀⠀⠀⠀⠀⠀⠀⡜⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡱⡄⠀⠀
⠀⠀⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢃⠀⠀⠀⢸⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⢀⠜⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠘⣆⠀
⠀⢸⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⣆⠀⠀⡆⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⡠⠖⣡⣾⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⠀
⠀⡏⣾⣿⣿⣿⣿⡿⡛⢟⢿⣿⣿⣿⣿⣿⣿⣧⡈⢦⣠⠃⠀⠀⠀⠀⠀⢱⣀⠤⠒⢉⣾⡉⠻⠋⠈⢘⢿⣿⣿⣿⣿⠿⣿⣿⠏⠉⠻⢿⣿⣿⣿⣿⡘⡆
⢰⡇⣿⣿⠟⠁⢸⣠⠂⡄⣃⠜⣿⣿⠿⠿⣿⣿⡿⠦⡎⠀⠀⠀⠀⠀⠒⠉⠉⠑⣴⣿⣿⣎⠁⠠⠂⠮⢔⣿⡿⠉⠁⠀⠹⡛⢀⣀⡠⠀⠙⢿⣿⣿⡇⡇
⠘⡇⠏⠀⠀⠀⡾⠤⡀⠑⠒⠈⠣⣀⣀⡀⠤⠋⢀⡜⣀⣠⣤⣀⠀⠀⠀⠀⠀⠀⠙⢿⡟⠉⡃⠈⢀⠴⣿⣿⣀⡀⠀⠀⠀⠈⡈⠊⠀⠀⠀⠀⠙⢿⡇⡇
⠀⠿⠀⠀⠀⠀⠈⠀⠉⠙⠓⢤⣀⠀⠁⣀⡠⢔⡿⠊⠀⠀⠀⠀⠙⢦⡀⠀⠐⠢⢄⡀⠁⡲⠃⠀⡜⠀⠹⠟⠻⣿⣰⡐⣄⠎⠀⠀⠀⠀⠀⠀⠀⠀⢣⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠙⢦⣀⢀⡴⠁⠀⠀⠀⠀⠉⠁⢱⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠈⢏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⢀⡴⠁⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣧⣠⠤⠖⠋⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠳⢄⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠊⠈⠁⠀⠀⠀⡔⠛⠲⣤⣀⣀⣀⠀⠈⢣⡀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⢀⡠⢔⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢈⠤⠒⣀⠀⠀⠀⠀⣀⠟⠀⠀⠀⠑⠢⢄⡀⠀⠀⠈⡗⠂⠀⠀⠀⠙⢦⠤⠒⢊⡡⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠒⣒⡁⠬⠦⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⢺⢠⠤⡀⢀⠤⡀⠠⠷⡊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠣⡀⡱⠧⡀⢰⠓⠤⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    pokemon_dic[17]['Ascii art'] = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⢳⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠋⠀⢰⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢆⣤⡞⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢠⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣾⢳⠀⠀⠀⠀⢸⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⡤⠴⠊⠉⠀⠀⠈⠳⡀⠀⠀⠘⢎⠢⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠳⣄⠀⠀⡠⡤⡀⠀⠘⣇⡀⠀⠀⠀⠉⠓⠒⠺⠭⢵⣦⡀⠀⠀⠀
⠀⢹⡆⠀⢷⡇⠁⠀⠀⣸⠇⠀⠀⠀⠀⠀⢠⢤⠀⠀⠘⢷⣆⡀⠀
⠀⠀⠘⠒⢤⡄⠖⢾⣭⣤⣄⠀⡔⢢⠀⡀⠎⣸⠀⠀⠀⠀⠹⣿⡀
⠀⠀⢀⡤⠜⠃⠀⠀⠘⠛⣿⢸⠀⡼⢠⠃⣤⡟⠀⠀⠀⠀⠀⣿⡇
⠀⠀⠸⠶⠖⢏⠀⠀⢀⡤⠤⠇⣴⠏⡾⢱⡏⠁⠀⠀⠀⠀⢠⣿⠃
⠀⠀⠀⠀⠀⠈⣇⡀⠿⠀⠀⠀⡽⣰⢶⡼⠇⠀⠀⠀⠀⣠⣿⠟⠀
⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⡶⠤⣷⣅⡀⠀⠀⠀⣀⡠⢔⠕⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠫⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀"""
    return pokemon_dic
