from discord.ext import commands
import os
import urllib.parse
import google.generativeai as genai
import aiohttp

from Bot.cogs.memory import Memory


class Api(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, *, city_name: str = "London"):
        print(f"Command /weather executed by: {ctx.author}")
        WEATHER_API_KEY = os.getenv('WEATHER_TOKEN')
        parsed_city_name = urllib.parse.quote_plus(city_name)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={parsed_city_name}&appid={WEATHER_API_KEY}&units=metric"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    temperature = data["main"]["temp"]
                    description = data["weather"][0]["description"]
                    emoji_id = data["weather"][0]["icon"]
                    emoji_dictionary = {
                        ("01d", "01n"): ":sun:",
                        ("02d", "02n"): ":partly_sunny:",
                        ("03d", "03n", "04d", "04n"): ":cloud:",
                        ("09d", "09n"): ":cloud_rain:",
                        ("10d", "10n"): ":white_sun_rain_cloud:",
                        ("11d", "11n"): ":thunder_cloud_rain:",
                        ("13d", "13n"): ":cloud_snow:",
                        ("50d", "50n"): ":fog:",
                    }
                    emoji = None
                    for key, value in emoji_dictionary.items():
                        if emoji_id in key:
                            emoji = value
                            break
                    await ctx.send(f"The weather in {city_name} is: {description}, {temperature}°C {emoji}")
                elif response.status == 401:
                    await ctx.send("Error: My API key is invalid. Please contact an admin.")
                elif response.status == 404:
                    await ctx.send(f"Error: I couldn't find a city called **{city_name}**.")
                elif response.status == 429:
                    await ctx.send("Error: Too many requests, please try again later.")
                else:
                    await ctx.send(f"Unexpected error occured. Please contact an admin. (Status: {response.status}).")

    @commands.command()
    async def dictionary(self, ctx, *, word: str = "Dictionary"):
        print(f"Command /dictionary executed by: {ctx.author}")
        parsed_word = urllib.parse.quote_plus(word)
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{parsed_word}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    text_list = []
                    header = f"{word.capitalize()} definitions:\n"
                    print(data[0]["meanings"][0]["definitions"])
                    print(len(data[0]["meanings"][0]["definitions"]))
                    for i in range(len(data[0]["meanings"][0]["definitions"])):
                        definition = data[0]["meanings"][0]["definitions"][i]["definition"]
                        if len(definition) > 1900:
                            definition = definition[:1900] + "... (truncated)"
                        text_list.append(f"{i + 1}. {definition}\n")
                    message = header
                    for definition in text_list:
                        if len(message) + len(definition) > 2000:
                            await ctx.send(message)
                            message = definition
                        else:
                            message += definition
                    if message:
                        await ctx.send(message)
                elif response.status == 404:
                    await ctx.send(f"Error: I couldn't find the word **{word}**.")
                elif response.status == 429:
                    await ctx.send("Error: Too many requests, please try again later.")
                else:
                    await ctx.send(f"Unexpected error occured. Please contact an admin. (Status: {response.status}).")

    @commands.command()
    async def ask(self, ctx, *, message):
        print(f"Command /ask executed by: {ctx.author}")
        await ctx.typing()
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = await model.generate_content_async(message)
            final_response = response.text
            if len(final_response) <= 2000:
                await ctx.send(final_response)
            else:
                for i in range(0, len(final_response), 2000):
                    part = final_response[i:i+2000]
                    await ctx.send(part)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(Api(bot))