def calculate_new_location(character, direction):
    coordinate_changes = {"1": (0, -1), "2": (0, 1), "3": (-1, 0), "4": (1, 0)}
    new_x_coordinate = character['Location'][0] + coordinate_changes[direction][0]
    new_y_coordinate = character['Location'][1] + coordinate_changes[direction][1]
    return new_x_coordinate, new_y_coordinate
