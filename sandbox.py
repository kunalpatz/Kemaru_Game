import json
import random

def get_offline_data(pattern):
    with open('database/offline_grids.json') as json_file:
        data = json.load(json_file)
        number = random.randint(1500, 1600)
    return data[pattern][str(number)]