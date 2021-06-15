import telebot
from telebot import types

SMILE = ['↘️', '🇬🇧', '➡️', '↗️', '💰', '🇪🇺','🇺🇸', '🇯🇵', '🇷🇺']

bot = telebot.TeleBot('1837594513:AAFGpB23vmOtODWEms2B2qCbMhHYtnPBpYE')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/pairs')
    itembtn2 = types.KeyboardButton('/news')
    markup.add(itembtn1, itembtn2)
    msg = bot.send_message(message.chat.id, 
                    "Выберите команду для начала работы!", reply_markup=markup)

@bot.message_handler(commands=['pairs'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item3 = types.InlineKeyboardButton('🇪🇺|🇺🇸', callback_data='question_1')
    item4 = types.InlineKeyboardButton('🇬🇧|🇺🇸', callback_data='question_2')
    item5 = types.InlineKeyboardButton('🇺🇸|🇷🇺', callback_data='question_3')
    item6 = types.InlineKeyboardButton('🇺🇸|🇯🇵', callback_data='question_4')
    markup.add(item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Выбери валютную пару:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'question_1':
            bot.send_message(call.message.chat.id, 'Курс на сегодня = 1.21 💰 \nТренд: боковой ➡️ \nРекомендация - BUY ↗️ \nhttps://www.tradingview.com/x/tTX31P3X/')
        elif call.data == 'question_2':
            bot.send_message(call.message.chat.id, 'Курс на сегодня = 1.41 💰 \nТренд: боковой ➡️ \nРекомендация - SELL ↗️ \nhttps://www.tradingview.com/x/Nz8FgC5b/')
        elif call.data == 'question_3':
            bot.send_message(call.message.chat.id, 'Курс на сегодня = 71.77 💰 \nТренд: нисходящий ➡️ \nРекомендация - BUY ↗️ \nhttps://www.tradingview.com/x/tGols8eH/')
        elif call.data == 'question_4':
            bot.send_message(call.message.chat.id, 'Курс на сегодня = 109.36 💰 \nТренд: восходящий ➡️ \nРекомендация - BUY ↗️ \nhttps://www.tradingview.com/x/xtnMFIq6/')

@bot.message_handler(commands=['news'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_q = types.KeyboardButton('Европа')
    item_w = types.KeyboardButton('Великобритания')
    item_e = types.KeyboardButton('Россия')
    item_r = types.KeyboardButton('Япония')
    markup.add(item_q, item_w,item_e, item_r )
    msg = bot.send_message(message.chat.id, 
                    "Выберите страну!", reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def main(message):
    id = message.chat.id
    msg = message.text

    if msg == 'Европа':
         bot.send_message(id,'Вот данные по Еврозоне: \n14;45 - Ставка по депозитным средствам (июнь) ожидается -0,5% \n14;45 - ставка маржевого кредитования ЕЦБ ожидается 0,25% \n14;45 - заявление по монетарной политике ЕЦБ \n15;30 - пресс-конференция ЕЦБ')
    elif msg == 'Великобритания':
         bot.send_message(id,'Сегодня важных данных нет')
    elif msg == 'Россия':
         bot.send_message(id,'Сегодня важных данных нет')
    elif msg == 'Япония':
         bot.send_message(id,'Сегодня важных данных нет')
    elif msg == 'Привет':
         bot.send_message(id,'Привет!')
    else:
        bot.send_message(id,'Такой команды не существует, выберите доступную команду: \n/pairs - Обзор валютных пар! \n/news - Важные статистические данные на сегодня!')

    
   
    


bot.polling(none_stop=True)

