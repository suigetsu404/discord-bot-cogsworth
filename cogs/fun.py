import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        print(f"Command /ping executed by: {ctx.author}")
        await ctx.send("pong")

    @commands.command()
    async def coinflip(self, ctx):
        print(f"Command /coinflip executed by: {ctx.author}")
        await ctx.send(random.choice(['Heads', 'Tails']))

    @commands.command()
    async def diceroll(self, ctx, d: int = 6):
        print(f"Command /diceroll executed by: {ctx.author}")
        try:
            await ctx.send(random.randint(1, d))
        except ValueError:
            await ctx.send("Invalid input, please enter a positive number.")
    @diceroll.error
    async def diceroll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Invalid input, please enter a positive number.")
        else:
            print(f"Unhandled error: {error}")

    @commands.command()
    async def avatar(self, ctx, user: discord.Member = None):
        print(f"Command /avatar executed by: {ctx.author}")
        if user is None:
            user = ctx.author
        await ctx.send(user.avatar.url)

    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, question: str = "Do you like me?"):
        print(f"Command /8ball executed by: {ctx.author}")
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it",
                     "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
                     "Don't count on it,", "My reply is no", "My sources say no", "Outlook not so good",
                     "Very doubtful", "Reply hazy, try again", "Ask again later", "Better not tell you now",
                     "Cannot predict now", "Concentrate and ask again"]
        await ctx.send(f"Your question was: {question}\n The answer is: {random.choice(responses)}")

    @commands.command()
    async def user(self, ctx, user: discord.Member = None):
        print(f"Command /user executed by: {ctx.author}")
        if user is None:
            user = ctx.author
        await ctx.send(f"Username: {user.name}\n"
                       f"Joined: {user.joined_at.strftime("%d/%m/%Y")}\n"
                       f"Created: {user.created_at.strftime("%d/%m/%Y")}")

    @commands.command()
    async def poll(self, ctx, *, question: str = "Do you like me?"):
        print(f"Command /poll executed by: {ctx.author}")
        emoji1 = self.bot.get_emoji(123456789012345678)  # emoji ids here
        emoji2 = self.bot.get_emoji(123456789012345678)
        emoji3 = self.bot.get_emoji(123456789012345678)
        if not emoji1 or not emoji2 or not emoji3:
            emoji1 = "🟢"
            emoji2 = "🟡"
            emoji3 = "🔴"
        poll_message = await ctx.send(question)
        await poll_message.add_reaction(emoji1)
        await poll_message.add_reaction(emoji2)
        await poll_message.add_reaction(emoji3)

async def setup(bot):
    await bot.add_cog(Fun(bot))