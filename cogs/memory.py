from discord.ext import commands, tasks
import discord
import sqlite3
import datetime

class Memory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.remind_loop.start()

    @tasks.loop(seconds=15)
    async def remind_loop(self):
        await self.bot.wait_until_ready()
        now_str = datetime.datetime.now().isoformat()
        connection = sqlite3.connect("data/bot.db")
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM reminders WHERE remind_time <= ?", (now_str,))
            reminders = cursor.fetchall()
            for row in reminders:
                reminder_id = row[0]
                user_id = int(row[1])
                channel_id = int(row[2])
                message = row[4]
                print(f"Reminding! ID: {reminder_id} to {user_id}")
                try:
                    user = await self.bot.fetch_user(user_id)
                    if user:
                        await user.send(f"Reminding: {message}")
                    else:
                        channel = self.bot.get_channel(channel_id)
                        if channel:
                            await channel.send(f"Reminding <@{user_id}>: {message}")
                        else:
                            print(f"I couldn't find a channel with ID: {channel_id}.")
                    cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
                except Exception as e:
                    print(f"An error occurred {reminder_id}: {e}")
            connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()

    @commands.command()
    async def thx(self, ctx, user: discord.Member = None):
        print(f"Command /thx executed by: {ctx.author}")
        if user == ctx.author:
            await ctx.send("You cannot thx yourself.")
            return
        try:
            connection = sqlite3.connect("data/bot.db")
            cursor = connection.cursor()
            cursor.execute(f"INSERT OR IGNORE INTO karma (user_id, points) VALUES (?, 0)", (user.id,))
            cursor.execute(f"UPDATE karma SET points = points + 1 WHERE user_id = ?", (user.id,))
            connection.commit()
            connection.close()
            await ctx.send(f"Successfully thxed **{user.name}**.", delete_after=3)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command()
    async def karma(self, ctx, user: discord.Member = None):
        print(f"Command /karma executed by: {ctx.author}")
        if user is None:
            user = ctx.author
        try:
            connection = sqlite3.connect("data/bot.db")
            cursor = connection.cursor()
            cursor.execute(f"SELECT points FROM karma WHERE user_id = ?", (user.id,))
            result = cursor.fetchone()
            if result is None:
                points = 0
            else:
                points = result[0]
            await ctx.send(f"**{user.name}** has **{points}** points.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @karma.error
    async def karma_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("I couldn't find any user with that name.")
        else:
            await ctx.send(f"An error occurred: {error}")

    @commands.command()
    async def remind(self, ctx, time: str, *, message):
        print(f"Command /remind executed by: {ctx.author}")
        try:
            parsed_time = parse_time_to_seconds(time)
            if parsed_time is None:
                await ctx.send("Invalid time format. Please use 's', 'm', 'h' or 'd' (e.g. 10m)")
                return
            date_time = datetime.datetime.now() + datetime.timedelta(seconds=parsed_time)
            date_time_str = date_time.isoformat()
            connection = sqlite3.connect("data/bot.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO reminders (user_id, channel_id, remind_time, message) VALUES (?, ?, ?, ?)",
                           (ctx.author.id, ctx.channel.id, date_time_str, message))
            connection.commit()
            connection.close()
            await ctx.send(f"I'll remind you about {message} in {time}.")
        except Exception as e:
            print(f"An error occurred: {e}")

def parse_time_to_seconds(time_str: str):
    unit = time_str[-1].lower()
    try:
        time_int = int(time_str[:-1])
        match unit:
            case 's':
                return time_int
            case 'm':
                return time_int * 60
            case 'h':
                return time_int * 60 * 60
            case 'd':
                return time_int * 60 * 60 * 24
            case _:
                return None
    except ValueError:
        return None

async def setup(bot):
    await bot.add_cog(Memory(bot))