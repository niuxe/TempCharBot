import discord
import re
import invite_service
import repository
from decouple import config
from discord.ext import commands


"""Allowing the bot to access the list of members"""
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
async def add_quote(ctx):
    author = ctx.author
    await ctx.message.delete()
    await repository.dm_quote(author)

    def check(m):
        return m.channel == author.dm_channel and m.author == ctx.author

    _quote = await bot.wait_for('message', check=check, timeout=30)
    await repository.dm_name(author)

    _name = await bot.wait_for('message', check=check, timeout=30)
    await repository.dm_year(author)

    _year = await bot.wait_for('message', check=check, timeout=30)

    await repository.add_quote(_quote.content, _name.content, _year.content)
    await author.send("Quote added")


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
