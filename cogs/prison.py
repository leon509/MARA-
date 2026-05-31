import discord
from discord.ext import commands
import asyncio

class Prison(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.prisonniers = {}

    @commands.command()
    @commands.has_permissions(move_members=True)
    async def prison(
        self,
        ctx,
        membre: discord.Member,
        duree: int,
        salon: discord.VoiceChannel
    ):

        if duree > 10:
            return await ctx.send(
                "❌ Maximum 10 minutes"
            )

        if not membre.voice:
            return await ctx.send(
                "❌ La personne doit être en vocal"
            )

        self.prisonniers[membre.id] = salon.id

        await membre.move_to(salon)

        embed = discord.Embed(
            title="🔒 Prison Vocale",
            description=(
                f"{membre.mention} emprisonné\n"
                f"⏰ Durée : {duree} minute(s)\n"
                f"🎤 Salon : {salon.name}"
            ),
            color=discord.Color.red()
        )

        await ctx.send(embed=embed)

        await asyncio.sleep(duree * 60)

        if membre.id in self.prisonniers:
            del self.prisonniers[membre.id]

            await ctx.send(
                f"🔓 {membre.mention} est maintenant libre"
            )

    @commands.command()
    @commands.has_permissions(move_members=True)
    async def unprison(
        self,
        ctx,
        membre: discord.Member
    ):

        if membre.id not in self.prisonniers:

            return await ctx.send(
                "❌ Cette personne n'est pas emprisonnée"
            )

        del self.prisonniers[membre.id]

        embed = discord.Embed(
            title="🔓 Prison retirée",
            description=f"{membre.mention} est libre",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(
        self,
        member,
        before,
        after
    ):

        if member.id in self.prisonniers:

            prison_channel_id = self.prisonniers[member.id]

            if (
                after.channel is None
                or after.channel.id != prison_channel_id
            ):

                channel = member.guild.get_channel(
                    prison_channel_id
                )

                await member.move_to(channel)

async def setup(bot):
    await bot.add_cog(Prison(bot))
