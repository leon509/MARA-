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
async def on_ready():
    print(f"{bot.user} connecté")

async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start("TOKEN")

asyncio.run(main())