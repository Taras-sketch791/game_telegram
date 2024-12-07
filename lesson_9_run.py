#pip install pyTelegramBotAPI
# https://t.me/BotFather
# https://t.me/kbvfdhhkjkeyjbot

import telebot
import lesson9_game_logic

bot = telebot.TeleBot("7940044719:AAFsqm4qVz6e8LCQbFPELrXk4-VR8D0HY-8")
CURRENT_PLAYER = ['X']


@bot.message_handler(commands=['start'])
def start_game(message):
	lesson9_game_logic.clear_data()
	bot.send_message(message.chat.id, f'Новая игра началась')
	bot.send_message(message.chat.id, lesson9_game_logic.print_game_field())
	bot.send_message(message.chat.id, f'Вах ход: {CURRENT_PLAYER[0]}')


@bot.message_handler(content_types=['text'])
def start_game(message):
	bot.send_message(
		message.chat.id,
		lesson9_game_logic.input_value(message.text, CURRENT_PLAYER[0])
	)
	if lesson9_game_logic.check_is_game_end() == lesson9_game_logic.STATUS_CONTINUE:
		bot.send_message(
			message.chat.id,
			lesson9_game_logic.print_game_field()
		)
		if CURRENT_PLAYER[0] == 'X':
			CURRENT_PLAYER[0] = 'O'
		else:
			CURRENT_PLAYER[0] = 'X'
		bot.send_message(
			message.chat.id,
			f'Сейчас ходит: {CURRENT_PLAYER[0]}'
		)
	else:
		bot.send_message(message.chat.id, f'Игра закончена, победа: {lesson9_game_logic.check_is_game_end()}')


bot.infinity_polling()
