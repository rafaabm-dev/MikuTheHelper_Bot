# COGS: SERVIDOR

import discord
import os
from discord import app_commands
from discord.ext import commands
from discord import ui
from dotenv import load_dotenv

load_dotenv()
bml = GUILD = os.getenv("GUILD")
mikuid = BOTID = os.getenv("BOTID")
anunciarcanal = os.getenv("ANNOUNCEMENTCHANNEL")


# Classe da Cog
class BML(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    #Comandos de Prefixo
    @commands.command(name="anunciar")
    @commands.is_owner()
    async def anunciar(self, ctx:commands.Context, titulo: str, descricao: str):
        
        view = ui.LayoutView()
        view.add_item(ui.TextDisplay(f"{titulo}"))
        view.add_item(ui.Separator(spacing=discord.SeparatorSpacing.small))
        view.add_item(ui.TextDisplay(f"{descricao}"))
        view.add_item(ui.Separator(visible=False, spacing=discord.SeparatorSpacing.small))
        view.add_item(ui.TextDisplay(f"-# ** *Anúncio Oficial por MikuTheHelper Bot* **"))
        
        anúnciocanal = await self.bot.fetch_channel(anunciarcanal)
        
        try:
            await anúnciocanal.send(view=view)
            await ctx.reply("Anúncio Enviado!")
        except Exception as e:
            await ctx.reply("Occoreu um erro")
            
    # Grupo de Comandos
    bml = app_commands.Group(name="bml", description="Informações gerais do servidor")
    
    @bml.command(name="sobre", description="Informações sobre o servidor")
    async def sobre(self, interaction:discord.Interaction):
        
        server = await self.bot.fetch_guild(bml)
        svicon = server.icon.url if server.icon else None
        
        miku = await self.bot.fetch_user(mikuid)
        mkavatar = miku.display_avatar.url
        
        container = ui.Container(accent_color=discord.Color.red())
        seccao = ui.Section(
    "## <:dc_mod_decor:1514958235902152904> • Boom Lounge Community",
    accessory=ui.Thumbnail(svicon)
    )
        container.add_item(seccao)
        container.add_item(ui.Separator(spacing=discord.SeparatorSpacing.small))
        container.add_item(ui.TextDisplay("* <:coroa_BM:1498012224764117103> **Criado por:** <@1402358262631760023>\n* <:question_decor:1515069777914233043> **Aos:** ``10/04/26``\n* <:saba_cute:1530199260975337512> **Com:** *Muito ♥️*"))
        
        container2 = ui.Container(accent_color=discord.Color.blurple())
        seccao2 = ui.Section(
        "## <:Discord:1555080135047258183> • MikuTheHelper Bot",
        accessory=ui.Thumbnail(mkavatar)
        )
        container2.add_item(seccao2)
        container2.add_item(ui.Separator(spacing=discord.SeparatorSpacing.small))
        botao = ui.ActionRow(ui.Button(label="Ver Repositório", url="https://github.com/rafaabm-dev/MikuTheHelper_Bot", emoji="<:github:1573023481178886154>"))
        container2.add_item(ui.TextDisplay("* <:Discord:1555080135047258183> **discord.py:** ``2.7.1``\n* <:python:1555080227313553539> **Python:** ``3.14.6``\n* <:rule_decor:1514958523610562570> **Repositório:**"))
        container2.add_item(botao)
             
        view = ui.LayoutView()
        view.add_item(container)
        view.add_item(ui.Separator(spacing=discord.SeparatorSpacing.small))
        view.add_item(container2)
        
        await interaction.response.defer()
        await interaction.followup.send(view=view)
    
    
async def setup(bot):
    await bot.add_cog(BML(bot))