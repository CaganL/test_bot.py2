from telegram import Bot

# Telegram bilgilerin
BOT_TOKEN = "8320997161:AAFuNcpONcHLNdnitNehNZ2SOMskiGva6Qs"
CHAT_ID = 7294398674

# Botu başlat
bot = Bot(BOT_TOKEN)

# Test mesajı gönder
bot.send_message(chat_id=CHAT_ID, text="Bot test mesajı geldi! ✅")
print("Mesaj gönderildi!")
