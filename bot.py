from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8908221574:AAGq77dJDfQRtPvjWa3Hm30vGGjkKfrkEpI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom Sabina! Bot ishlayapti.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
app.run_polling()