import json

with open('database/urls.json') as json_file:
    data = json.load(json_file)

easy_grid = data['easy']
hard_grid = data['hard']
