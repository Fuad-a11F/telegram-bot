from datetime import timedelta, datetime


class ValidationMessage:
    def __init__(self):
        self.blocked = {}
        self.mats = ['Пизда', 'Хуй', 'Ебать', 'Уебок', 'Пиздабол', 'Хуесос',
                     'Блять', 'Бля', 'Блядина', 'Наебал', 'Съебал']

    def __is_has_mat(self, message):
        for mat in self.mats:
            if mat.lower() in message.lower():
                return True

        return False

    def check_message(self, message, user):
        if self.__is_has_mat(message):
            self.blocked[user] = datetime.now() + timedelta(seconds=20)
            return True

    def user_blocked(self, user):
        if user in self.blocked:
            if self.blocked[user] < datetime.now():
                return False
            return True

        else:
            return False

    @staticmethod
    def get_text(username):
        return f'Пользователь {username} сматерился. Его сообщение удалено, а он сам не может писать сообщения в чат в течение 20 секунд.'

    @staticmethod
    def __get_correct_time(time):
        return f'{time[0:7].split(":")[1][1]} мин {time[0:7].split(":")[2]} сек'

    def get_blocked_text(self, username, id):
        get_time_to_unblock = self.blocked[id] - datetime.now()
        return f'{username}, вы сможете снова отправлять сообщения через {self.__get_correct_time(str(get_time_to_unblock))}.'
