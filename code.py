from pickle import TRUE
import telebot

#API Токен бота
bot = telebot.TeleBot('')

CUSTOM_CODE_DICT = {'А':'01','Б':'00','В':'7','Г':'85','Д':'42','Е':'35','Ж':'75','И':'4','Й':'5','К':'11','Л':'111','М':'1111','Н':'0000',
                   'У':'0','Ц':'00jdvxnqwe','Ш':'3sfsq0','Щ':'0wrcz1233','З':'45434fs4','Х':'47xbq6','Ъ':'11d564','Ф':'6vv54','Ы':'9vv4','П':'F7412','Р':'G854','О':'NX85','Э':'SA445',
                   'Я':'78564999V','Ч':'TTT9','С':'T1','Т':'WR5','Ь':'4565GHHR3TGF2','Ю':'G3488883','а':'GGER5234','б':'FSFF3f','в':'FV4550ds','г':'VBX14441fb','д':'DF42dg','е':'FSVqe','ж':'FG2vdz',
                   'з':'VXV32vxa','и':'GBF11fF','й':'gggGGG','к':'BDbdBD','л':'2da4F','м':'XV2489qef','н':'DGV123','о':'gerXYU','п':'wfffXYU11','р':'ds2XYTY','с':'XERVDvc13','т':'v345FVERN','у':'bxFFR7416',
                   'ф':'F0F0F0','х':'31T2YU4Tfdsfqe','ц':'3DGDGBAZA4','ч':'BAZANHERQ345','ш':'GEW31EDDSDRE1','щ':'GR4RV3EE1FVDZ','ъ':'441dgdhTGBFSQEF','ы':'QEQERQRWERt34','ь':'QQQWE555Q','э':'Q3Q2Q1QQ','ю':'WRFQQQ445',
                   'я':'FWWER13R34',' ':'P4325245678RhOjjB13R2EwerL','.':'TOC0g',',':'7f31D','?':'S3242R4f',':':'FJW109', '-':'ERF5','1': '4324VXZ', '2': '131E41EZFQ', '3': '2343D', '4': 'werFOU', 
                   '5': '222bla2222', '6': 'GXXsada133', '7': '00313TZW4FS', '8': '24FSF1313', '9': '0010101010', 
                   '0': '43413213fsf23','A': 'ewr8572934g', 'B': 'qsfsfc4w1345sew', 'C': 'eqe52fsfDA', 'D': 'rDAtDA', 'E': 'tDgG', 
                   'F': '5R56654SF65SFD5gvsf', 'G': 'GD625RWFQ1113fz23', 'H': '4ewfv1238EW6FZF', 'I': 'F845SFEWEE86f', 'J': 'rWR485', 
                   'K': 'SFG62WER341ewf', 'L': 'sf52QW9', 'M': '5RSF5sf56qwe-', 'N': '5TSDASDSA4sf65s', 'O': 'FSDF4FNOUP4198qe', 
                   'P': '445fDSGODAsffsf', 'Q': 'TINA39451', 'R': 'KI23483gghLOWERq', 'S': '34MAMEqe', 'T': 'NUOPURE', 
                   'U': 'FSWER956z', 'V': '66qr4TG3555552', 'W': '56sFSAFE', 'X': 'F5sFREMON424TYWEQE', 'Y': '5TOOLR27YJqeqwrf', 
                   'Z': 'PAZDAFRRQEsfcsdfq', 'a': 'BVPIZs45f', 'b': 'G1O25OR4D3494956ad', 'c': 'SFBUJN4781FSF1EDF5GS', 'd': 'ERBGTGAGTA424qfzvqe65', 
                   'e': '94Mqdd1c', 'f': 'werfsfMMM', 'g': 'MERTsfsdMf5Mr', 'h': 'qdc7SDFeFE16', 'i': 'qe45d2adqeddad888837', 
                   'j': 'RURURU4UE8JEDNENDG', 'k': 'FGFRU2Ssfs49qe3dfd', 'l': 'HWR7VNSFNA4SAdfqdf', 'm': 'REEWWWEFVFDBsdfqedzdad', 'n': 'SCOYfsfHOY45', 
                   'o': 'FS23341DGHNMVZQ431re', 'p': '747DS4719RBDAH3E', 'q': '43327HNDUIFG3DA', 'r': '595=SGYUINTBS1YNEWR34RGY731734', 's': 'SY341M55PAYWR', 
                   't': 'F47HR2FSOQNNNMMDQWEs9df', 'u': 'dsfoo4jrmODMQ', 'v': '4998000ooooOOO', 'w': '.GGGSD32gggewrfs666', 'x': '4sdfSFNNNN47438FNGGG2FS1', 
                   'y': '42FfweFTNJMOLsdfsdf', 'z': 'eeefvvceLLLFWERWERC3T674U'}

#Функция которая шифрует сообщение
def encrypt(text):
    message = []
    for i in text:
        if i in CUSTOM_CODE_DICT:
            message.append(CUSTOM_CODE_DICT[i])
    return ' '.join(message)

#Функция которая дешифрует сообщение
def decrypt(text):
    message = []
    codes = text.split(' ')
    for code in codes:
        for key, value in CUSTOM_CODE_DICT.items():
            if value == code:
                message.append(key)
    return ''.join(message)

#Функция для анализа
def analytics(func: callable):
    total_messages = 0    # Всего сообщений
    users = set()         # Множество пользователей(чтобы были уникальные пользователи)
    total_users = 0       # Всего пользователей
    def analytics_wrapper(message):
        nonlocal total_messages, total_users
        total_messages+=1
        if message.chat.id not in users:
            users.add(message.chat.id)
            total_users+=1
        print("Новое сообщение:", message.text)
        print(f"Всего сообщений:{total_messages} Уникальных пользователей:{total_users}")
        return func(message)
    return analytics_wrapper

'''Это приветствие и инструкции как пользовалься ботом'''
@bot.message_handler(commands=['start'])
@analytics
def start(message):
    mess = f'Привествую, {message.from_user.first_name}, это бот шифрует и расшифровывает сообщения.Чтобы зашифровать нажмите комманду crypt и ваше сообщение, расшифровать decrypt и ваше сообщение'
    primer = f'Пример: Привет'
    primer_1 = f'Ответ: F7412 ds2XYTY GBF11fF FV4550ds FSVqe v345FVERN'
    bot.send_message(message.chat.id, mess)
    bot.send_message(message.chat.id, primer)
    bot.send_message(message.chat.id, primer_1)


@bot.message_handler(commands=['crypt'])
@analytics
def tools_mess_1(message):
    mess = f'Введите что хотите зашифровать:'
    bot.send_message(message.chat.id, mess)  # Отправка пользователю сообщения mess
    bot.register_next_step_handler(message, encrypt_message) # Ожидание нового сообщения от пользователя
    
    
def encrypt_message(message):
    message_text = message.text
    if len(message_text)>0: # Проверка на то что пользователь хоть что-то написал
        crypted_message = encrypt(message_text) #Обращение к функции которая шифрует
        bot.reply_to(message, 'Зашифрованное сообщение: ')
        bot.reply_to(message, crypted_message)
    

@bot.message_handler(commands=['decrypt'])
@analytics
def tools_mess_2(message):
    mess = f'Введите что хотите расшифровать:'
    bot.send_message(message.chat.id, mess) # Отправка пользователю сообщения mess
    bot.register_next_step_handler(message, decrypt_message) # Ожидание нового сообщения от пользователя
    
    
def decrypt_message(message):
    message_text = message.text
    if len(message_text)>0: # Проверка на то что пользователь хоть что-то написал
        crypted_message = decrypt(message_text) #Обращение к функции которая шифрует
        bot.reply_to(message, 'Расшифрованное сообщение: ')
        bot.reply_to(message, crypted_message)

bot.polling(none_stop = TRUE)    

#Для постоянной работы бота
#bot.infinity_polling()