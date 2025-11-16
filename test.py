import telebot
users = {}
freeid = None

    
    # Инициализация бота с использованием его токена
bot = telebot.TeleBot("8476458388:AAEq36uFRg_FdkDARoyIAuCmPtAstKRuOM8")
    
    # Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
        bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
    # Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
        count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
        bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['find'])
def find(message):
    global freeid

    if message.chat.id not in users:
        bot.send_message(message.chat.id, 'Finding...')

        if freeid is None:
            freeid = message.chat.id
        else:
            # Question:
            # Is there any way to simplify this like `bot.send_message([message.chat.id, freeid], 'Founded!')`?
            bot.send_message(message.chat.id, 'Founded!')
            bot.send_message(freeid, 'Founded!')

            users[freeid] = message.chat.id
            users[message.chat.id] = freeid
            freeid = None

        print(users, freeid) # Debug purpose, you can remove that line
    else:
        bot.send_message(message.chat.id, 'Shut up!')

@bot.message_handler(commands=['stop'])
def stop(message):
    global freeid

    if message.chat.id in users:
        bot.send_message(message.chat.id, 'Stopping...')
        bot.send_message(users[message.chat.id], 'Your opponent is leavin`...')

        del users[users[message.chat.id]]
        del users[message.chat.id]
        
        print(users, freeid) # Debug purpose, you can remove that line
    elif message.chat.id == freeid:
        bot.send_message(message.chat.id, 'Stopping...')
        freeid = None

        print(users, freeid) # Debug purpose, you can remove that line
    else:
        bot.send_message(message.chat.id, 'You are not in search!')
    # Запуск бота

@bot.message_handler(content_types=['animation', 'audio', 'contact', 'dice', 'document', 'location', 'photo', 'poll', 'sticker', 'text', 'venue', 'video', 'video_note', 'voice'])
def chatting(message):
    if message.chat.id in users:
        bot.copy_message(users[message.chat.id], users[users[message.chat.id]], message.id)
    else:
        bot.send_message(message.chat.id, 'No one can hear you...')


bot.polling()