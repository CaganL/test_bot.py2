from telegram import Bot

# Bot token ve chat ID'yi buraya yaz
BOT_TOKEN = "8320997161:AAFuNcpONcHLNdnitNehNZ2SOMskiGva6Qs"
CHAT_ID = 7294398674

bot = Bot(BOT_TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Bot test mesajı başarılı ✅")
print("Mesaj gönderildi")
