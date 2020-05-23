import discord
from discord.ext import commands, tasks
from itertools import cycle
from datetime import date

TOKEN = "NzAzMjAwOTQwNDU4NzcwNjEz.XqPu-Q.AWKWWI2lW39i2MW41e9KcbKP_0c"
status = cycle(["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010"])
client = commands.Bot(command_prefix = '.')
 
evenemnts = []

@client.event
async def on_ready():
    change_status.start()
    print('Beep Boop Boop')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

@client.command(aliases = ['rappel'])
async def addEvent(ctx, *, evenement):
    evenements.append()
    await ctx.send("D'accord, je vous rappelerai: " + evenement)

@client.command(aliases = ['man'])
async def guide(ctx):
    embed = discord.Embed(title = "Help", description = "Liste de commandes")
    embed.add_field(name =  ".ping", value = "retourne la latence du bot en ms ")
    embed.add_field(name = ".rappel jj/mm//aaaa evenemnt", value = "rappelra l'évenemnt à la date specifiée")
    await ctx.send(content = None, embed = embed)

"""
@client.event
async def on_message(message):
    if message.content == ".help":
        embed = discord.Embed(title = "Help", description = "Liste de commandes")
        embed.add_field(name =  ".ping", value = "retourne la latence du bot en ms ")
        await message.channel.send(content = None, embed = embed)
"""

client.run(TOKEN)
