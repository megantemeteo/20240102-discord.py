import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


#起動したときに起こるイベント
@bot.event
async def on_ready():
    print("準備完了")
    await bot.tree.sync()


#!ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


#/ping
@bot.tree.command(name="ping", description="Ping.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


bot.run("MTIxODE3MzAyNDAxNzA1OTg1MA.GhNXX2.EHu3VlG7pT2zk1c5yCc9ZP2-jJ9gwMCZ2HeEUM")
