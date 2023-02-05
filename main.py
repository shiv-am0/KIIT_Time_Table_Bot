import os
from dotenv import load_dotenv
import telebot
import timetable

load_dotenv()

API_KEY = os.environ.get('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['getcore'])
def get_core(message):
    sent_msg = bot.send_message(message.chat.id, 'Please enter your section followed by the day (e.g. CSE-1 MON): ')
    bot.register_next_step_handler(sent_msg, return_core_time_table)


def return_core_time_table(message):
    data = message.text
    keyword_list = data.split()
    try:
        res_dict = timetable.get_core_time_table(keyword_list[0], keyword_list[1])
        print(res_dict)
        res = core_dict_to_table(res_dict)
    except KeyError as ex:
        print(ex)
        res = 'This section/command is not valid. Please try again.'

    bot.send_message(message.chat.id, res)


def core_dict_to_table(res_dict):
    res = '''
     {:<10}: {:<10}
     {:<10}: {:<10} 
     {:<10}: {:<10}
     {:<10}: {:<10} 
     {:<10}: {:<10} 
     {:<10}: {:<10} 
     {:<10}: {:<10} 
     {:<10}: {:<10} 
     {:<10}: {:<10}
     '''.format(
        'DAY', res_dict.get('DAY'),
        'ROOM1', res_dict.get('ROOM1'),
        '8-9', res_dict.get('8-9'),
        '9-10', res_dict.get('9-10'),
        '10-11', res_dict.get('10-11'),
        'ROOM2', res_dict.get('ROOM2'),
        '11-12', res_dict.get('11-12'),
        '12-1', res_dict.get('12-1'),
        '1-2', res_dict.get('1-2')
    )

    print(res)
    return res


@bot.message_handler(commands=['getElective'])
def get_elective(message):
    sent_msg = bot.send_message(message.chat.id,
                                'Please enter your elective code, section and day (e.g. ML_CSE-1 MON): ')
    bot.register_next_step_handler(sent_msg, return_elective_time_table)


def return_elective_time_table(message):
    data = message.text
    keyword_list = data.split()
    try:
        res_dict = timetable.get_ele_time_table(keyword_list[0], keyword_list[1])
        print(res_dict)
        res = ele_dict_to_table(res_dict)
    except KeyError as ex:
        print(ex)
        res = 'This section/command is not valid. Please try again.'

    bot.send_message(message.chat.id, res)


def ele_dict_to_table(res_dict):
    # res = '''
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      {:<10}: {:<10}
    #      '''.format(
    #     'DAY', res_dict.get('DAY'),
    #     'ROOM1', res_dict.get('ROOM1'),
    #     '11-12', res_dict.get('11-12'),
    #     'ROOM2', res_dict.get('ROOM2'),
    #     '12-1', res_dict.get('12-1'),
    #     'ROOM3', res_dict.get('ROOM3'),
    #     '1-2', res_dict.get('10-11'),
    #     'ROOM4', res_dict.get('ROOM4'),
    #     '3-4', res_dict.get('3-4'),
    #     'ROOM5', res_dict.get('ROOM5'),
    #     '4-5', res_dict.get('4-5')
    # )

    res = f'''
        DAY: {res_dict.get('DAY')}
        ROOM1: {res_dict.get('ROOM1')}
        11-12: {res_dict.get('11-12')}
        ROOM2: {res_dict.get('ROOM2')}
        12-1: {res_dict.get('12-1')}
        ROOM3: {res_dict.get('ROOM3')}
        1-2: {res_dict.get('10-11')}
        ROOM4: {res_dict.get('ROOM4')}
        3-4: {res_dict.get('3-4')}
        ROOM5: {res_dict.get('ROOM5')}
        4-5: {res_dict.get('4-5')}
        '''

    print(res)
    return res


bot.polling()
