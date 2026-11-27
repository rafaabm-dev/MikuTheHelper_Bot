# COGS = LOGS DO SERVER

import discord
import os
from discord import ui
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
logchannel = LOGCHANNEL = os.getenv("LOGCHANNEL")

# Classe da Cog
class EventLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Eventos de Log
    
    # Mensagem Editada
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        
        if before.author.bot:
            return
            
            
        user = before.author
        msg_antiga = before.content
        msg_nova = after.content
        
        logcanal = await self.bot.fetch_channel(logchannel)
        
        
        if msg_antiga == msg_nova:
            return
        
        container = ui.Container(accent_color=discord.Colour.yellow())
        container.add_item(ui.TextDisplay("## <:automod_decor:1514958344883011614>   *Mensagem Editada*"))
        container.add_item(ui.Separator(spacing=discord.SeparatorSpacing.small))
        container.add_item(ui.TextDisplay(f"** Por {user.mention} • {user.id} **"))
        container.add_item(ui.TextDisplay(f"**Mensagem Antiga:**\n``{msg_antiga}``\n\n**Mensagem Nova:**\n``{msg_nova}``"))
        
        view = ui.LayoutView()
        view.add_item(container)
        
        await logcanal.send(view=view)
        
    # Mensagem Apagada
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        
        if message.author.bot:
            return
            
        user2 = message.author
        msg = message.content
        
        logcanal2 = await self.bot.fetch_channel(logchannel)
        
        container2 = ui.Container(accent_color=discord.Colour.red())
        container2.add_item(ui.TextDisplay("## <:automod_decor:1514958344883011614>   *Mensagem Apagada*"))
        container2.add_item(ui.Separator(spacing=discord.SeparatorSpacing.small))
        container2.add_item(ui.TextDisplay(f"** Por {user2.mention} • {user2.id} **"))
        container2.add_item(ui.TextDisplay(f"**Mensagem:**\n``{msg}``"))
        
        view2 = ui.LayoutView()
        view2.add_item(container2)
        
        await logcanal2.send(view=view2)
        
async def setup(bot):
    await bot.add_cog(EventLog(bot))