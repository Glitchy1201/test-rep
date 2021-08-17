import discord
from discord import channel
from discord.ext import commands

client = commands.Bot(command_prefix = '(')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.invisible, activity=discord.Game('with his food'))
    print('Too slow, too slow, The World is the ultimate stand!')

@client.event
async def on_member_join(member):
    print(member,'are you approaching me?')

@client.event
async def on_member_remove(member):
    print(member,'came as close as they could.')

@client.command(aliases=['w'])
async def warn (ctx, *, message, amount=10000000000000):
    await ctx.channel.purge(limit=amount)
    for i in range (0,50):
        await ctx.send(message)
        await ctx.channel.purge(limit=amount)
    
@client.command(aliases=['c'])
async def clear(ctx, *, amount):
    e = int(amount)
    await ctx.send('ZA WAURDO')
    await ctx.channel.purge(limit=e)

@client.command(aliases=['dm','DM','D'])
async def d(ctx, user: discord.User, *, message=None, amount=1):
    await ctx.channel.purge(limit=amount)
    message = message
    await user.send(message)

@client.command(aliases=['s'])
async def say(ctx, *, me, amount=1):
    e = int(amount)
    await ctx.channel.purge(limit=amount)
    await ctx.send(me)

@client.command(aliases=['a'])
async def annoy (ctx, *, who: discord.User, amount=1):
    await ctx.channel.purge(limit=amount)
    for i in range(0,100000):
        await who.send('im anooying you')

@client.event
async def on_message(ctx):
    await ctx.channel.send(ctx)

client.run('')
