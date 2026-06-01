import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        print("PING EXECUTE")
        await ctx.send("Pong 🏓")

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def rename(self, ctx, member: discord.Member, *, pseudo):
        await member.edit(nick=pseudo)
        await ctx.send(f"✏️ {member.mention} renommé en **{pseudo}**")

    @commands.command()
    async def mp(self, ctx, member: discord.Member, *, message):
        try:
            await member.send(message)
            await ctx.send(f"✅ MP envoyé à {member.mention}")
        except:
            await ctx.send("❌ Impossible d'envoyer le message")

async def setup(bot):
    await bot.add_cog(Utility(bot))
