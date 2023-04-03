from simple_bot import Bot
from longpoll_bot import LongPollBot

if __name__=='__main__':
    # Создание и запуск обычного бота
    bot = Bot()

    # Отправка тестового сообщения
    bot.send_message()

    # создание и запуск бота, автоматически отвечающего на заданные сообщения
    long_poll_bot = LongPollBot()
    long_poll_bot.run_long_poll()
