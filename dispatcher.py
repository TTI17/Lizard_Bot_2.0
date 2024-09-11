from config import bot
from telebot.types import Message
import time
from database_config import ChatDatabase

@bot.message_handler(content_types=['text'])  # This is a decorator that tells the bot to listen for text messages
def get_commands_admin(message:Message):  # This is a function that gets called when a text message is received
    save_database = ChatDatabase(bot=bot, chat_id=message.chat.id, chat_username=message.chat.username)
    save_database.handle_message(message=message)
    # print("message saved")

    #ban user   
    if message.text == '!ban':  # Check if the message is '!ban'
        if bot.get_chat_member(chat_id=message.chat.id , user_id=message.from_user.id).status in ['administrator','creator']:  # Check if the user is an admin
            if not message.reply_to_message:  # Check if the user replied to another message
                bot.send_message(message.chat.id, 'Пожалуйста выделите пользователя, которого хотите отправить в бан')  # Send a message to the chat
            else:
                bot.ban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)  # Ban the user
                bot.send_message(chat_id=1138005743,text=f'Данный пользователь: @{message.reply_to_message.from_user.username} был забанен в группе {message.chat.title}\nСсылка: https://t.me/{message.chat.username}')  # Send a message to the chat
                bot.delete_message(message.chat.id, message.message_id)  # Delete the original message
        else:
            pass

    #unban user
    if message.text == '!unban':  # Check if the message is '!unban'
        if bot.get_chat_member(chat_id=message.chat.id , user_id=message.from_user.id).status in ['administrator','creator']:  # Check if the user is an admin
            if not message.reply_to_message:  # Check if the user replied to another message
                bot.send_message(message.chat.id, 'Пожалуйста выделите пользователя, которого хотите разбанить')  # Send a message to the chat
            else:
                bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)  # Unban the user
                bot.send_message(chat_id=message.reply_to_message.from_user.id, text=f"Ты был разбанен, может присоединяться к чату: https://t.me/{message.chat.username}")

                bot.send_message(chat_id=1138005743,text=f'Данный пользователь: @{message.reply_to_message.from_user.username} был разбанен в группе {message.chat.title}\nСсылка: https://t.me/{message.chat.title}')  # Send a message to the chat
        else:
            pass
    
    #mute user on 1 day
    if message.text == '!mute':  # Check if the message is '!mute'
        if bot.get_chat_member(chat_id=message.chat.id , user_id=message.from_user.id).status in ['administrator','creator']:  # Check if the user is an admin
            if not message.reply_to_message:  # Check if the user replied to another message
                bot.send_message(message.chat.id, 'Пожалуйста выделите пользователя, которого хотите отправить в мут')  # Send a message to the chat
            else:
                bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id,  # Mute the user
                                can_send_messages=False,
                                can_send_media_messages=False, 
                                can_send_other_messages=False, 
                                can_add_web_page_previews=False, until_date=time.time() + 86400)  # Mute for 1 day
                bot.send_message(chat_id=message.chat.id,text=f'{message.reply_to_message.from_user.first_name} был отправлен в мут на день' )
    
    #gives the user the chat administrator role
    if message.text == '!get_admin':  # Check if the message is '!get_admin'
        if bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id).status in ['administrator','creator']:  # Check if the user is an admin
            if not message.reply_to_message:  # Check if the user replied to another message
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)  # Delete the original message
            else:
                bot.promote_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id,  # Make the user an admin
                                        can_change_info=False, 
                                        can_delete_messages=True, 
                                        can_invite_users=True, 
                                        can_restrict_members=True, 
                                        can_pin_messages=True, 
                                        can_promote_members=False)
                bot.send_message(chat_id=message.reply_to_message.from_user.id, text=f'Теперь вы админ в {message.chat.title}')  # Send a message to the chat
                bot.send_message(chat_id=1138005743, text=f'Новый админ в {message.chat.title}: {message.reply_to_message.from_user.username}')  # Send a message to the chat
    
    #revokes administrator rights from the user
    if message.text == '!restrict_admin':
        if bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id).status =='creator':
            if not message.reply_to_message:
                bot.send_message(message.chat.id, 'Пожалуйста выделите пользователя, которого хотите ограничить')  # Send a message to the chat
            else:
                bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id,  # Restrict the user
                                        can_send_messages=True,
                                        can_send_media_messages=True, 
                                        can_change_info=False,
                                        can_invite_users=False,
                                        can_pin_messages=False,
                                        can_send_polls=False,
                                        can_send_other_messages=False,
                                        can_add_web_page_previews=False)
                bot.send_message(chat_id=message.from_user.id, text=f'Пользователь {message.reply_to_message.from_user.username} был ограничен')

    #commands for chat members
    if message.text == '!report':  # Check if the message is '!report'
        if not message.reply_to_message:  # Check if the user replied to another message
            bot.send_message(message.chat.id, text="Пожалуйста, ответьте на сообщение, которое вы хотите репортить")  # Send a message to the chat
        else:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)  # Delete the original message
            bot.send_message(chat_id=message.reply_to_message.chat.id, text='Ваша заявка в обработке')  # Send a message to the chat
            bot.send_message(chat_id=1138005743,text=f'''Данный пользователь: @{message.reply_to_message.from_user.username} написал: "{message.reply_to_message.text}" в группе {message.chat.title}\nСсылка: https://t.me/{message.chat.username}
От кого: @{message.from_user.username}''')  # Send a message to the chat

    # Any other message that starts with '!' is ignored and deleted
    if message.text not in ['!mute', '!unban', '!ban', '!report', '!get_admin', '!restrict_admin'] and '!' in message.text:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)  # Delete the original message
    
    if message.text == '/start':
        if bot.get_chat(message.chat.id).type == 'private':
            bot.send_message(message.chat.id, text='''😊 Добро пожаловать в наш чат! 🎉

Я - бот-администратор, и я здесь, чтобы помочь вам и вашей группе или чату с модерацией. 🤝

Чтобы добавить меня в чат, нажмите на эту ссылку: https://telegram.me/testbotttibot?startgroup 📲

После добавления меня в чат, вы должны дать мне права администратора, чтобы бот заработал без перебоев. 🔓
''')
        else:
            pass