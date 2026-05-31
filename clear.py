import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: int):

        await ctx.channel.purge(limit=amount + 1)

        msg = await ctx.send(f"🧹 {amount} messages supprimés.")

        await msg.delete(delay=3)

async def setup(bot):
    await bot.add_cog(Clear(bot))