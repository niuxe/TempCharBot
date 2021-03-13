import discord
import re
import invite_service
import repository
from decouple import config
from discord.ext import commands


"""Allowing the bot to access the list of memebers"""
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='%', intents=intents)
client = discord.Client()


@bot.command()
async def inv(ctx, game, message=None):
    response = await invite_service.check_if_role_exist(ctx, game)
    if response:
        for member in ctx.guild.members:
            if member.get_role(response):
                await invite_service.dm_member(ctx.message.author.name,
                                               game,
                                               member,
                                               message)
                await ctx.send("Invite was sent")
    else:
        await ctx.send("Game doest not exist, consider adding it")


@bot.command()
async def quote(ctx):
    await ctx.send(repository.get_quote())


@bot.command()
async def add_quote(ctx, new_quote):
    if re.match(r'[\w\s]+-\s[\w]+\s\d{4}', new_quote):
        await repository.add_quote(new_quote)
        await ctx.send("Quote was added!")
    else:
        await ctx.send("Quote doesn't match the format. Should be: what they say - name year(e.g. 1234)")


@bot.command()
async def subscribe(ctx, game):
    await ctx.send("{} is now subscribing to {}".format(ctx.message.author.name, game))


@bot.command()
async def unsubscribe(ctx, game):
    await ctx.send("{} is now unsubscribed to {}".format(ctx.message.author.name, game))


@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()


if __name__ == "__main__":
    bot.run(config('TOKEN'))
