from discord.ext import commands, tasks
import discord
import sqlite3
import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.remind_loop.start()

    @tasks.loop(seconds=15)
    async def remind_loop(self):
        await self.bot.wait_until_ready()
        now_str = datetime.datetime.now().isoformat()
        connection = sqlite3.connect("bot.db")
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