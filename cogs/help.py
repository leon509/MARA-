import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):

        embed = discord.Embed(
            title="📜 Commandes du Bot",
            description="Voici toutes les commandes disponibles.",
            color=discord.Color.blue()
        )

        # MODÉRATION
        embed.add_field(
            name="🛡️ Modération",
            value=(
                "`+lock` → Verrouiller un salon\n"
                "`+unlock` → Déverrouiller un salon\n"
                "`+clear <nombre>` → Supprimer des messages\n"
                "`+renew` → Recréer le salon"
            ),
            inline=False
        )

        # GIVEAWAY
        embed.add_field(
            name="🎉 Giveaway",
            value=(
                "`+giveaway <durée> <gagnants> <récompense>`\n"
                "`+reroll <id_message>`"
            ),
            inline=False
        )

        # REGLEMENT
        embed.add_field(
            name="📖 Règlement",
            value=(
                "`+setup_reglement #salon message`\n"
                "Bouton ✅ J'accepte inclus"
            ),
            inline=False
        )

        # PRISON
        embed.add_field(
            name="⛓️ Prison",
            value=(
                "`+prison @membre`\n"
                "`+unprison @membre`\n"
                "`+jail @membre`\n"
                "`+unjail @membre`"
            ),
            inline=False
        )

        # CONFESSION
        embed.add_field(
            name="🙈 Confession",
            value=(
                "`+confess message`\n"
                "`+confession message`"
            ),
            inline=False
        )

        # UTILITY
        embed.add_field(
            name="🛠️ Utility",
            value=(
                "`+ping`\n"
                "`+avatar @membre`\n"
                "`+userinfo @membre`\n"
                "`+serverinfo`"
            ),
            inline=False
        )

        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)

        embed.set_footer(
            text=f"Demandé par {ctx.author}",
            icon_url=ctx.author.avatar.url if ctx.author.avatar else None
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
