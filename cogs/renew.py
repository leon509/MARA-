import discord
from discord.ext import commands

class Renew(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def renew(self, ctx):

        ancien = ctx.channel

        nouveau = await ancien.clone()

        await nouveau.edit(position=ancien.position)

        await ancien.delete()

        embed = discord.Embed(
            description="♻️ Salon recréé.",
            color=discord.Color.blue()
        )

        await nouveau.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Renew(bot))
