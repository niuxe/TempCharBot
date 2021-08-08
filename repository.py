import json
import random
import discord


def read_roles():
    return None


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
        json_object['quotes'].append(quote_to_add)
        file.seek(0)
        json.dump(json_object, file, indent=4, ensure_ascii=False)


def get_quote():
    with open("save_file.json", 'r', encoding='utf8') as file:
        json_object = json.load(file)
        return json_object['quotes'][random.randint(0, len(json_object['quotes'])-1)]
