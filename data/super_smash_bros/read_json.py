import json


def read_json(file_json):
    """
    This function will open json files
    and convert the contents inside into
    a json object
    """
    with open(file_json) as m:
        character = json.load(m)
    return character

# An empty list made to be populated with json objects
json_list = []


def read_all_json_files(json_file):
    """
    This function will take a json object as a parameter
    and put it into as list
    """
    return json_list.append(read_json(json_file))

# Here the function to read all json files will be called
# and takes a json file as an argument to be opened from
# the read_json function and saved as a json object, to
# then be saved in a list with the read_all_json_files function
read_all_json_files("mario.json")
read_all_json_files("link.json")


# Iterating through the list that is holding the json files
# in a dictionary
for j in json_list:
    for key, value in j.items():
        print(key, value)
