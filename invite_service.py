async def check_if_role_exist(ctx, game):
    for role in ctx.guild.roles:
        if role.name == "bot_{}".format(game):
            return role.id
    return None


async def dm_member(host, game, member, message=None):
    if not member.dm_channel:
        await member.create_dm()
    invite_message = "{} invites you to play {}".format(host, game)
    if message:
        invite_message += (", with the message: {}".format(message))
    await member.send(invite_message)
