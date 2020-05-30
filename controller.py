import requests
import random


def easy():
    number = random.randint(1, 1554)
    url = "https://rcijeux.fr/drupal_game/20minutes/kemaru/grids/"+ str(number) + ".kemj"
    return getData(url)

def hard():
    number = random.randint(1, 190)
    init = random.randint(1, 2)
    url = "https://rcijeux.fr/drupal_game/telestar/kemaru/grids/kemaru_"+str(init)+"_"+str(number)+".kemj"
    return getData(url)


def getData(url):
    response = requests.get(url)
    if response.status_code == 200:
        solution = response.text.split('solution:')[1].split(',')[0]
        zone = response.text.split('zone:')[1].split('}')[0]
        places = response.text.split(solution+',')[1].split('zone')[0]
        places_dict={}
        for i in [x for x in places.strip('\r\n').strip(',').split(',')]:
            key = i.split(':')[0]
            value = int(i.split(':')[1].strip('\"'))
            places_dict.update({key: value})

        return {'solution': [int(x) for x in str(int(solution.strip('\"')))],
                'zone': [str(x) for x in zone.strip('\r\n').strip('\"')], 'places': places_dict}
    else:
        getData(url)



def create_grids(getPattern_to_solve, number):

    grid_from_site = getPattern_to_solve['places']
    grid_to_solve = {}
    for i in range(1, (number * number) + 1):
        grid_to_solve.update({'c' + str(i): 0})

    for key in grid_to_solve:
        if key in grid_from_site:
            grid_to_solve[key] = grid_from_site[key]
        else:
            continue
    return grid_to_solve


def map_solution_sets(sets):
    grid_to_solve = {}
    for i in range(0, len(sets)):
        grid_to_solve.update({'c' + str(i+1): sets[i]})
    return grid_to_solve


def split_dict_equally(my_dict, chunks):
    return_list = [dict() for idx in range(chunks)]
    idx = 0
    return_dict={}
    for k,v in my_dict.items():
        return_list[idx][k] = v
        if idx < chunks-1:  # indexes start at 0
            idx += 1
        else:
            idx = 0
    for item in range(1, len(return_list)+1):
        return_dict.update({'r'+str(item): return_list[item-1]})
    return return_dict

def pattern_generator(board, inner_square):
    club = [board, inner_square]
    pattern = {}
    for k in board.keys():
        pattern[k] = list(pattern[k] for pattern in club)
    return pattern