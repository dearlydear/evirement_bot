
import discord
import discord.ext import commands
import random, os

intents = discord.Intents.default()
intents.message_content =  True

bot = commands.Bot(commands_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print('BOT TELAH SIAP!')

bot.command()
async def ide(ctx):
    img_name = random.choice(os.lisdir('kerajinan'))
    with open(f'kerajinan/{img_name}', ' rb') as gambar:
        picture = discord.File(gambar)
    await ctx.send(picture)

    bot.run('your token')
