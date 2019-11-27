import json
data = {
    "president": {
        "name": "Allif Izzuddin",
        "species": "Homo-sapien"
    }
}

with open("data_file.json", "w+") as write_file:
    json.dump(data, write_file) #json.dump(data object to serialized, file-like object)

#also can use as below, but it means we didnot write data into disk, careful!
#json_string = json.dumps(data) #look at dumps(), similar to dump()

#dump() and dumps() use same keywords arguement, example
#json.dumps(data, indent=4)

#ENCODE AND DECODE USUALLY NOT YIELD SAME RESULT, example

blackjack_hand = (8,"Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)
print(blackjack_hand == decoded_hand)
print(type(blackjack_hand))
print(type(decoded_hand))
print(blackjack_hand == tuple(decoded_hand))

#if we already have data stored on disk, we can use context manager to manipulate

with open("data_file.json","r") as read_file:
    data = json.load(read_file) #deserialize json file

json_string = """
{
    "researcher": {
        "name": "Allif Izzuddin",
        "species": "kacang sedap",
        "relatives": [
            {
                "name": "Siti Nur Syazana",
                "species": "beautiful"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(data)