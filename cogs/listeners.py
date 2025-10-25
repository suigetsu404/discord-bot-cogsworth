from discord.ext import commands

class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot {self.bot.user} is online!")
        print("--------------------------")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"A new member joined {member}")
        channel_id = 1431398812244644001  # channel id where you want to greet members
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(f"Welcome {member.mention}!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"A member left {member}")
        channel_id = 1431398812244644001  # channel id where you want to greet members
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(f"Bye {member.mention}!")

async def setup(bot):
    await bot.add_cog(Listeners(bot))