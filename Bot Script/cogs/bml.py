# COGS: INFORMAÇÕES DO SERVIDOR

import discord
import os
from discord import app_commands
from discord.ext import commands
from discord import ui
from dotenv import load_dotenv

load_dotenv()
bml = GUILD = os.getenv("GUILD")

# Classe da Cog
class BML(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Grupo de Comandos
    bml = app_commands.Group(name="bml", description="Informações gerais do servidor")
    
    @bml.command(name="sobre", description="Informações sobre o servidor")
    async def sobre(self, interaction:discord.Interaction):
        
        server = await self.bot.fetch_guild(bml)
        svicon = server.icon.url if server.icon else None
    
        container = ui.Container(accent_color=discord.Color.red())
        seccao = ui.Section(
    f"## <:dc_mod_decor:1514958235902152904> • Boom Lounge Community",
    accessory=ui.Thumbnail(svicon)
    )
        container.add_item(seccao)
        container.add_item(ui.Separator(spacing=discord.SeparatorSpacing.small))
        container.add_item(ui.TextDisplay("* TESTE"))
             
        view = ui.LayoutView()
        view.add_item(container)
        
        await interaction.response.send_message(view=view)
    
    
async def setup(bot):
    await bot.add_cog(BML(bot))