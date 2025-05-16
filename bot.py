import telebot
import requests

# Replace with your real keys
TELEGRAM_BOT_TOKEN = '8008077466:AAHLXCTxdBaLdRxVU52G_ap2_MgjWYfCqNo'
DEEPSEEK_API_KEY = 'sk-bbca2c40c3bf462a99638ab045d62d7a'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "👋 Assalamualaikum! Mein aapka AI Assistant hoon. Aap mujhse koi bhi sawal pooch saktay hain.")

@bot.message_handler(func=lambda message: True)
def ai_chat(message):
    user_input = message.text

    headers = {
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=data
        )

        response.raise_for_status()
        reply = response.json()['choices'][0]['message']['content']
        bot.reply_to(message, reply)

    except Exception as e:
        bot.reply_to(message, "❌ Error aagya. Kripya dobara koshish karein.")

bot.polling()
