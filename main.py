import discord
from discord.ext import commands
import os 
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()
bot = commands.Bot(debug_guilds=["942042072083488768", "1021160480766709952"], intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.event
async def on_message(ctx):
    if ctx.author.bot == False:
        print(f"In {ctx.guild.name}, in channel {ctx.channel.name}, {ctx.author.name} said \"{ctx.content}\"")
        message = gTTS(f"{ctx.author.name} said {ctx.content}")
        message.save("message.mp3")
        if discord.utils.get(bot.voice_clients, guild=ctx.guild) != None and (ctx.channel.name.contains("voice") or ctx.channel.name.contains("vc") or ctx.channel.name.contains("tts")) :
            await discord.utils.get(bot.voice_clients, guild=ctx.guild).play(discord.FFmpegPCMAudio(source="./message.mp3"))
            
@bot.slash_command(name='join', guild_ids=["942042072083488768", "889094087595147295", "1021160480766709952"], description='Tells the bot to join the voice channel')
async def join(ctx):
    await ctx.respond("Attempting to join VC.")
    vchannel = ctx.author.voice.channel
    await vchannel.connect()
bot.run(os.getenv('TOKEN')) 