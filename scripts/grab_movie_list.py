import json, os

def grab_movie_list():
    file_dir = os.path.dirname(__file__)

    last_scrap_location = os.path.join(file_dir, '../scrap/last_scrap.json')
    name_list_location = os.path.join(file_dir, '../scrap/name_list')

    scrap_results = {}
    with open(last_scrap_location, "r") as scrap_file:
        scrap_results = json.load(scrap_file)
			
    name_list = []
    with open(name_list_location, "r") as f:
        for line in f:
            name_list.append(line.strip())

    return name_list, scrap_results
