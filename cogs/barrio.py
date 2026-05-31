import discord
from discord.ext import commands

OWNER_ID = 740607879173898332

class Barrio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # role_id : owner_id
        self.role_owners = {}

    @commands.command()
    async def barrio(self, ctx, cible=None):

        # =========================
        # PRENDRE UN ROLE
        # +barrio @ROLE
        # =========================

        if ctx.message.role_mentions:

            role = ctx.message.role_mentions[0]

            if role.id in self.role_owners:

                return await ctx.send(
                    "❌ Ce rôle possède déjà un propriétaire"
                )

            self.role_owners[role.id] = ctx.author.id

            await ctx.author.add_roles(role)

            embed = discord.Embed(
                title="💎 Barrio pris",
                description=(
                    f"{ctx.author.mention} possède maintenant "
                    f"le rôle {role.mention}"
                ),
                color=discord.Color.gold()
            )

            return await ctx.send(embed=embed)

        # =========================
        # DONNER LE ROLE
        # +barrio @PERSONNE
        # =========================

        if ctx.message.mentions:

            membre = ctx.message.mentions[0]

            role_trouve = None

            for role_id, owner_id in self.role_owners.items():

                if owner_id == ctx.author.id:

                    role_trouve = ctx.guild.get_role(role_id)
                    break

            if role_trouve is None:

                return await ctx.send(
                    "❌ Tu ne possèdes aucun rôle"
                )

            await membre.add_roles(role_trouve)

            embed = discord.Embed(
                title="💎 Rôle donné",
                description=(
                    f"{membre.mention} a reçu "
                    f"le rôle {role_trouve.mention}"
                ),
                color=discord.Color.green()
            )

            return await ctx.send(embed=embed)

        await ctx.send(
            "❌ Utilisation : +barrio @ROLE ou +barrio @MEMBRE"
        )

    @commands.command()
    async def unclaim(self, ctx, role: discord.Role):

        if ctx.author.id != OWNER_ID:

            return await ctx.send(
                "❌ Commande propriétaire uniquement"
            )

        if role.id not in self.role_owners:

            return await ctx.send(
                "❌ Ce rôle n'a pas de propriétaire"
            )

        del self.role_owners[role.id]

        embed = discord.Embed(
            title="🗑️ Barrio supprimé",
            description=(
                f"Le rôle {role.mention} "
                f"n'a plus de propriétaire"
            ),
            color=discord.Color.red()
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Barrio(bot))
