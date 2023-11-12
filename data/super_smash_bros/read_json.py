import json
def read_json():
    with open("mario.json") as smb:
        character = json.load(smb)
    print(character)

read_json()