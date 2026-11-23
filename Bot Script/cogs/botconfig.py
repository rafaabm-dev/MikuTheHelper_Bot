#Cogs: CONFIGURAÇÕES DE PERFIL DO BOT
import discord
import asyncio 
from discord import ui
from discord import app_commands
from discord.ext import commands

# Classe da Cog
class BotConfig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="status")
    @commands.is_owner()
    async def status(self, ctx:commands.Context, *,texto):
            atividade = discord.CustomActivity(status=discord.Status.do_not_disturb, name=texto)
            try:
                await self.bot.change_presence(activity=atividade)
                
                await ctx.reply("<:saba_cute:1530199260975337512> *Conectando Status...*")
            except Exception as e:
                await ctx.reply("💔 Não foi possível conectar o status")
        
    @commands.command(name="say")
    @commands.is_owner()
    async def say(self, ctx:commands.Context, *,falar):
        await ctx.send(falar)

async def setup(bot):
    await bot.add_cog(BotConfig(bot))