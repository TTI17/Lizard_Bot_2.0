from config import bot
from telebot.types import Message

@bot.message_handler(content_types=['new_chat_members'])
def hello_chat_members(message:Message):
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text=f"Приветствую вас, {message.from_user.username}!")
    bot.send_message(chat_id=1138005743, text=f"{message.from_user.username} joined in group!")

@bot.message_handler(content_types=['left_chat_member'])
def left_chat_member(message:Message):
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text=f"Пользователь {message.from_user.username} покинул чат")
    bot.send_message(chat_id=1138005743, text=f"Пользователь {message.from_user.username} leaved in group!")