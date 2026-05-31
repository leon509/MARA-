import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong 🏓")

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def rename(self, ctx, member: discord.Member, *, pseudo):

        await member.edit(nick=pseudo)

        embed = discord.Embed(
            title="✏️ Pseudo Modifié",
            description=f"{member.mention} → **{pseudo}**",
            color=discord.Color.blue()
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def bingobook(self, ctx, cible: discord.Member, recompense, message, *, raison):

        embed = discord.Embed(
            title="BINGO BOOK 📕",
            color=discord.Color.red()
        )

        embed.add_field(
            name="🎯 Cible",
            value=f"{cible.mention}\n`{cible.name}`\n`{cible.id}`",
            inline=False
        )

        embed.add_field(
            name="🔥 Récompense",
            value=recompense,
            inline=False
        )

        embed.add_field(
            name="📨 Message à mettre",
            value=message,
            inline=False
        )

        embed.add_field(
            name="📄 Raison",
            value=raison,
            inline=False
        )

        embed.set_footer(
            text="BINGO BOOK • Vive la Mara 💎"
        )

        await ctx.send(embed=embed)
   
    @commands.command()
    async def mp(self, ctx, member: discord.Member, *, message):

        try:
            await member.send(message)

            embed = discord.Embed(
                title="✅ MP envoyé",
                description=f"Message envoyé à {member.mention}",
                color=discord.Color.green()
            )

            await ctx.send(embed=embed)

        except:
            await ctx.send("❌ Impossible d'envoyer le message")

async def setup(bot):
    await bot.add_cog(Utility(bot))