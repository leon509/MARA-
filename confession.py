import discord
from discord.ext import commands

CONFESSION_CHANNEL = "📜⥐confessions"

class Confession(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def confess(self, ctx, *, message):

        salon = discord.utils.get(
            ctx.guild.text_channels,
            name=CONFESSION_CHANNEL
        )

        if not salon:
            return await ctx.send("❌ Salon confession introuvable")

        embed = discord.Embed(
            title="📩 Confession MARA",
            description=message,
            color=discord.Color.dark_purple()
        )

        embed.set_footer(
            text="VIVA LA MARA"
        )

        await salon.send(embed=embed)

        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Confession(bot))