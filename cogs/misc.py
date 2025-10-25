from discord.ext import commands
import discord

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def message(self, ctx, user_id, *, message):
        print(f"Command /message executed by: {ctx.author}")
        try:
            user = await self.bot.fetch_user(user_id)
            if user is None:
                await ctx.send("I couldn't find a user with that ID.")
                return
        except discord.NotFound:
            await ctx.send("I couldn't find a user with that ID.")
            return
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            return
        try:
            await user.send(message)
            await ctx.send(f"Successfully sent that message to **{user.name}**.")
        except discord.Forbidden:
            await ctx.send(f"I couldn't send that message. User **{user.name}** has his DM blocked.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
    @message.error
    async def message_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("User ID must be a number.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("'?message <userid> <message>'")
        else:
            print(f"An error occurred: {error}")

async def setup(bot):
    await bot.add_cog(Misc(bot))