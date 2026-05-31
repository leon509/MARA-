import discord
from discord.ext import commands
import asyncio
import random
import re


# ----------------------------
# PARSE DURATION
# ----------------------------
def parse_duration(duration: str) -> int:
    """
    Convertit:
    10m / 2h / 1j / 1j2h30m → secondes
    """
    pattern = r"(\d+)([mjh])"
    matches = re.findall(pattern, duration.lower())

    total = 0

    for value, unit in matches:
        value = int(value)

        if unit == "m":
            total += value * 60
        elif unit == "h":
            total += value * 3600
        elif unit == "j":
            total += value * 86400

    return total


# ----------------------------
# FORMAT TIMER
# ----------------------------
def format_time(seconds: int) -> str:
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60

    if days > 0:
        return f"{days}j {hours}h {minutes}m"
    if hours > 0:
        return f"{hours}h {minutes}m"
    if minutes > 0:
        return f"{minutes}m {sec}s"
    return f"{sec}s"


# ----------------------------
# COG
# ----------------------------
class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def giveaway(self, ctx, duree: str, winners: int, *, recompense: str):

        total_seconds = parse_duration(duree)

        if total_seconds <= 0:
            return await ctx.send("❌ Format invalide (ex: 10m, 2h, 1j, 1j2h30m)")

        embed = discord.Embed(
            title="🎉 GIVEAWAY",
            description=(
                f"🎁 Récompense : {recompense}\n"
                f"🏆 Gagnants : {winners}\n"
                f"⏰ Temps restant : {format_time(total_seconds)}\n\n"
                "Réagis avec 🎉 pour participer"
            ),
            color=discord.Color.gold()
        )

        embed.set_footer(text=f"Lancé par {ctx.author}")

        message = await ctx.send(embed=embed)
        await message.add_reaction("🎉")

        remaining = total_seconds

        # ----------------------------
        # COUNTDOWN LIVE
        # ----------------------------
        while remaining > 0:
            await asyncio.sleep(5)
            remaining -= 5

            if remaining < 0:
                remaining = 0

            embed.description = (
                f"🎁 Récompense : {recompense}\n"
                f"🏆 Gagnants : {winners}\n"
                f"⏰ Temps restant : {format_time(remaining)}\n\n"
                "Réagis avec 🎉 pour participer"
            )

            await message.edit(embed=embed)

        # ----------------------------
        # GET PARTICIPANTS
        # ----------------------------
        message = await ctx.channel.fetch_message(message.id)

        reaction = discord.utils.get(message.reactions, emoji="🎉")

        if not reaction:
            return await ctx.send("❌ Aucun participant")

        participants = [
            user async for user in reaction.users()
            if not user.bot
        ]

        if not participants:
            return await ctx.send("❌ Aucun participant")

        gagnants = random.sample(participants, min(winners, len(participants)))

        mentions = ", ".join(user.mention for user in gagnants)

        embed_end = discord.Embed(
            title="🎉 GIVEAWAY TERMINÉ",
            description=(
                f"🏆 Gagnants : {mentions}\n"
                f"🎁 Récompense : {recompense}"
            ),
            color=discord.Color.green()
        )

        await message.edit(embed=embed_end)
        await ctx.send(f"🎉 Félicitations {mentions} !")

    # ----------------------------
    # REROLL
    # ----------------------------
    @commands.command()
    async def reroll(self, ctx, message_id: int):

        try:
            message = await ctx.channel.fetch_message(message_id)
            reaction = discord.utils.get(message.reactions, emoji="🎉")

            if not reaction:
                return await ctx.send("❌ Aucun giveaway trouvé")

            participants = [
                user async for user in reaction.users()
                if not user.bot
            ]

            if not participants:
                return await ctx.send("❌ Aucun participant")

            gagnant = random.choice(participants)

            await ctx.send(f"🎉 Nouveau gagnant : {gagnant.mention}")

        except:
            await ctx.send("❌ Giveaway introuvable")


# ----------------------------
# SETUP (IMPORTANT)
# ----------------------------
async def setup(bot):
    await bot.add_cog(Giveaway(bot))
