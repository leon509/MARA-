import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="+",
    intents=intents,
    help_command=None
)

@bot.event
async def on_command(ctx):
    print(f"COMMANDE : {ctx.command} | {ctx.author}")

async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            print(f"Chargement : {file}")
            await bot.load_extension(f"cogs.{file[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("TOKEN"))

asyncio.run(main())
