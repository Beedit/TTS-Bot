import asyncio
import discord
from discord.ext import commands
import os 
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()
servers = ["942042072083488768", "889094087595147295", "1021160480766709952"]
queue = []

# intents
intent=discord.Intents.default()
intent.message_content = True

bot = commands.Bot(debug_guilds=servers, intents=intent)

# This is here so if i decide to do something more fancy with it then its easier probably.
def tts(author, message):
    return gTTS(f"{author} said {message}")

# Prints a message when the bot comes online.
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

# Runs when a message is sent.
@bot.event
async def on_message(ctx):
    if ctx.author.bot == False:
        print(f"In {ctx.guild.name}, in channel {ctx.channel.name}, {ctx.author.name} said \"{ctx.content}\"")
        vc = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if vc != None:# and ("voice" in ctx.channel.name or "vc" in ctx.channel.name or "tts" in ctx.channel.name) : # <- This works i just dont want it for testing 
            if not vc.is_playing():
                message = tts(ctx.author.name, ctx.content)
                message.save("message.mp3")
                vc.play(discord.FFmpegPCMAudio(source="./message.mp3"))
            else:
                print("Playing already")
                queue.append([ctx.author.name, ctx.content])
                while vc.is_playing():
                    await asyncio.sleep(0.1)
                while queue[0] != [ctx.author.name, ctx.content]:
                    await asyncio.sleep(0.1)
                message = tts(queue[0][0], queue[0][1])
                message.save("message.mp3")
                await asyncio.sleep(0.3)
                vc.play(discord.FFmpegPCMAudio(source="./message.mp3"))
                queue.pop(0)


@bot.slash_command(name='join', guild_ids=servers, description='Tells the bot to join the voice channel')
async def join(ctx):
    try:
        await ctx.respond("Attempting to join VC!")
        await ctx.author.voice.channel.connect()
    except:
        await ctx.respond("You are not in a VC or the bot can't see it.")

@bot.slash_command(name='vars', guild_ids=servers, description='vars into terminal')
async def vars(ctx):
    print(queue)
    ctx.respond("q")
bot.run(os.getenv('TOKEN')) 