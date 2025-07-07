import json


def import_to_json(data):
    with open('high-score.json', 'w') as f:
        json.dump(data, f)

def json_read():
    with open('high-score.json') as f:
        return json.load(f)
