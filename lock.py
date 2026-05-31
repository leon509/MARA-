import discord
from discord.ext import commands

class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lock(self, ctx):

        await ctx.channel.set_permissions(
            ctx.guild.default_role,
            send_messages=False
        )

        embed = discord.Embed(
            description="🔒 Salon verrouillé.",
            color=discord.Color.red()
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def unlock(self, ctx):

        await ctx.channel.set_permissions(
            ctx.guild.default_role,
            send_messages=True
        )

        embed = discord.Embed(
            description="🔓 Salon déverrouillé.",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Lock(bot))