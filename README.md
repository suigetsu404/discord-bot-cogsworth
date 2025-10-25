[🇬🇧 English version](./README.md) | [🇵🇱 Wersja polska](./README_PL.md)
***
# Cogsworth - A Multipurpose Discord Bot

Cogsworth is a multipurpose Discord bot built with Python and the `discord.py` library. It integrates with external APIs and manages server utilities, moderation, and persistent user data using SQLite.

This project is built modularly using the "Cogs" system to ensure clean and scalable code.

---

## 🤖 AI & API Integration

* `?ask [question]`
    * Allows direct interaction with the Google Gemini AI.
    * **Note:** This command does not retain conversation history or context from previous messages.
* `?weather [city]`
    * Fetches the current weather forecast for a specified location.
* `?dictionary [word]`
    * Looks up the English definition of a word or phrase.

---

## 💾 Memory & Database (SQLite)

* `?remind [time] [message]`
    * Sets a reminder (e.g., "1h", "30m", "1d"). The bot will DM you when the time is up. Powered by `asyncio tasks.loop` and `sqlite3`.
* `?thx @user`
    * Gives a "karma" point to another user.
* `?karma [@user]`
    * Checks the karma point total for yourself or a mentioned user.

---

## 🛡️ Moderation

* `?kick @user [reason]`
    * Kicks a member from the server. Requires "Kick Members" permission.
* `?purge [amount]`
    * Deletes a specified number of messages from a channel. Requires "Manage Messages" permission.

---

## 🎉 Fun & Utilities

* `?poll [question]`
    * Creates a simple poll with (🟢/🟡/🔴) reactions.
* `?diceroll [sides]`
    * Rolls a die (default 6 sides).
* `?coinflip`
    * Flips a coin (Heads or Tails).
* `?8ball [question]`
    * Asks the magic 8-ball a question.
* `?user [@user]`
    * Displays information about a user (join date, account creation date).
* `?message [user_id] [message]`
    * Sends private message to the user.
---

## 🔔 Automated Listeners

* **Welcome:** Automatically greets new members in a designated channel.
* **Goodbye:** Posts a farewell message when a member leaves.

---

## 🛠️ Technology Stack

* **Python 3.10+**
* **discord.py** (For Discord API interaction and Cog management)
* **sqlite3** (For persistent data storage: reminders and karma)
* **google-generativeai** (For the Google Gemini API integration)
* **aiohttp** (For asynchronous API requests to weather and dictionary APIs)
* **asyncio** (For handling background tasks, e.g., the reminder loop)

---

## 🚀 How to Run

1.  Clone the repository:
    `git clone https://github.com/YourName/discord-bot-cogsworth.git`
2.  Navigate to the project directory:
    `cd discord-bot-cogsworth`
3.  Create and activate a virtual environment:
    `python -m venv venv`
    `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4.  Install the dependencies:
    `pip install -r requirements.txt`
5.  Create a `.env` file and fill in your API keys:
    ```
    DISCORD_TOKEN="YOUR_DISCORD_BOT_TOKEN"
    GEMINI_TOKEN="YOUR_GEMINI_API_KEY"
    WEATHER_TOKEN="YOUR_OPENWEATHERMAP_API_KEY"
    ```
6.  Run the bot:
    `python main.py`