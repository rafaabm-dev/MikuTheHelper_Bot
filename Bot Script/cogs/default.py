# COGS = COMANDOS DE AJUDA & BOT

import discord
from discord import app_commands
from discord.ext import commands

# Classe da Cog
class BotMiku(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Grupo de Comandos
    miku = app_commands.Group(name="miku", description="Informações gerais de Miku")
        
    @miku.command(name="ajuda", description="Painel de Ajuda do Bot")
    async def ajuda(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Ajuda", 
            description="*Seja bem-vindo ao painel de ajuda, o bot ainda está em desenvolvimento então não será possível exibir todos os comandos!*", 
            color=0x5865F2
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(BotMiku(bot))
