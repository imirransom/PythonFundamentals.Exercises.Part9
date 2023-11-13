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
# read_all_json_files("yoshi.json")

# Iterating through the list that is holding the json files
# in a dictionary
for j in json_list:
    for key, value in j.items():
        print(key, value)


# The "json" file path being used for the write_pickle function
captain_falcon = {
    "name": "Captain Falcon",
    "neutral_special": "Falcon Punch",
    "side_special": "Raptor Boost",
    "up_special": "Falcon Dive",
    "down_special": "Falcon Kick",
    "final_smash": "Blue Falcon"
}
yoshi = {
    "name": "Yoshi",
    "neutral_special": "Egg Lay",
    "side_special": "Egg Roll",
    "up_special": "Yoshi Throw",
    "down_special": "Yoshi Bomb",
    "final_smash": "Super Dragon"
}


def write_pickle(file, file_name):
    """
    This function takes in a file path as a parameter and the
    function writes the contents of the json file to a file
    called super_smash_characters.pickle
    :param file_name:
    :return:
    """
    with open(file, "w") as f:
        character = json.dump(file_name, f)
        return character

# write_pickle(yoshi_pickled)
def load_pickle(character_data):
    """
    When given a file path as the parameter, the function will
    open up a pickled file and return the data
    :param character_data:
    :return:
    """
    with open(character_data) as f:
        character = json.load(f)
    return character

# y = load_pickle(load_yoshi)


# I passed the captain_falcon dict (json file) into the function
# write pickle so that it can save this json file in it

write_pickle("super_smash_characters.pickle", yoshi)
write_pickle("super_smash_characters.pickle", captain_falcon)
# This is taking the pickled file and loading it to be
# printed to the console. It has the file I wrote into
# it and will return that data. saved to a
# variable, so I can iterate through it

y = load_pickle("super_smash_characters.pickle")
cp_fal = load_pickle("super_smash_characters.pickle")
# Iterates through the file and prints to the console
for key, value in cp_fal.items():
    print(key, value)
