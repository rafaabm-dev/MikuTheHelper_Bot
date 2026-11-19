# COGS = COMANDOS DE STAFF

import discord
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
staffrole = STAFFROLE = os.getenv("STAFFROLE")

# Classe da Cog
class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # Grupo de Comandos
    staff = app_commands.Group(name="staff", description="Comandos de moderação")
        
    @staff.command(name="ajuda", description="Informações Staff")
    async def ajuda(self, interaction: discord.Interaction):
        membrostaff = any(role.id == staffrole_id for role in interaction.user.roles)
        
        embed = discord.Embed(
            title="Ajuda • Ataff", 
            description="*Seja bem-vindo ao painel de ajuda, o bot ainda está em desenvolvimento então não será possível exibir todos os comandos!*", 
            color=0x5865F2
        )
        
        if membrostaff:
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.followup.send("Este comando é exclusivo para membros da staff!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Staff(bot))
