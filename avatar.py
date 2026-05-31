import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):

        if member is None:
            member = ctx.author

        # récupère les infos complètes du user
        user = await self.bot.fetch_user(member.id)

        embed = discord.Embed(
            title=f"🖼️ Profil de {member}",
            color=discord.Color.blue()
        )

        # PHOTO DE PROFIL
        embed.set_image(
            url=member.display_avatar.url
        )

        embed.add_field(
            name="📸 Avatar",
            value=f"[Clique ici]({member.display_avatar.url})",
            inline=False
        )

        # BANNIÈRE
        if user.banner:

            embed.add_field(
                name="🎨 Bannière",
                value=f"[Clique ici]({user.banner.url})",
                inline=False
            )

            embed.set_thumbnail(
                url=user.banner.url
            )

        else:

            embed.add_field(
                name="🎨 Bannière",
                value="❌ Aucune bannière",
                inline=False
            )

        embed.set_footer(
            text=f"ID : {member.id}"
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Avatar(bot))