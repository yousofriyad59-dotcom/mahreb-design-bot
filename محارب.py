from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters


# =========================
# التوكن
# =========================

TOKEN = "8841853429:AAFEEHpauM_euSOoGRpByfX-9isv1Sj75wg"


# =========================
# ملفات الخطوط
# =========================

files = {

    # الخطوط القديمة
    "2013": "BQACAgQAAxkBAAMRapy1mDURG_V_ome8RrmreUwFVGsAAiYPAALY-eBTle_JSXvOdtA9BA",
    "2005": "BQACAgQAAxkBAAMgapy68TMzO_2MwYuR_SVxCeSby3oAAiQPAALY-eBTiqwRkGFaNlU9BA",

    # خطوط التفسير
    "خط التفسير 1": "BQACAgQAAxkBAANUapzNKK6872umj4tUzsOE_s-AN8AAAjwiAAKm96lS3ddTkxC8s889BA",
    "خط التفسير 2": "BQACAgQAAxkBAANYapzSvRl-mWSMklwktoHbDfVzFdkAAkYiAAKm96lSLzJOxtQ7v3w9BA",
    "خط التفسير 3": "BQACAgQAAxkBAANlapzTQxaTLayFEStUh-UrM6YOrp8AAugaAAI3J-FTDUavOY1Vd_49BA",
    "خط التفسير 4": "BQACAgQAAxkBAANpapzTmuQl-iuL0XEb6LWbM5QmwKMAAmsdAALoxUhT0cxoRESI0-w9BA",

    # خطوط أخرى
    "خط 5": "",
    "خط 6": "",
    "خط 7": "",
    "خط 8": "",
    "خط 9": "",
    "خط 10": "",
    "خط 11": "",
    "خط 12": "",
    "خط 13": "",
    "خط 14": "",
    "خط 15": "",
    "خط 16": "",
    "خط 17": "",
    "خط 18": "",
    "خط 19": "",
    "خط 20": "",
}


# =========================
# أمر البداية
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بيك في محارب ديزاين ❤️\n\n"
        "اكتب اسم الخط أو الكود بتاعه."
    )


# =========================
# إرسال الخط
# =========================

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.strip()

    if text in files:

        file_id = files[text]

        if file_id == "":
            await update.message.reply_text(
                "⏳ الخط ده لسه مش متضاف."
            )
            return

        await update.message.reply_document(
            document=file_id,
            caption=f"📦 {text}"
        )


# =========================
# استقبال الملفات واستخراج File ID
# =========================

async def receive_file(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.document:

        file_id = update.message.document.file_id

        print("\n====================")
        print("FILE ID:")
        print(file_id)
        print("====================\n")

        await update.message.reply_text(
            "تم استلام الملف ✅\n"
            "بص على الـ Terminal هتلاقي الـ File ID."
        )


# =========================
# تشغيل البوت
# =========================

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(filters.Document.ALL, receive_file)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_text
        )
    )

    print("البوت يعمل الآن...")

    app.run_polling()


if __name__ == "__main__":
    main()