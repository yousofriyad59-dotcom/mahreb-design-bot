import os
import httpx

from fastapi import FastAPI, Request

# =========================
# التوكن
# =========================
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN غير موجود في Environment Variables")

# =========================
# ملفات الخطوط
# =========================
files = {
    "2013": "BQACAgQAAxkBAAMRapy1mDURG_V_ome8RrmreUwFVGsAAiYPAALY-eBTle_JSXvOdtA9BA",
    "2005": "BQACAgQAAxkBAAMgapy68TMzO_2MwYuR_SVxCeSby3oAAiQPAALY-eBTiqwRkGFaNlU9BA",

    "خط التفسير 1": "BQACAgQAAxkBAANUapzNKK6872umj4tUzsOE_s-AN8AAAjwiAAKm96lS3ddTkxC8s889BA",
    "خط التفسير 2": "BQACAgQAAxkBAANYapzSvRl-mWSMklwktoHbDfVzFdkAAkYiAAKm96lSLzJOxtQ7v3w9BA",
    "خط التفسير 3": "BQACAgQAAxkBAANlapzTQxaTLayFEStUh-UrM6YOrp8AAugaAAI3J-FTDUavOY1Vd_49BA",
    "خط التفسير 4": "BQACAgQAAxkBAANpapzTmuQl-iuL0XEb6LWbM5QmwKMAAmsdAALoxUhT0cxoRESI0-w9BA",

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
# تطبيق الويب
# =========================
app = FastAPI()


# =========================
# التواصل مع Telegram
# =========================
async def telegram(method, data):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"

    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data)
        return response.json()


# =========================
# الصفحة الرئيسية
# =========================
@app.get("/")
async def home():
    return {"status": "محارب ديزاين يعمل ✅"}


# =========================
# استقبال رسائل Telegram
# =========================
@app.post("/webhook")
async def webhook(request: Request):
    update = await request.json()

    message = update.get("message")

    if not message:
        return {"ok": True}

    chat = message.get("chat", {})
    chat_id = chat.get("id")

    # =========================
    # استقبال ملف واستخراج File ID
    # =========================
    if message.get("document"):
        file_id = message["document"].get("file_id")

        await telegram(
            "sendMessage",
            {
                "chat_id": chat_id,
                "text": (
                    "تم استلام الملف ✅\n\n"
                    "File ID:\n"
                    f"{file_id}"
                ),
            },
        )

        return {"ok": True}

    # =========================
    # استقبال النص
    # =========================
    text = message.get("text", "").strip()

    # =========================
    # /start
    # =========================
    if text == "/start":
        await telegram(
            "sendMessage",
            {
                "chat_id": chat_id,
                "text": (
                    "أهلاً بيك في محارب ديزاين ❤️\n\n"
                    "اكتب اسم الخط أو الكود بتاعه."
                ),
            },
        )

        return {"ok": True}

    # =========================
    # إرسال الخط
    # =========================
    if text in files:
        file_id = files[text]

        if file_id == "":
            await telegram(
                "sendMessage",
                {
                    "chat_id": chat_id,
                    "text": "⏳ الخط ده لسه مش متضاف.",
                },
            )

            return {"ok": True}

        await telegram(
            "sendDocument",
            {
                "chat_id": chat_id,
                "document": file_id,
                "caption": f"📦 {text}",
            },
        )

        return {"ok": True}

    return {"ok": True}
