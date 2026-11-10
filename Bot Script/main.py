import asyncio
import datetime
import discord
import os
from discord.ext import commands, tasks
from discord import ui
from discord import app_commands
from datetime import time
from zoneinfo import ZoneInfo
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = TOKEN = os.getenv("TOKEN")


intents = discord.Intents.all()        
bot = commands.Bot("m.", intents=intents, help_command=None)


async def carregarcogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            
            
@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=None)
    print(f"Bot Conectado: {bot.user}")
    
    
    
async def setup_hook():
    await carregarcogs()

bot.setup_hook = setup_hook
    
bot.run(BOT_TOKEN)
    
