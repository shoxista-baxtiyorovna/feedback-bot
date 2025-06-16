# 🤖 Feedback Telegram Bot

A simple and user-friendly Telegram bot that allows users to send feedback directly to the admin. Ideal for collecting ideas, complaints, or suggestions from a community or team.

---

## ✨ Features

- 📩 Message with identity
- 🔐 Admin-only access to received messages
- ⚙️ Easy to configure with environment variables
- 🚀 Deployable to platforms like Railway or Render

---

## 🚀 Deployment Guide

1. **Clone the project**
   ```bash
   git clone https://github.com/your-username/feedback-bot.git
   cd feedback-bot

2. **Create a .env file:**

    ```env

    BOT_TOKEN=your_telegram_bot_token
    ADMIN_ID=your_telegram_id

3. **Install requirements:**

    ```bash

    pip install -r requirements.txt

4. **Run the bot:**

    ```bash

    python bot.py
   
---
   
## ⚙️ Environment Variables
| Variable    | Description              |
|-------------|--------------------------|
| `BOT_TOKEN` | Token from BotFather     |
| `ADMIN_ID`  | Your personal Telegram ID |

## 🛠️ Built With

- python-telegram-bot

- dotenv

## 📬 Feedback
Have suggestions or issues? Feel free to open an issue or send feedback through the bot itself 😉
