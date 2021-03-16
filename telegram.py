import telebot
from text import csv_telega

WRITE = 'write.csv'
#  токен бота
TOKEN_TELEGA = '1658739648:AAHTURfBoFQrb69wvYLnkuQ5o6gFiga2gGo'

bot = telebot.TeleBot(TOKEN_TELEGA)
print(bot)


@bot.message_handler(commands=['help'])
def send_welcome(message):
	"""Вывод команд для работы с ботом

	Args:
		message (str): входящая команда
	Returns:
		сообщение с командами для работы с ботом по команде '/help'
	"""
	bot.reply_to(message, "Write commands: /start")


@bot.message_handler(commands=['start'])
def start_pars(message):
	"""Вывод результата парсинга сайтов

	Args:
		message (str): входящая команда
	Returns:
		сообщение с результатами парсинга сайтов по команде '/start'
	"""
	offers_list = csv_telega(WRITE)
	bot.reply_to(message, '\n'.join(offers_list))


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	"""Обработка не существующих команд в боте

	Args:
		message (str): входящая команда
	Returns:
		Вывод сообщения что такой команды не существует
	"""
	bot.reply_to(message, 'Такой команды не существует, действуй дальше')


bot.polling()
