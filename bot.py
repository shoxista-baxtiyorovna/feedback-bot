import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler, filters
from dotenv import load_dotenv

load_dotenv()


ADMIN_ID = int(os.getenv("ADMIN_ID"))
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    message = update.message.text
    fullname = f"{user.first_name} {user.last_name or ''}".strip()

    text_to_send = f"📩 Yangi xabar:\n👤 Foydalanuvchi: {fullname} (@{user.username or 'username yo‘q'})\n\n📝 Xabar:\n{message}"

    await context.bot.send_message(chat_id=ADMIN_ID, text=text_to_send)
    await update.message.reply_text("✅ Xabaringiz yuborildi!")


# Komitetlar ro'yxati
committees = [
    "General Assembly",
    "HRC",
    "UN Women",
    "UNODC",
    "UNESCO",
    "Security Council",

]

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(text=committee, callback_data=committee)] for committee in committees
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to the UCraftMUN Gossip Box! 👋\n\nPlease select your committee:",
        reply_markup=reply_markup
    )

# Komitet tanlanganda chaqiriladigan funksiya
async def handle_committee_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    selected_committee = query.data
    context.user_data["committee"] = selected_committee  # foydalanuvchi uchun komitetni saqlaymiz

    await query.edit_message_text(
        text=f"You selected *{selected_committee}*.\nNow send your message 👇",
        parse_mode='Markdown'
    )

# (adminning) chat ID'si
ADMIN_CHAT_ID = ADMIN_ID

# Foydalanuvchi matn yuborganda
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    committee = context.user_data.get("committee", "Unknown")
    user = update.effective_user

    text = update.message.text

    message_to_admin = (
        f"🗣 *New Message from {user.first_name} (@{user.username}):*\n"
        f"*Committee:* {committee}\n"
        f"*Message:* {text}"
    )

    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=message_to_admin,
        parse_mode='Markdown'
    )

    await update.message.reply_text("✅ Your message was successfully sent!")


app = ApplicationBuilder().token(BOT_TOKEN).build()
print("Bot ishlayapti...")
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_committee_selection))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

app.run_polling()