from telegram import Bot

# Telegram bilgilerin
BOT_TOKEN = "8320997161:AAFuNcpONcHLNdnitNehNZ2SOMskiGva6Qs"  # senin bot token
CHAT_ID = 7294398674  # senin chat ID

# Botu başlat
bot = Bot(BOT_TOKEN)

# Test mesajı gönder
bot.send_message(chat_id=CHAT_ID, text="Bot test mesajı geldi! ✅")
print("Mesaj gönderildi!")
