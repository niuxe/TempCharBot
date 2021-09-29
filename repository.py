import json
import random


def read_roles():
    return None


# region Add quote
async def dm_quote(author):
    if not author.dm_channel:
        await author.create_dm()
    await author.send("Enter the quote")


async def dm_name(author):
    await author.send("Who said it?")


async def dm_year(author):
    await author.send("What year?")


async def add_quote(quote, name, year):
    quote_to_add = "".join((quote.capitalize(), " - ", name.capitalize(), " ", year))
    with open("save_file.json", 'r+', encoding='utf8') as file:
        json_object = json.load(file)
        quote_weights = list(x[1] for x in json_object['quotes'])
        weight = round(sum(quote_weights) / len(quote_weights))
        json_object['quotes'].append([quote_to_add, weight])
        _save_data(json_object, file)
# endregion


# region get quote
def get_quote():
    with open("save_file.json", 'r+', encoding='utf8') as file:
        json_object = json.load(file)
        quote_index = list(range(0, len(json_object['quotes'])))
        weights_list = list(x[1] for x in json_object['quotes'])
        number = random.choices(quote_index, weights=weights_list, k=1)[0]
        _edit_weights(json_object, number, file)
        quote = json_object['quotes'][number][0]
        return quote


def get_all_quotes():
    with open("save_file.json", 'r', encoding='utf8') as file:
        json_object = json.load(file)
        return "\n".join(json_object['quotes'])
# endregion


# region Helper functions
def _edit_weights(json_object, number, file):
    weight = json_object['quotes'][number][1]
    if weight == 1:
        json_object = _add_weights(json_object)
    else:
        json_object['quotes'][number][1] = weight-1
    print(json_object)
    _save_data(json_object, file)


def _add_weights(json_object):
    for idx, x in enumerate(json_object['quotes']):
        json_object['quotes'][idx][1] = x[1]+10
    return json_object


def _save_data(json_object, file):
    file.seek(0)
    print(json_object)
    json.dump(json_object, file, indent=4, ensure_ascii=False)
    file.truncate()

# endregion
