import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove
bot = telebot.TeleBot("7044157262:AAHigeqpw8C7EojD4Bje_00rnjhRKvfgRxY")


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()

    question = types.InlineKeyboardButton('Вернуться в начало', callback_data='start')
    markup0 = types.InlineKeyboardMarkup() 
    markup0.row(question)   
    question1 = types.InlineKeyboardButton('Что такое структурный инвестиционный продукт?', callback_data='question1')
    question2 = types.InlineKeyboardButton('Какой структурный продукт мне подойдет?', callback_data='question2')
    markup.row(question1)
    markup.row(question2)
    bot.send_message( message.chat.id, 'Привет, {first}! Я бот по подбору структурного инвестиционного продукта. Я отвечу на вопросы и помогу выбрать подходящий продукт'.format(first=message.from_user.first_name))
    bot.send_message( message.chat.id, 'Что тебя интересует?', reply_markup=markup)
    @bot.callback_query_handler(func = lambda callback: True)
    def callback_question(callback):
        if callback.data == 'question1':
            question1 = types.InlineKeyboardButton('Расскажи подробнее о каждом продукте', callback_data='question1.1')
            question2 = types.InlineKeyboardButton('Перейти к выбору продукта', callback_data='question2')
            markup1 = types.InlineKeyboardMarkup()
            markup1.row(question1)
            markup1.row(question2)
            bot.send_message(callback.message.chat.id, 'Структурный инвестиционный продукт — это конструктор из нескольких финансовых инструментов. В его состав входят рисковые активы (базовый актив, который приносит доход): акции, фьючерсы, опционы и т.д. и защитные (та часть денег, которая вернется 100%): депозит или облигация. В зависимости от пропорций распределения финансов между рисковой и защитной частью, структурные продукты делятся на три категории:\
С полной защитой капитала, они подойдут осторожным инвесторам.\
С частичной защитой капитала.\
Без защиты капитала, подойдут только самым опытным инвесторам. Такие продукты часто бессрочные.', reply_markup=markup1)
        if callback.data == 'question1.1':
            question1 = types.InlineKeyboardButton('Перейти к выбору продукта', callback_data='question2')
            markup2 = types.InlineKeyboardMarkup()
            markup2.row(question1)
            bot.send_message(callback.message.chat.id, 'Продукт с полной защитой капитала (низкорискованные продукты) характеризуется риском в 10% от общей суммы вклада. Лучший период для вложения: низкая волатильность рынка, в этом случае доход от структурного продукта гарантирован.\
Продукт с частичной защитой капитала (Умеренные продукты) характеризуется риском от 10 до 50% от общей суммы вклада. Умеренная рискованность продукта. Подходит инвесторам, готовым рисковать, но не сильно.\
Продукт без защиты капитала (Высокорисковые продукты) характеризуется риском большей частью вложенной суммы, однако при этом имеет более высокую доходность. Наиболее выгодно вкладываться в период высокой волатильности рынка, когда у базового актива есть возможность резко вырасти в цене.', reply_markup=markup2)
        if callback.data == 'question2':
            question1 = types.InlineKeyboardButton('Высокорисковые продукты', callback_data='answer1')
            question2 = types.InlineKeyboardButton('Умеренные продукты', callback_data='answer2')  
            question3 = types.InlineKeyboardButton('Низкорискованные продукты', callback_data='answer3')
            question4 = types.InlineKeyboardButton('Расскажи подробнее о каждом продукте', callback_data='question1.1')
            markup3 = types.InlineKeyboardMarkup()
            markup3.row(question1) 
            markup3.row(question2) 
            markup3.row(question3)
            markup3.row(question4)   
            bot.send_message(callback.message.chat.id, 'Вас интересуют высокорисковые, умеренные или низкорискованные продукты?', reply_markup=markup3)  
        if callback.data == 'answer1':
            question1 = types.InlineKeyboardButton('10% депозит + 90% базовый актив', callback_data='answer1.1')
            question2 = types.InlineKeyboardButton('10% Облигация + 90% базовый актив', callback_data='answer1.2')  
            question3 = types.InlineKeyboardButton('Комбинация из базовых активов', callback_data='answer1.3')
            markup4 = types.InlineKeyboardMarkup()
            markup4.row(question1)  
            markup4.row(question2)
            markup4.row(question3) 
            bot.send_message(callback.message.chat.id, 'Какая комбинация вас интересует?', reply_markup=markup4) 
        if callback.data == 'answer2':
            question1 = types.InlineKeyboardButton('50 - 90% Депозит + 10 - 50% базовый актив', callback_data='answer2.1')
            question2 = types.InlineKeyboardButton('50 - 90% Облигация + 10 - 50% базовый актив', callback_data='answer2.2') 
            markup5 = types.InlineKeyboardMarkup()
            markup5.row(question1) 
            markup5.row(question2)  
            bot.send_message(callback.message.chat.id, 'Какой вариант финансовых инструментов вас интересует?', reply_markup=markup5)
        if callback.data == 'answer3':
            question1 = types.InlineKeyboardButton('90% Депозит + 10% базовый актив', callback_data='answer3.1')
            question2 = types.InlineKeyboardButton('90% Облигация + 10% базовый актив', callback_data='answer3.2') 
            markup6 = types.InlineKeyboardMarkup()
            markup6.row(question1) 
            markup6.row(question2)  
            bot.send_message(callback.message.chat.id, 'Какой вариант финансовых инструментов вас интересует?', reply_markup=markup6)  
        if callback.data == 'answer1.1':
            question1 = types.InlineKeyboardButton('1', url = 'https://bcs.ru/foryou/sp')
            question2 = types.InlineKeyboardButton('2', url = 'https://alfabank.ru/corporate/investments/business/structdep/')
            question3 = types.InlineKeyboardButton('3', url = 'https://alfabank.ru/corporate/investments/business/indxdep/') 
            markup7 = types.InlineKeyboardMarkup()
            markup7.row(question1) 
            markup7.row(question2)
            markup7.row(question3)  
            bot.send_message(callback.message.chat.id, 'В данной вариации пока можем предложить три варианта:\
1) БКС, вход от любой суммы, срок от одной недели\
2) Альфа-банк, вход от 10 млн.руб. срок от 1 недели, возможность конвертации в валюту\
3) Альфа-банк, вход от 10 млн.руб. срок от 3х месяцев', reply_markup=markup7) 
            bot.send_message(message.chat.id, "Надеюсь мне удалось тебе помочь",reply_markup=markup0) 
        if callback.data == 'start':
            bot.send_message( message.chat.id, 'Что тебя интересует?', reply_markup=markup)
        if callback.data == 'answer1.2':
            question1 = types.InlineKeyboardButton('1', url = 'https://www.vtb.ru/personal/investicii/strukturnye-obligacii/#block')
            question2 = types.InlineKeyboardButton('2', url = 'https://alfabank.ru/corporate/investments/structbonds/')
            markup8 = types.InlineKeyboardMarkup()
            markup8.row(question1) 
            markup8.row(question2)  
            bot.send_message(callback.message.chat.id, 'В данной вариации пока можем предложить два варианта:\
1) ВТБ, минимум 50 тыс.рублей\
2) Альфа-банк, срок от 3х месяцев до 5 лет', reply_markup=markup8) 
            bot.send_message(message.chat.id, "Надеюсь мне удалось тебе помочь",reply_markup=markup0)
        if callback.data == 'answer1.3':
            question1 = types.InlineKeyboardButton('1', url = 'https://bcs.ru/foryou/sp')
            markup9 = types.InlineKeyboardMarkup()
            markup9.row(question1)
            markup9.row(question2)   
            bot.send_message(callback.message.chat.id, 'В данной вариации пока можем предложить один вариант:\
1) БКС, предлагаются разные варианты, вход от любой суммы, срок от 1 недели', reply_markup=markup9)
            bot.send_message(message.chat.id, "Надеюсь мне удалось тебе помочь",reply_markup=markup0)
        if callback.data == 'answer2.1':
            question1 = types.InlineKeyboardButton('1', url = 'https://bcs.ru/foryou/sp')
            question2 = types.InlineKeyboardButton('2', url = 'https://alfabank.ru/corporate/investments/business/structdep/')
            question3 = types.InlineKeyboardButton('3', url = 'https://alfabank.ru/corporate/investments/business/indxdep/') 
            markup10 = types.InlineKeyboardMarkup()
            markup10.row(question1) 
            markup10.row(question2)
            markup10.row(question3)  
            bot.send_message(callback.message.chat.id, 'В данной вариации пока можем предложить три варианта:\
1) БКС, предлагаются разные варианты, вход от любой суммы, срок от 1 недели\
2) Альфа-банк, вход от 10 млн.руб. срок от 1 недели, возможность конвертации в валюту\
3) Альфа-банк, вход от 10 млн.руб. срок от 3х месяцев', reply_markup=markup10) 
            bot.send_message(message.chat.id, "Надеюсь мне удалось тебе помочь",reply_markup=markup0)
        if callback.data == 'answer2.2':
            question1 = types.InlineKeyboardButton('1', url = 'https://www.vtb.ru/personal/investicii/strukturnye-obligacii/#block')
            question2 = types.InlineKeyboardButton('2', url = 'https://alfabank.ru/corporate/investments/structbonds/')
            markup11 = types.InlineKeyboardMarkup()
            markup11.row(question1) 
            markup11.row(question2)  
            bot.send_message(callback.message.chat.id, 'В данной вариации пока можем предложить два варианта:\
1) ВТБ, минимум 50 тыс.рублей\
2) Альфа-банк, срок от 3х месяцев до 5 лет', reply_markup=markup11)  
            bot.send_message(message.chat.id, "Надеюсь мне удалось тебе помочь",reply_markup=markup0)
        if callback.data == 'answer3.1':
            question1 = types.InlineKeyboardButton('1', url = 'https://bcs.ru/foryou/sp')
            question2 = types.InlineKeyboardButton('2', url = 'https://alfabank.ru/corporate/investments/business/structdep/')
            question3 = types.InlineKeyboardButton('3', url = 'https://alfabank.ru/corporate/investments/business/indxdep/') 
            markup10 = types.InlineKeyboardMarkup()
            markup10.row(question1)   
            markup10.row(question2)
            markup10.row(question3)
            bot.send_message(callback.message.chat.id, 'В данной вариации пока можем предложить три варианта:\
1) БКС, предлагаются разные варианты, вход от любой суммы, срок от 1 недели\
2) Альфа-банк, вход от 10 млн.руб. срок от 1 недели, возможность конвертации в валюту\
3) Альфа-банк, вход от 10 млн.руб. срок от 3х месяцев', reply_markup=markup10) 
            bot.send_message(message.chat.id, "Надеюсь мне удалось тебе помочь",reply_markup=markup0)
        if callback.data == 'answer3.2':
            question1 = types.InlineKeyboardButton('1', url = 'https://www.vtb.ru/personal/investicii/strukturnye-obligacii/#block')
            question2 = types.InlineKeyboardButton('2', url = 'https://alfabank.ru/corporate/investments/structbonds/')
            markup11 = types.InlineKeyboardMarkup()
            markup11.row(question1)
            markup11.row(question2)  
            bot.send_message(callback.message.chat.id, 'В данной вариации пока можем предложить два варианта:\
1) ВТБ, минимум 50 тыс.рублей\
2) Альфа-банк, срок от 3х месяцев до 5 лет', reply_markup=markup11)  
            bot.send_message(message.chat.id, "Надеюсь мне удалось тебе помочь",reply_markup=markup0) 
bot.polling(none_stop=True)