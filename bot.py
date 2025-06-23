import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = 'ТВОЙ_ТОКЕН'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        "🛍 Открыть магазин",
        web_app=WebAppInfo(url="https://your-shop.vercel.app")  # замени на свой URL
    ))
    bot.send_message(message.chat.id, "Добро пожаловать в наш магазин! 👇", reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def handle_order(message):
    order = message.web_app_data.data
    bot.send_message(message.chat.id, f"✅ Заказ получен:\n\n{order}\n\n📦 Мы свяжемся с вами для доставки!")

bot.polling()
