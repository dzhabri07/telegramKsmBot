import telebot
from telebot import types

token = "1033623575:AAE9F7tT_lcRMTZs6juRrtbwtg7B5UPiaUs"

proxy_const = {'https':'socks5://Dzhabri:e834326d@195.123.249.187:1490'}

seeds = {
    'Рис': "Укажите основные характеристики клейковина/протеин/натура(Цена/Вес/Регион)",
    'Ячмень': "Укажите основные характеристики натура от/влажность до/сорная примесь до(Цена/Вес/Регион)",
    'Соя': "Укажите основные характеристики протеин/влажность/сорная примись(Цена/Вес/Регион)",
    'Горох': "Укажите основные характеристики влага/сорная примись/зерновая примись(Цена/Вес/Регион)",
    'Пшеница': "Укажите основные характеристики класс/влажность/протеин/натура(Цена/Вес/Регион)",
    'Кукуруза': "Укажите основные характеристики влажность/натура/протеин (Цена/Вес/Регион)",
    'Семечка': "Укажите основные характеристики влажность/натура/протеин (Цена/Вес/Регион)",
    'Лен': "Укажите основные характеристики влажность/натура/протеин (Цена/Вес/Регион)"
}

strart_message = '''<u>Как работает данный алгоритм</u>:
<b>1)</b> Выбираем 'Покупка' или 'Продажа'
<b>2)</b> Далее выбираем продукт который хотим купить/продать
<b>3)</b> Указываем доп. информацию(Всё о вашем продукте или продукте который вы хотите купить)
<b>4)</b> Указываем контактные данные'''

exmple_message = '''<u>Пример того как будет выглядить ваше конечное объявление:</u>
<b>Покупка</b>
<b>Кукуруза</b>
Вес - 500т. влага - 14%, зерновая примесь - 6%, натура - 735+. Цена - 11000 с НДС. Прием осуществляется в  ст. Ленинградская,Краснодарский край.
<b>Контактные данные</b> -  <i>89298241971</i>'''

rules_message = '''<u>Правила работы с ботом</u>
1) Запрещенно спамить боту - Бан в группе
2) Запрещенно писать слишком большие объявления!
3) Следаовать алгориту заполнения объявления
4) Доработать правила общения с ботом..........'''

сommands_message = '''<b>Вы можете использовать следующие команды:</b>
/example - просмотр примера как будет выглядить готовое объявление созданное с помощью данного алгоритма
/help    - помощь заполнения бота
/rules   - правила работы с ботом'''

greeting_message = '''<b>Добро пожаловать {0.first_name}!</b>\nВас приветствует {1.first_name}.\nЯ помогу выставить ваше объявление просто следйуте инструкциям: '''

greeting_message_public = '''<b>Добро пожаловать, {0}!</b>
Чтобы разместить своё объявление обратитесь к боту @KsmAgroBot'''
buy_sell_message = '''1) Покупаем или продаём(Выберите кнопку)'''

type_of_product = "2) Выберите продукт для покупки: "

error_message = '''<b>Ошибка! Выберите кнопку <i>START</i></b>'''

get_contact_message = "4) Укажите контактные данные:"

check_message = '''<strong><u>Спасибо за терпение, проверьте всё ли верно:\n</u></strong>'''

last_message = '''<strong>Спасибо ваше объявление отправлено в группу @ksmagro</strong>'''

start_again_message = "Для повторного отправления объявления нажмите /start!"

who_send_message = "\n\n<u><i>Отправитель объявления:</i> <b>{} {} - @{}</b></u>"

buy_sell_keyboard = telebot.types.ReplyKeyboardMarkup(True, True).row('Покупка', 'Продажа')

seed_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).row(
    'Соя', 'Горох', 'Ячмень')
seed_keyboard.add('Пшеница', 'Семечка')
seed_keyboard.row('Семечка', 'Лен', 'Рис')

choose_end_keybord = telebot.types.ReplyKeyboardMarkup(True, True).row('Всё верно!', 'Заполнить заново')

start_keybord = telebot.types.ReplyKeyboardMarkup(True, True).row('/start')

triger_words = '(\s+|^)[пПnрРp]?[3ЗзВBвПnпрРpPАaAаОoO0о]?[сСcCиИuUОoO0оАaAаыЫуУyтТT]?[Ппn][иИuUeEеЕ][зЗ3][ДдDd]\w*[\?\,\.\;\-]*|(\s+|^)[рРpPпПn]?[рРpPоОoO0аАaAзЗ3]?[оОoO0иИuUаАaAcCсСзЗ3тТTуУy]?[XxХх][уУy][йЙеЕeEeяЯ9юЮ]\w*[\?\,\.\;\-]*|(\s+|^)[бпПnБ6][лЛ][яЯ9]([дтДТDT]\w*)?[\?\,\.\;\-]*|(\s+|^)(([зЗоОoO03]?[аАaAтТT]?[ъЪ]?)|(\w+[оОOo0еЕeE]))?[еЕeEиИuUёЁ][бБ6пП]([аАaAиИuUуУy]\w*)?[\?\,\.\;\-]*'
