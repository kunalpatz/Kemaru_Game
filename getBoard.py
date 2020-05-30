from apicall import *

def launch(userInput):
    if userInput == 'easy':
        number = 6
        getPattern_to_solve = easy()
        board = create_grids(getPattern_to_solve, number)
        final_solution = map_solution_sets(getPattern_to_solve['solution'])
        inner_square = map_solution_sets(getPattern_to_solve['zone'])

    elif userInput == 'normal':
        number = 9
        getPattern_to_solve = hard()
        board = create_grids(getPattern_to_solve, number)
        final_solution = map_solution_sets(getPattern_to_solve['solution'])
        inner_square = map_solution_sets(getPattern_to_solve['zone'])

    colors = {'a': 'PINK', 'b': 'LIGHTGOLDENRODYELLOW', 'c': 'CYAN', 'd': 'LIGHTSALMON', 'e': 'PALEGREEN',
              'f': 'AQUAMARINE', 'g': 'LIGHTSTEELBLUE',
              'h': 'CHARTREUSE', 'i': 'MEDIUMAQUAMARINE', 'j': 'SKYBLUE', 'k': 'DARKKHAKI', 'l': 'YELLOWGREEN',
              'm': 'TAN', 'n': 'MEDIUMPURPLE',
              'o': 'LAVENDER', 'p': 'bisque', 'q': 'YELLOW', 'r': 'PALEVIOLETRED', 's': 'THISTLE'}

    for key, val in inner_square.items():
        inner_square[key] = colors[val]


    layout = split_dict_equally(pattern_generator(board, inner_square), number)
    solution_layout = split_dict_equally(pattern_generator(final_solution, inner_square), number)
    return {'pattern': layout, 'final_solution': solution_layout}


