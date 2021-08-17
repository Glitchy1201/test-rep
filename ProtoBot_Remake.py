i = 1
a = 1
canvas_width = 700
canvas_height = 500
brush_size = 3
color = "yellow"
import random
import discord
from turtle import *
from tkinter import *
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('With OG Protobot'))
    print('Too slow, too slow, The World is the ultimate stand!')

@client.event
async def on_member_join(member):
    print(member,'are you approaching me?')

@client.event
async def on_member_remove(member):
    print(member,'came as close as they could.')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question, amount=1):
    await ctx.channel.purge(limit=amount)
    responses =['● It is certain.',
'● It is decidedly so.',
'● Without a doubt.',
'● Yes - definitely.',
'● You may rely on it.',
'● As I see it, yes.',
'● Most likely.',
'● Outlook good.',
'● Yes.',
'● Signs point to yes.',
'● Reply hazy, try again.',
'● Ask again later.',
'● Better not tell you now.',
'● Cannot predict now.',
'● Concentrate and ask again.',
'● Dont count on it.',
'● My reply is no.',
'● My sources say no.',
'● Outlook not so good.',
'● Very doubtful.']
    await ctx.send(f'question:{question}\nAnswer: {random.choice(responses)}')


        
@client.command(aliases=['c'])
async def comp(ctx, *, question, amount=1):
    await ctx.channel.purge(limit=amount)
    responses =['you are a pro!',
                'I bet you make babies smile. ...',
    'You have impeccable manners. ...',
    'You are the most perfect you there is. ...',
    'Your perspective is refreshing. ...',
    'You should be proud of yourself. ...',
    'Youre more helpful than you realize. ...',
    'Youve got all the right moves! ...',
    'Your kindness is a balm to all who encounter it.']
    await ctx.send(f' {question}, {random.choice(responses)}')
    
@client.command(aliases=['i'])
async def insult(ctx, *, question, amount=1):
    await ctx.channel.purge(limit=amount)
    responses =['You are a noob!',
                'you Bastard Brat of a Scotch Pedler',
                'you Drunken Trowser-Maker',]
    await ctx.send(f' {question}, {random.choice(responses)}')

@client.command(aliases=['cl'])
async def clear (ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['k'])
async def kick(ctx, member : discord.Member, *, reason=None, amount=1):
    await ctx.channel.purge(limit=amount)
    await member.kick(reason=reason)

@client.command(aliases=['b'])
async def ban(ctx, member : discord.Member, *, reason=None, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send('reason?')
    wait = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
    wait = reason.content
    await ctx.channel.purge(limit=amount)
    await ctx.channel.purge(limit=amount)
    await member.ban(reason=reason)

@client.command(aliases=['ub'])
async def unban(ctx, *, member, amount=1):
    await ctx.channel.purge(limit=amount)
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'the idiot {user.name}#{user.mention} that got banned',
                           'is back!')
            return

@client.command(aliases=['clall'])
async def clear_all (ctx, amount=1000000):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['m'])
async def message (ctx, who, *, message, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send (f'{who} {message}')

@client.command(aliases=['a', 'an'])
async def announce (ctx, *, message, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send (f'@everyone {message}')

@client.command(aliases=['cv'])
async def Creatorsvibes(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send('https://www.youtube.com/playlist?list=PLK7Ubt-aBVWPoL47gogqqU8hMZ_mLfgAo')

@client.command(aliases=['off'])
async def poweroff (ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await client.change_presence(status=discord.Status.invisible, activity=discord.Game('Off'))

@client.command(aliases=['on'])
async def poweronn (ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('With OG Protobot'))

@client.command(aliases=['s'])
async def status (ctx, *, status1, amount=1):
    await ctx.channel.purge(limit=amount)
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f'{status1}'))

@client.command(aliases=['bt'])
async def Bad_Time (ctx, *, amount=1):
    await ctx.channel.purge(limit=amount)
    for i in range(1,2):
        await ctx.send('youre gonna have a bad time (-insert megalovania-)')

@client.command(aliases=['d'])
async def draw (ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('the creator has been given a doodlebook')

    def paint(event):
        global brush_size
        global color
        x1 = event.x - brush_size
        x2 = event.x + brush_size
        y1 = event.y - brush_size
        y2 = event.y + brush_size
        w.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    def brush_size_change(new_size):
        global brush_size
        brush_size = new_size

    def color_change(new_color):
        global color
        color = new_color
        
    root = Tk()
    root.title("Doodlepad")

    w = Canvas(root, width=canvas_width,
              height=canvas_height,
               bg="light blue")
    w.bind("<B1-Motion>", paint)

    red_btn = Button(text="red", width=10, command=lambda: color_change("red"))
    blue_btn = Button(text="blue", width=10, command=lambda: color_change("blue"))
    yellow_btn = Button(text="yellow",
                        width=10, command=lambda: color_change("yellow"))
    clear_btn = Button(text="clear", width=10, command=lambda: w.delete("all"))
    black_btn = Button(text="black", width=10,
                       command=lambda: color_change("black"))
    white_btn = Button(text="white", width=10, command=lambda: color_change("white"))


    five_btn = Button(text="5",width=10,command=lambda: brush_size_change(5))
    two_btn = Button(text="2",width=10,command=lambda: brush_size_change(2))
    three_btn = Button(text="3",width=10,command=lambda: brush_size_change(3))
    ten_btn = Button(text="10",width=10,command=lambda: brush_size_change(10))
    fifteen_btn = Button(text="15",width=10,command=lambda: brush_size_change(15))
    twenty_btn = Button(text="20",width=10,command=lambda: brush_size_change(20))


    w.grid(row=2, column=0, columnspan=7, padx=5, pady=5,
           sticky=E+W+S+N)
    w.columnconfigure(6, weight=1)
    w.rowconfigure(2, weight=2)

    red_btn.grid(row=0, column=2)
    blue_btn.grid(row=0, column=3)
    yellow_btn.grid(row=0, column=1)
    clear_btn.grid(row=0, column=6)
    black_btn.grid(row=0, column=5)
    white_btn.grid(row=0, column=4)

    five_btn.grid(row=1, column=3)
    three_btn.grid(row=1, column=2)
    two_btn.grid(row=1, column=1)
    ten_btn.grid(row=1, column=4)
    fifteen_btn.grid(row=1, column=5)
    twenty_btn.grid(row=1, column=6)

    root.mainloop()

@client.command(aliases=['n'])
async def Notepad (ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('the creator has been given a notebook')
    
    root = Tk()
    root.title("Notepad")


    text = Entry(width=100)
    text.grid(row=1, column=3)
    text2 = Entry(width=100)
    text2.grid(row=2, column=3)
    text3 = Entry(width=100)
    text3.grid(row=3, column=3)
    text4 = Entry(width=100)
    text4.grid(row=4, column=3)
    text5 = Entry(width=100)
    text5.grid(row=5, column=3)
    text6 = Entry(width=100)
    text6.grid(row=6, column=3)

    root.mainloop()

@client.command(aliases=['sa'])
async def say (ctx, *, what):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{what}')

@client.command(aliases=['e'])
async def ear (ctx):
    await ctx.channel.purge(limit=1)
    for i in range(1,5):
        await ctx.send('Protobot is awsome')
    await ctx.channel.purge(limit=5)

@client.command(aliases=['td1'])
async def turtledrawing1 (ctx):
    await ctx.channel.purge(limit=1)
    for i in range(1,50):
            forward(23)
            left(115)
            
@client.command(aliases=['cr'])
async def crash (ctx, *, i):
    await ctx.channel.purge(limit=1)
    for i in range(1,10):
            forward(25)
            left(45)


    
client.run('')
