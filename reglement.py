import discord
from discord.ext import commands

class Reglement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup_reglement(self, ctx, channel: discord.TextChannel, *, message: str):

        if not ctx.author.guild_permissions.administrator:
            return await ctx.send("❌ Tu n'as pas la permission.")

        embed = discord.Embed(
            title="📜 Règlement du serveur",
            description=message,
            color=discord.Color.blue()
        )

        embed.set_footer(text="Respect obligatoire")

        await channel.send(embed=embed)
        await ctx.send("✅ Règlement envoyé !")

        import discord
from discord.ext import commands

class AcceptView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="J'accepte", style=discord.ButtonStyle.green, emoji="✅")
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):

        await interaction.response.send_message(
            "✅ Tu as accepté le règlement.",
            ephemeral=True
        )

class Reglement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup_reglement(self, ctx, channel: discord.TextChannel, *, message: str):

        embed = discord.Embed(
            title="📜 Règlement du serveur",
            description=message,
            color=discord.Color.blue()
        )

        embed.set_footer(text="Clique sur le bouton pour accepter")

        await channel.send(
            embed=embed,
            view=AcceptView()
        )

        await ctx.send("✅ Règlement envoyé.")

async def setup(bot):
    await bot.add_cog(Reglement(bot))
    