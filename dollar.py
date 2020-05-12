import requests
from bs4 import BeautifulSoup
import telebot

bot = telebot.TeleBot('1089222329:AAGKNacApj2ozz-GLwg-EG5W3DrTvIIG2Z0')

dollar = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83&aqs=chrome.0.35i39j69i57j35i39j0l2j69i61l3.2152j1j4&sourceid=chrome&ie=UTF-8'
euro = 'https://www.google.com/search?safe=strict&sxsrf=ALeKk01MwcmPJqlx6lR5TG2RUqPzQNJjXw%3A1585460974862&ei=7jaAXv2eNJ6Ck74Pz8-84Aw&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5&gs_lcp=CgZwc3ktYWIQARgAMgQIIxAnMgIIADICCAAyAggAMgIIADICCAAyBQgAEIMBMgIIADICCAAyAggAOgQIABBHOgcIABCDARBDOgkIIxAnEEYQggI6BwgAEBQQhwI6BAgAEApQ_f2CA1j8noMDYLSsgwNoA3ADeACAAUqIAcUEkgEBOZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab'
funt = 'https://www.google.com/search?safe=strict&sxsrf=ALeKk00go8pEyd9cDS2y5hpEqcqSLCoUOg%3A1585467322232&ei=uk-AXsDlDbKKmwXJ4Z-IDQ&q=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%83%D0%BD%D1%82%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%84&gs_lcp=CgZwc3ktYWIQARgBMgQIIxAnMgIIADICCAAyBwgAEBQQhwIyAggAMgIIADICCAAyAggAMgIIADIFCAAQgwE6BAgAEEc6BAgAEEM6CQgjECcQRhCCAjoECAAQClD-2lhYvLhZYL7FWWgCcAJ4AIABVogB0gSSAQE5mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab'
frank = 'https://www.google.com/search?safe=strict&sxsrf=ALeKk02WK38eS060iA0LHvhtqDVwEWGaVg%3A1585468995692&ei=Q1aAXvDJKeLImwWGr6LADw&q=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%80%D0%B0%D0%BD%D0%BA%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%84&gs_lcp=CgZwc3ktYWIQARgBMgkIIxAnEEYQggIyBAgjECcyBwgAEBQQhwIyAggAMgIIADICCAAyAggAMgIIADICCAAyBQgAEIMBOgQIABBHUPnCqwFY6MqrAWCc1asBaABwAngAgAFAiAH7AZIBATSYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('курс доллара', 'курс евро', 'курс фунта', 'курс франка')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, что ты хочешь?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def course(message):
    if message.text == 'курс доллара':
        full_page = requests.get(dollar, headers=header)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        bot.send_message(message.chat.id,'1 доллар = ' + convert[0].text)
    elif message.text == 'курс евро':
        full_page1 = requests.get(euro, headers=header)
        soup1 = BeautifulSoup(full_page1.content, 'html.parser')
        convert1 = soup1.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2} )
        bot.send_message(message.chat.id,'1 евро = ' + convert1[0].text)
    elif message.text == 'курс фунта':
        full_page2 = requests.get(funt, headers=header)
        soup2 = BeautifulSoup(full_page2.content, 'html.parser')
        convert2 = soup2.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2} )
        bot.send_message(message.chat.id,'1 фунт = ' + convert2[0].text)
    elif message.text == 'курс франка':
        full_page3 = requests.get(frank, headers=header)
        soup3 = BeautifulSoup(full_page3.content, 'html.parser')
        convert3 = soup3.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2} )
        bot.send_message(message.chat.id,'1 франк = ' + convert3[0].text)



bot.polling()
