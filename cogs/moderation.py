from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge(self, ctx, amount: int):
        print(f"Command /purge executed by: {ctx.author}")
        if not ctx.author.guild_permissions.manage_messages:
            ctx.send("You do not have permissions to use this command.")
            return
        try:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"Successfully purged **{amount}** messages.", delete_after=3)
        except discord.errors.Forbidden:
            await ctx.send("I don't have permissions to use this command.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command()
    async def kick(self, ctx, user: discord.Member = None, *, reason: str = None):
        print(f"Command /kick executed by: {ctx.author}")
        if not ctx.author.guild_permissions.kick_members:
            await ctx.send("You do not have permissions to use this command.")
            return
        if user is None:
            await ctx.send("You must mention a user to kick them.")
            return
        if user == ctx.author:
            await ctx.send("You cannot kick yourself.")
            return
        try:
            await user.kick(reason=reason)
            await ctx.send(f"Successfully kicked **{user.name}**.", delete_after=3)
        except discord.errors.Forbidden:
            await ctx.send("I don't have permissions to use this command.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("I couldn't find any user with that name.")
        else:
            await ctx.send(f"An error occurred: {error}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))