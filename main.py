from telebot import types, TeleBot
from telebot.types import *

bot = TeleBot(token='5418678353:AAFOznwfToWPFkAhvtuVE36BR_pltEKtaeo')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Да")
btn2 = types.KeyboardButton("Нет")
markup.add(btn1, btn2)

rating = {"1": 0,
          "2": 0,
          "3": 0,
          "4": 0,
          "5": 0,
          "6": 0,
          "7": 0,
          "8": 0,
          "9": 0,
          "10": 0}

data = {"1": {"text": """Корги
Корги — это пастушья собака, она любит собирать всех в группы, особенно маленьких детей. Несмотря на милую кукольную внешность, корги быстрые и ловкие, хорошо поддаются дрессировке. Этой породе нужно большое пространство и много упражнений, которые они воспринимают как приключение!
Корги очень преданные и активные, любят детей и постоянно улыбаются.""",
              "photo_name": "1.jpg"},

        "2": {"text": """Немецкий пинчер 
Эта порода относится к древнему роду и имеет великолепные рабочие качества. Выглядит соответствующе — грациозно и статно. Пинчеры активные и самостоятельные, а при защите хозяина отважны и злобны.""",
              "photo_name": "2.jpg"},

        "3": {"text": """Джек-Рассел терьер
Эта порода страстная и азартная. Под стать хозяину ;) Джек-Рассел терьеры бесстрашны — они готовы драться даже с наиболее сильными противниками, так как у них в крови большой уровень адреналина. Они любят детей и легко уживаются с другими животными, но бывают ревнивы. Джек-Рассел терьеры легко поддаются дрессировке и будут прекрасными питомцами в большой семье.""",
              "photo_name": "3.jpg"},

        "4": {"text": """Кроличья такса
Таксы — высокоинтеллектуальные собаки. Им комфортно жить в квартире. 
Таксам необходимо внимание хозяина, иначе они будут обижаться и даже вести себя агрессивно, как и многие обиженные люди. 
Они хорошо уживаются с другими животными, если это не грызуны.""",
              "photo_name": "4.jpg"},

        "5": {"text": """Акита
Эта порода по своей природе не очень контактная, в ней нужно специально взращивать контактность, если стоит такая задача. Акита обладает крепким здоровьем и очень вынослива. Они имеют безупречные «манеры» и любят детей, но их непросто обучать.""",
              "photo_name": "5.jpg"},

        "6": {"text": """Эстонская гончая
Эта порода комфортно себя чувствует с другими животными и детьми. Эстонская гончая очень «чистоплотна» и послушна. Им необходимы длинные прогулки.""",
              "photo_name": "6.jpg"},

        "7": {"text": """Курцхаар
Эти собаки настоящие атлеты! Они активны, резки и любят игры. К чужим людям могут относиться агрессивно, а маленькие животные и вовсе имеют вероятность быть съеденными, но по отношению к хозяину они нежные и преданные.""",
              "photo_name": "7.jpg"},

        "8": {"text": """Золотистый ретривер 
Эта собака очень нежная со спокойным характером. Они чувствительные и общительные, но постоянно о чём-то переживают и беспокоятся, в силу своего чувствительного характера.""",
              "photo_name": "8.jpg"},

        "9": {"text": """Мопс
Это очень добрые собаки, но одновременно с тем смелые: считают, что нападение – лучшая защита, могут охранять квартиру. Мопсам комфортно в квартире и они любят отбивать ритм своими лапками по двери, когда она закрыта. Они хорошо ладят с животными и очень уверены в себе, а также умеют обаятельно хрюкать.""",
              "photo_name": "9.jpg"},

        "10": {"text": """Русская псовая борзая
Это бывшие питомцы царей и помещиков, национальная гордость России. Русские борзые спокойные и умные, стремятся продумать каждый свой шаг. 
Одна из немногих собак, которая не будет требовать внимания хозяина, если он занят — очень послуша.""",
               "photo_name": "10.jpg"}}


@bot.message_handler(commands=['start'])
def start(message):
    global rating

    rating = {"1": 0,
              "2": 0,
              "3": 0,
              "4": 0,
              "5": 0,
              "6": 0,
              "7": 0,
              "8": 0,
              "9": 0,
              "10": 0}
    new_message = bot.send_message(message.from_user.id,
                                   "Я задам тебе 15 коротких вопросов о твоих предпочтениях и образе жизни,"
                                   " на которые тебе нужно будет ответить «да» или «нет», продолжаем?",
                                   reply_markup=markup)

    bot.register_next_step_handler(new_message, question_1)


def question_1(message):
    if message.text == "Да":
        new_message = bot.send_message(message.from_user.id,
                                       "1) Шерсть — это ужасно, не хочу её видеть в квартире и возиться с вычёсыванием",
                                       reply_markup=markup)
        bot.register_next_step_handler(new_message, question_2)
    elif message.text == "Нет":
        bot.send_message(message.from_user.id,
                         "Возвращайся когда будешь готов! Чтобы запустить бота заново напиши /start",
                         reply_markup=ReplyKeyboardRemove())


def question_2(message):
    global rating
    if message.text == "Да":
        rating["1"] = -1
        rating["5"] = -1
        rating["8"] = -1
        rating["10"] = -1

    elif message.text == "Нет":
        if rating["2"] != -1:
            rating["2"] += 1
        if rating["4"] != -1:
            rating["4"] += 1

    new_message = bot.send_message(message.from_user.id,
                                   "2) У меня есть дети или в ближайшее время планирую завести", reply_markup=markup)
    bot.register_next_step_handler(new_message, question_3)


def question_3(message):
    global rating
    if message.text == "Да":
        rating["4"] = -1
        rating["8"] = -1

    elif message.text == "Нет":
        if rating["1"] != -1:
            rating["1"] += 1

        if rating["3"] != -1:
            rating["3"] += 1
        if rating["5"] != -1:
            rating["5"] += 1
        if rating["6"] != -1:
            rating["6"] += 1
        if rating["9"] != -1:
            rating["9"] += 1

    new_message = bot.send_message(message.from_user.id,
                                   "3) У меня есть маленькие животные", reply_markup=markup)
    bot.register_next_step_handler(new_message, question_4)


def question_4(message):
    global rating
    if message.text == "Да":
        rating["4"] = -1
        rating["7"] = -1
        rating["10"] = -1

    elif message.text == "Нет":
        if rating["3"] != -1:
            rating["3"] += 1
        if rating["9"] != -1:
            rating["9"] += 1
    new_message = bot.send_message(message.from_user.id,
                                   "4) Я не готов(а) отвлекаться от важных дел на собаку, она должна уметь занять себя,"
                                   " если я занят(а)",
                                   reply_markup=markup)
    bot.register_next_step_handler(new_message, question_5)


def question_5(message):
    global rating
    if message.text == "Да":
        rating["4"] = -1
        rating["8"] = -1

    elif message.text == "Нет":
        if rating["6"] != -1:
            rating["6"] += 1
        if rating["9"] != -1:
            rating["9"] += 1
        if rating["10"] != -1:
            rating["10"] += 1
    new_message = bot.send_message(message.from_user.id, "5) Я живу в квартире", reply_markup=markup)
    bot.register_next_step_handler(new_message, question_6)


def question_6(message):
    global rating
    if message.text == "Да":
        rating["1"] = -1
        rating["10"] = -1

    elif message.text == "Нет":
        if rating["4"] != -1:
            rating["4"] += 1

        if rating["9"] != -1:
            rating["9"] += 1
    new_message = bot.send_message(message.from_user.id, "6) Я не готов(а) тратить по два часа в день"
                                                         " на активные прогулки с собакой", reply_markup=markup)
    bot.register_next_step_handler(new_message, question_7)


def question_7(message):
    global rating
    if message.text == "Да":
        rating["1"] = -1
        rating["2"] = -1
        rating["3"] = -1
        rating["6"] = -1
        rating["7"] = -1

    elif message.text == "Нет":
        if rating["4"] != -1:
            rating["4"] += 1
        if rating["9"] != -1:
            rating["9"] += 1
    new_message = bot.send_message(message.from_user.id, "7) Мне принципиально важно, "
                                                         "чтоб собаку было легко обучить командам", reply_markup=markup)
    bot.register_next_step_handler(new_message, question_8)


def question_8(message):
    global rating
    if message.text == "Да":
        rating["5"] = -1

    elif message.text == "Нет":
        if rating["6"] != -1:
            rating["6"] += 1
    new_message = bot.send_message(message.from_user.id, "8) Я — контактный человек и хочу чтобы собака любила ласку",
                                   reply_markup=markup)
    bot.register_next_step_handler(new_message, question_9)


def question_9(message):
    global rating
    if message.text == "Да":
        rating["5"] = -1

    elif message.text == "Нет":
        if rating["8"] != -1:
            rating["8"] += 1

    new_message = bot.send_message(message.from_user.id, "9) Я жду от собаки абсолютного послушания",
                                   reply_markup=markup)
    bot.register_next_step_handler(new_message, question_10)


def question_10(message):
    global rating
    if message.text == "Да":
        rating["5"] = -1

    elif message.text == "Нет":
        if rating["1"] != -1:
            rating["1"] += 1
        if rating["3"] != -1:
            rating["3"] += 1
        if rating["6"] != -1:
            rating["6"] += 1
        if rating["9"] != -1:
            rating["9"] += 1
        if rating["10"] != -1:
            rating["10"] += 1

    new_message = bot.send_message(message.from_user.id, "10) Ко мне часто приходят с друзья и мне важно,"
                                                         " чтоб собака была дружелюбна к другим людям",
                                   reply_markup=markup)
    bot.register_next_step_handler(new_message, question_11)


def question_11(message):
    global rating
    if message.text == "Да":
        rating["2"] = -1
        rating["7"] = -1
        rating["8"] = -1

    elif message.text == "Нет":
        if rating["5"] != -1:
            rating["5"] += 1
        if rating["9"] != -1:
            rating["9"] += 1

    new_message = bot.send_message(message.from_user.id, "11) Я хочу, "
                                                         "чтобы моя собака демонстрировала высокие "
                                                         "умственные способности и "
                                                         "готов с ней заниматься для этого результата",
                                   reply_markup=markup)
    bot.register_next_step_handler(new_message, question_12)


def question_12(message):
    global rating
    if message.text == "Да":
        rating["5"] = -1

    elif message.text == "Нет":
        if rating["4"] != -1:
            rating["4"] += 1
        if rating["10"] != -1:
            rating["10"] += 1

    new_message = bot.send_message(message.from_user.id, "12) Я не готов постоянно бегать с собакой по ветеринарам,"
                                                         " хочу взять породу с крепким здоровьем",
                                   reply_markup=markup)
    bot.register_next_step_handler(new_message, question_13)


def question_13(message):
    global rating
    if message.text == "Да":
        rating["9"] = -1
    elif message.text == "Нет":
        if rating["5"] != -1:
            rating["5"] += 1
    new_message = bot.send_message(message.from_user.id, "13) Я люблю сёрфинг или просто предпочитаю отдых на воде",
                                   reply_markup=markup)
    bot.register_next_step_handler(new_message, question_14)


def question_14(message):
    global rating
    if message.text == "Да":
        if rating["8"] != -1:
            rating["8"] += 1

    new_message = bot.send_message(message.from_user.id, "14) Я хочу гордиться древним родом своей собаки",
                                   reply_markup=markup)
    bot.register_next_step_handler(new_message, question_15)


def question_15(message):
    global rating
    if message.text == "Да":
        if rating["2"] != -1:
            rating["2"] += 1
        if rating["10"] != -1:
            rating["10"] += 1

    new_message = bot.send_message(message.from_user.id, "15) Я буду с пониманием относится к ревнивости "
                                                         "и обидчивости моей собаки "
                                                         "и стараться давать ей столько любви, сколько ей нужно:",
                                   reply_markup=markup)
    bot.register_next_step_handler(new_message, final)


def final(message):
    global rating

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Пройти тест заново!")
    keyboard.add(button1)

    answer = []
    if message.text == "Да":
        if rating["3"] != -1:
            rating["3"] += 1
        if rating["4"] != -1:
            rating["4"] += 1
        if rating["8"] != -1:
            rating["8"] += 1
    for i in rating.items():
        answer.append(i)

    answer = sorted(answer, key=lambda x: x[1])[::-1]
    bot.send_message(message.from_user.id, data[answer[0][0]]["text"], reply_markup=keyboard)
    photo = open(f"Photos/{data[answer[0][0]]['photo_name']}", 'rb')
    new_message = bot.send_photo(message.from_user.id, photo, reply_markup=keyboard)
    bot.register_next_step_handler(new_message, start)


bot.polling()
