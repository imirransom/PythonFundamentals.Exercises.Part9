import json
def read_json():
    with open("mario.json") as m:
        character = json.load(m)
    print(character)


def read_json2():
    with open("link.json") as l:
        character = json.load(l)
    print(character)
json_list = []
def read_all_json_files(json_file):
    with open(json_file) as f:
        file_object = json.load(f)
    json_list.append(file_object)

read_all_json_files("mario.json")
read_all_json_files("link.json")

for j in json_list:
    for key, value in j.items():
        print(key, value)
# read_json()