from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


key_token = "6879284574:AAF9bqey4vKvQE5jBECaVTdB2Ml930xz-o8" #Masukkan KEY-TOKEN BOT 
user_bot = "Maaacaann_Bot" #Masukkan @user bot


async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan..")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo nama saya macan , kirim chat dan saya akan membalasss!!")


async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()


    greetings_triggers = ['halo', 'hallo', 'helo', 'hello']

    if any(greeting in text_lwr_diterima for greeting in greetings_triggers):
        await update.message.reply_text("Halo nama saya macan!!!")
    elif 'selamat malam' in text_lwr_diterima:
        await update.message.reply_text("Selamat malam..., jangan lupa istirahat 😊")
    elif 'siapa kamu ' in text_lwr_diterima:
        await update.message.reply_text(f"bot adalah : {user_bot}")
    elif 'terima kasih' in text_diterima:
        await update.message.reply_text("Sama-sama, senang bisa membantu!")
    elif 'apa kabar' in text_diterima:
        await update.message.reply_text("Saya bot, tidak memiliki perasaan, tapi terima kasih telah bertanya!")
    elif 'lagi apa' in text_diterima:
        await update.message.reply_text("Sedang di sini, siap melayani. Ada yang bisa saya bantu?")
    elif 'ada berita terbaru' in text_diterima:
        await update.message.reply_text("Maaf, saya bukan portal berita, tapi saya siap bercakap-cakap denganmu!")
    elif 'apa yang bisa kamu lakukan' in text_diterima:
        await update.message.reply_text("Saya bisa memberikan sapaan, memberikan informasi, dan banyak lagi. Coba saja tanyakan!")
    elif 'apa rencanamu hari ini' in text_diterima:
        await update.message.reply_text("Saya di sini untuk membantumu. Ada yang bisa saya bantu hari ini?")
    elif 'suka makan apa' in text_diterima:
        await update.message.reply_text("Saya bot, saya tidak bisa makan. Tapi, saya suka membantu! 😊")



async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)
