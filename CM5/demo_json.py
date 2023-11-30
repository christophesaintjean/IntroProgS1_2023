import json

Lisa = {'age': 8, 'sexe': 'F', 'prénom': 'Lisa', 'nom': 'Simpson'}

with open('Lisa.json', mode='w') as f:
    json.dump(Lisa, f)

with open('Lisa2.json', mode='w') as f:
    json.dump(Lisa, f, indent=4, sort_keys=True)