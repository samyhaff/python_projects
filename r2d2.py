import discord
from discord.ext import commands, tasks
from itertools import cycle

TOKEN = "NzAzMjAwOTQwNDU4NzcwNjEz.XqPu-Q.AWKWWI2lW39i2MW41e9KcbKP_0c"
status = cycle(["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010"])
client = commands.Bot(command_prefix = '.')

def is_it_me(ctx):
    return ctx.author.id == 347711466167861248

@client.event
async def on_ready():
    change_status.start()
    print('Beep Boop Boop')

"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('salut'):
        await message.channel.send('Bien le bonjour.')
"""

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases = ['salut', 'bonjour'])
async def saluer(ctx):
    await ctx.send('Bien le bonjour.')

@client.command(aliases = ['dis'])
@commands.check(is_it_me)
async def repeter(ctx, *, phrase):
    await ctx.send(phrase + " beep boop boop")

@client.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit = amount + 1)

@purge.error
async def purge_error(ctx, error):
    pass

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason )

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Veuillez renseginer tous les arguments necessaires.")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Cette commande n'existe pas!")

client.run(TOKEN)
