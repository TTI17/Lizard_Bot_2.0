import os
import json
from config import bot
from telebot.types import Message



def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)


class ChatDatabase:
    def __init__(self, bot, chat_id, chat_username):
        self.bot = bot
        self.chat_id = chat_id
        self.chat_username = chat_username
        self.database_folder = os.path.join("database", str(chat_username))
        self.users = {}

        create_folder(self.database_folder)

    def handle_message(self, message: Message):
        # Обрабатываем сообщение и обновляем информацию о пользователях
        user_id = message.from_user.id
        username = message.from_user.username
        status = bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id).status

        if user_id not in self.users:
            self.users[user_id] = {
                "id": user_id,
                "username": username,
                "status": status,
                "messages": []
            }

        self.users[user_id]["messages"].append(message.text)

        # Сохраняем информацию о пользователях в JSON файлы
        self.save_users()

    def save_users(self):
        for user_id, user_info in self.users.items():
            user_file = os.path.join(self.database_folder, f"{user_id}.json")
            with open(user_file, "w") as f:
                json.dump(user_info, f, indent=4)
