from telebot import types

def create_menu(bot, chat_id):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Настройки', callback_data='settings')
    button2 = types.InlineKeyboardButton(text='Добавить бота в чат', callback_data='add_to_chat')
    button3 = types.InlineKeyboardButton(text='FAQ', callback_data='faq')
    keyboard.add(button1, button2, button3)
    bot.send_message(chat_id, 'Выберите действие:', reply_markup=keyboard)

def handle_callback(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    data = query.data
    if data == 'settings':
        # Обработка нажатия на кнопку "Настройки"
        edit_settings_keyboard(bot, chat_id, query)
    elif data == 'add_to_chat':
        # Обработка нажатия на кнопку "Добавить бота в чат"
        edit_add_to_chat_keyboard(bot, chat_id, query)
    elif data == 'faq':
        # Обработка нажатия на кнопку "FAQ"
        edit_faq_keyboard(bot, chat_id, query)

def edit_settings_keyboard(bot, chat_id, query):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Параметр 1', callback_data='param1')
    button2 = types.InlineKeyboardButton(text='Параметр 2', callback_data='param2')
    keyboard.add(button1, button2)
    bot.edit_message_reply_markup(chat_id=chat_id, message_id=query.message.message_id, reply_markup=keyboard)

def edit_add_to_chat_keyboard(bot, chat_id, query):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Добавить в чат 1', callback_data='add_to_chat1')
    button2 = types.InlineKeyboardButton(text='Добавить в чат 2', callback_data='add_to_chat2')
    keyboard.add(button1, button2)
    bot.edit_message_reply_markup(chat_id=chat_id, message_id=query.message.message_id, reply_markup=keyboard)

def edit_faq_keyboard(bot, chat_id, query):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Вопрос 1', callback_data='question1')
    button2 = types.InlineKeyboardButton(text='Вопрос 2', callback_data='question2')
    keyboard.add(button1, button2)
    bot.edit_message_reply_markup(chat_id=chat_id, message_id=query.message.message_id, reply_markup=keyboard)