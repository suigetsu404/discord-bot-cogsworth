[🇬🇧 English version](./README.md) | [🇵🇱 Wersja polska](./README_PL.md)

[Add to Discord](https://discord.com/oauth2/authorize?client_id=1430896075933352017&permissions=76866&integration_type=0&scope=bot+applications.commands)
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

**Bot Logic & APIs:**
* Python 3.10+
* discord.py (Discord API, Cogs)
* google-generativeai (Google Gemini API)
* aiohttp (Async API requests for weather/dictionary)
* asyncio (Background tasks, e.g., reminder loop)

**Database:**
* sqlite3 (Persistent storage for karma and reminders)

**Infrastructure & Deployment (DevOps):**
* Oracle Cloud (OCI) VM (Hosting)
* Linux (Ubuntu) (Server OS)
* Git (Version Control)
* SSH (Server Management)
* tmux (Persistent session management)

---

## 🚀 Deployment

This bot is deployed and runs 24/7 on an **Oracle Cloud (OCI) Virtual Machine** (VM.Standard.E2.1.Micro "Always Free" tier).

* **Operating System:** The server runs on **Linux (Ubuntu)**.
* **Process:** The deployment involved manually configuring the server via **SSH**, setting up the environment (`python3-venv`, `pip`), cloning the repository with `Git`, and configuring environment variables.
* **Execution:** The application runs in the background as a persistent session managed by **`tmux`**.

---

## 🚀 How to Run

1.  Clone the repository:
    `git clone https://github.com/suigetsu404/discord-bot-cogsworth.git`
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

---

## ✉️ Contact

Feel free to reach out if you have any questions, suggestions, or collaboration inquiries.

* **Discord:** `suigetsu`
* **E-mail:** `szymonw0107 [at] gmail [dot] com`
