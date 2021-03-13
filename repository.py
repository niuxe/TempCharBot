import json
import random


def read_roles():
    return None


async def add_quote(quote):
    with open("save_file.json", 'r+', encoding='utf8') as file:
        json_object = json.load(file)
        json_object['quotes'].append(quote)
        file.seek(0)
        json.dump(json_object, file, indent=4, ensure_ascii=False)


def get_quote():
    with open("save_file.json", 'r', encoding='utf8') as file:
        json_object = json.load(file)
        return json_object['quotes'][random.randint(0, len(json_object['quotes'])-1)]
