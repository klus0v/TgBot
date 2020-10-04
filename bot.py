# -*- coding: utf8 -*-
import telebot
import requests
from datetime import datetime

bot = telebot.TeleBot('1050229554:AAFPkDrue8DnVa3T1ir-nCv3xg3Nq4ww-jA')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет,я Шпилс отправь мне любое сообщение и получи расписание.")
        user_id = message.from_user.id
        bot.send_message(815652307, message)
    else:
        user_id = message.from_user.id
        if user_id == 1033663402:
            bot.send_message(815652307, message.text)
        if user_id == 815652307:
            if message.text[0] == "+":
                bot.send_message(1033663402, message.text[1:])
                bot.send_message(815652307, "+")

        keyboard = telebot.types.InlineKeyboardMarkup()
        key_3 = telebot.types.InlineKeyboardButton(text='До ЕГЭ...', callback_data='ege')
        keyboard.add(key_3)
        rtx = message.from_user.first_name
        bot.send_message(message.from_user.id, text= "Привет, " + rtx , reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "rasp":
        res = requests.get('http://brgi.ucoz.ru/index/raspisanie_urokov/0-65', timeout=30.0)
        res.encoding = 'cp1251'
        urll = res.text
        z = urll.index("/raspisanie/")
        urll = urll[z:]
        z = urll.index('"')
        x = "http://brgi.ucoz.ru" + urll[:z]

        date = x[31:36] + ".2020"
        result = requests.get(x, timeout=30.0)
        result.encoding = 'cp1251'
        page = result.text
        l1 = page.index('09:15')
        l2 = page.index('10:10')
        l3 = page.index('11:15')
        l4 = page.index('12:20')
        l5 = page.index('13:15')
        l6 = page.index('14:15')
        if "15:10" in page:
            l7 = page.index('15:10')
        else:
            l7 = None
        aud = ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "201", "202", "203", "204", "205",
               "206", '207', "209", "210", "211", "212", "213", "214", "215", "301", "302", "303", "304", "305", "306",
               "307", "308", "208"]
        page1 = page[l1:l2].split(
            "<td class=T1 style=';border-top:2 solid #707070;text-align:left;border-top:2 solid #707070")
        page1 = page1[-2].split(">")

        page1 = "".join(page1)

        aud1 = ""
        for i in range(len(aud)):
            if aud[i] in page1:
                aud1 += aud[i]
        if len(aud1) == 6:
            aud1 = " (" + aud1[:3] + "/" + aud1[3:] + ")"
        else:
            aud1 = " (" + aud1 + ")"
        page1 = [word for word in page1 if 1039 < ord(word[0])]
        page1 = "".join(page1)
        if "Б" in page1[5:]:
            page1 = page1.replace("Б", " / Б")
        elif "Х" in page1[3:]:
            page1 = page1.replace("Х", " / Х")
        elif "И" in page1[5:]:
            page1 = page1.replace("И", " / И")
        elif "Ф" in page1[5:]:
            page1 = page1.replace("Ф", " / Ф")
        if len(page1) != 0:
            page1 = "1) " + page1

        page2 = page[l2:l3].split(" <td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page2 = page2[-2].split(">")
        page2 = "".join(page2)

        aud2 = ""
        for i in range(len(aud)):
            if aud[i] in page2:
                aud2 += aud[i]
        if len(aud2) == 6:
            aud2 = " (" + aud2[:3] + "/" + aud2[3:] + ")"
        else:
            aud2 = " (" + aud2 + ")"

        page2 = [word for word in page2 if 1039 < ord(word[0])]
        page2 = "".join(page2)
        if "Б" in page2[5:]:
            page2 = page2.replace("Б", " / Б")
        elif "Х" in page2[3:]:
            page2 = page2.replace("Х", " / Х")
        elif "И" in page2[5:]:
            page2 = page2.replace("И", " / И")
        elif "Ф" in page2[5:]:
            page2 = page2.replace("Ф", " / Ф")
        if len(page2) != 0:
            page2 = "2) " + page2

        page3 = page[l3:l4].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page3 = page3[-2]
        page3 = "".join(page3)

        aud3 = ""
        for i in range(len(aud)):
            if aud[i] in page3:
                aud3 += aud[i]
        if len(aud3) == 6:
            aud3 = " (" + aud3[:3] + "/" + aud3[3:] + ")"
        else:
            aud3 = " (" + aud3 + ")"

        page3 = [word for word in page3 if 1039 < ord(word[0])]
        page3 = "".join(page3)
        if "Б" in page3[5:]:
            page3 = page3.replace("Б", " / Б")
        elif "Х" in page3[3:]:
            page3 = page3.replace("Х", " / Х")
        elif "И" in page3[5:]:
            page3 = page3.replace("И", " / И")
        elif "Ф" in page3[5:]:
            page3 = page3.replace("Ф", " / Ф")
        if len(page3) != 0:
            page3 = "3) " + page3

        page4 = page[l4:l5].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page4 = page4[-2]

        aud4 = ""
        for i in range(len(aud)):
            if aud[i] in page4:
                aud4 += aud[i]
        if len(aud4) == 6:
            aud4 = " (" + aud4[:3] + "/" + aud4[3:] + ")"
        else:
            aud4 = " (" + aud4 + ")"

        page4 = [word for word in page4 if 1039 < ord(word[0])]
        page4 = "".join(page4)
        if "Б" in page4[5:]:
            page4 = page4.replace("Б", " / Б")
        elif "Х" in page4[3:]:
            page4 = page4.replace("Х", " / Х")
        elif "И" in page4[5:]:
            page4 = page4.replace("И", " / И")
        elif "Ф" in page4[5:]:
            page4 = page4.replace("Ф", " / Ф")
        if len(page4) != 0:
            page4 = "4) " + page4

        page5 = page[l5:l6].split(" <td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page5 = page5[-2]

        aud5 = ""
        for i in range(len(aud)):
            if aud[i] in page5:
                aud5 += aud[i]
        if len(aud5) == 6:
            aud5 = " (" + aud5[:3] + "/" + aud5[3:] + ")"
        else:
            aud5 = " (" + aud5 + ")"

        page5 = [word for word in page5 if 1039 < ord(word[0])]
        page5 = "".join(page5)
        if "Б" in page5[5:]:
            page5 = page5.replace("Б", " / Б")
        elif "Х" in page5[3:]:
            page5 = page5.replace("Х", " / Х")
        elif "И" in page5[5:]:
            page5 = page5.replace("И", " / И")
        elif "Ф" in page5[5:]:
            page5 = page5.replace("Ф", " / Ф")
        if len(page5) != 0:
            page5 = "5) " + page5

        page6 = page[l6:l7].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page6 = page6[-2]

        aud6 = ""
        for i in range(len(aud)):
            if aud[i] in page6:
                aud6 += aud[i]
        if len(aud6) == 6:
            aud6 = " (" + aud6[:3] + "/" + aud6[3:] + ")"
        elif len(aud6) != 0:
            aud6 = " (" + aud6 + ")"

        page6 = [word for word in page6 if 1039 < ord(word[0])]
        page6 = "".join(page6)
        if "Б" in page6[5:]:
            page6 = page6.replace("Б", " / Б")
        elif "Х" in page6[3:]:
            page6 = page6.replace("Х", " / Х")
        elif "И" in page6[5:]:
            page6 = page6.replace("И", " / И")
        elif "Ф" in page6[5:]:
            page6 = page6.replace("Ф", " / Ф")
        if len(page6) != 0:
            page6 = "6) " + page6

        page7 = page[l7:-1].split("<td class=T1 style=';text-align:left'>")
        page7 = page7[-2]

        aud7 = ""
        for i in range(len(aud)):
            if aud[i] in page7:
                aud7 += aud[i]
        if len(aud7) == 6:
            aud7 = " (" + aud7[:3] + "/" + aud7[3:] + ")"
        elif len(aud7) != 0:
            aud7 = " (" + aud7 + ")"

        page7 = [word for word in page7 if 1039 < ord(word[0])]
        page7 = "".join(page7)
        if "Б" in page7[5:]:
            page7 = page7.replace("Б", " / Б")
        elif "Х" in page7[3:]:
            page7 = page7.replace("Х", " / Х")
        elif "И" in page7[5:]:
            page7 = page7.replace("И", " / И")
        elif "Ф" in page7[5:]:
            page7 = page7.replace("Ф", " / Ф")

        if len(page7) != 0:
            page7 = "7) " + page7

        a = "Расписание 11а на " + date + "\n" + "\n"
        a += page1 + aud1 + "\n" + page2 + aud2 + "\n" + page3 + aud3 + "\n" + page4 + aud4 + "\n" + page5 + aud5 + "\n" + page6 + aud6 + "\n" + page7 + aud7 + "\n"

        if "язык" in a:
            a = a.replace("язык", " язык")
        if "литература" in a:
            a = a.replace("литература", " литература")
        if "культура" in a:
            a = a.replace("культура", " культура")
        if "актзал" in a:
            a = a.replace("актзал", " акт.зал")
        if "Алгебраиначалаанализа" in a:
            a = a.replace("Алгебраиначалаанализа", "Алгебра")

        bot.send_message(call.from_user.id, a)

    if call.data == "rasp1":
        res = requests.get('http://brgi.ucoz.ru/index/raspisanie_urokov/0-65', timeout=30.0)
        res.encoding = 'cp1251'
        urll = res.text
        z = urll.index("/raspisanie/")
        urll = urll[z:]
        z = urll.index('"')
        x = "http://brgi.ucoz.ru" + urll[:z]

        date = x[31:36] + ".2020"
        result = requests.get(x, timeout=30.0)
        result.encoding = 'cp1251'
        page = result.text
        l1 = page.index('09:15')
        l2 = page.index('10:10')
        l3 = page.index('11:15')
        l4 = page.index('12:20')
        l5 = page.index('13:15')
        l6 = page.index('14:15')
        if "15:10" in page:
            l7 = page.index('15:10')
        else:
            l7 = None
        aud = ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "201", "202", "203", "204", "205",
               "206", '207', "208", "209", "210", "211", "212", "213", "214", "215", "301", "302", "303", "304", "305",
               "306", "307", "308"]
        page1 = page[l1:l2].split(
            "<td class=T1 style=';border-top:2 solid #707070;text-align:left;border-top:2 solid #707070")
        page1 = page1[-1].split(">")

        page1 = "".join(page1)

        aud1 = ""
        for i in range(len(aud)):
            if aud[i] in page1:
                aud1 += aud[i]
        if len(aud1) == 6:
            aud1 = " (" + aud1[:3] + "/" + aud1[3:] + ")"
        else:
            aud1 = " (" + aud1 + ")"
        page1 = [word for word in page1 if 1039 < ord(word[0])]
        page1 = "".join(page1)
        if "Б" in page1[5:]:
            page1 = page1.replace("Б", " / Б")
        elif "Х" in page1[5:]:
            page1 = page1.replace("Х", " / Х")
        elif "И" in page1[5:]:
            page1 = page1.replace("И", " / И")
        elif "Ф" in page1[5:]:
            page1 = page1.replace("Ф", " / Ф")
        if len(page1) != 0:
            page1 = "1) " + page1

        page2 = page[l2:l3].split(" <td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page2 = page2[-1].split(">")
        page2 = "".join(page2)

        aud2 = ""
        for i in range(len(aud)):
            if aud[i] in page2:
                aud2 += aud[i]
        if len(aud2) == 6:
            aud2 = " (" + aud2[:3] + "/" + aud2[3:] + ")"
        else:
            aud2 = " (" + aud2 + ")"

        page2 = [word for word in page2 if 1039 < ord(word[0])]
        page2 = "".join(page2)
        if "Б" in page2[5:]:
            page2 = page2.replace("Б", " / Б")
        elif "Х" in page2[5:]:
            page2 = page2.replace("Х", " / Х")
        elif "И" in page2[5:]:
            page2 = page2.replace("И", " / И")
        elif "Ф" in page2[5:]:
            page2 = page2.replace("Ф", " / Ф")
        if len(page2) != 0:
            page2 = "2) " + page2

        page3 = page[l3:l4].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page3 = page3[-1]
        page3 = "".join(page3)

        aud3 = ""
        for i in range(len(aud)):
            if aud[i] in page3:
                aud3 += aud[i]
        if len(aud3) == 6:
            aud3 = " (" + aud3[:3] + "/" + aud3[3:] + ")"
        else:
            aud3 = " (" + aud3 + ")"

        page3 = [word for word in page3 if 1039 < ord(word[0])]
        page3 = "".join(page3)
        if "Б" in page3[5:]:
            page3 = page3.replace("Б", " / Б")
        elif "Х" in page3[5:]:
            page3 = page3.replace("Х", " / Х")
        elif "И" in page3[5:]:
            page3 = page3.replace("И", " / И")
        elif "Ф" in page3[5:]:
            page3 = page3.replace("Ф", " / Ф")
        if len(page3) != 0:
            page3 = "3) " + page3

        page4 = page[l4:l5].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page4 = page4[-1]

        aud4 = ""
        for i in range(len(aud)):
            if aud[i] in page4:
                aud4 += aud[i]
        if len(aud4) == 6:
            aud4 = " (" + aud4[:3] + "/" + aud4[3:] + ")"
        else:
            aud4 = " (" + aud4 + ")"

        page4 = [word for word in page4 if 1039 < ord(word[0])]
        page4 = "".join(page4)
        if "Б" in page4[5:]:
            page4 = page4.replace("Б", " / Б")
        elif "Х" in page4[5:]:
            page4 = page4.replace("Х", " / Х")
        elif "И" in page4[5:]:
            page4 = page4.replace("И", " / И")
        elif "Ф" in page4[5:]:
            page4 = page4.replace("Ф", " / Ф")
        if len(page4) != 0:
            page4 = "4) " + page4

        page5 = page[l5:l6].split(" <td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page5 = page5[-1]

        aud5 = ""
        for i in range(len(aud)):
            if aud[i] in page5:
                aud5 += aud[i]
        if len(aud5) == 6:
            aud5 = " (" + aud5[:3] + "/" + aud5[3:] + ")"
        else:
            aud5 = " (" + aud5 + ")"

        page5 = [word for word in page5 if 1039 < ord(word[0])]
        page5 = "".join(page5)
        if "Б" in page5[5:]:
            page5 = page5.replace("Б", " / Б")
        elif "Х" in page5[5:]:
            page5 = page5.replace("Х", " / Х")
        elif "И" in page5[5:]:
            page5 = page5.replace("И", " / И")
        elif "Ф" in page5[5:]:
            page5 = page5.replace("Ф", " / Ф")
        if len(page5) != 0:
            page5 = "5) " + page5

        page6 = page[l6:l7].split("<td class=T1 style=';text-align:left'><table cellspacing=0 border=0")
        page6 = page6[-1]

        aud6 = ""
        for i in range(len(aud)):
            if aud[i] in page6:
                aud6 += aud[i]
        if len(aud6) == 6:
            aud6 = " (" + aud6[:3] + "/" + aud6[3:] + ")"
        elif len(aud6) != 0:
            aud6 = " (" + aud6 + ")"

        page6 = [word for word in page6 if 1039 < ord(word[0])]
        page6 = "".join(page6)
        if "Б" in page6[5:]:
            page6 = page6.replace("Б", " / Б")
        elif "Х" in page6[5:]:
            page6 = page6.replace("Х", " / Х")
        elif "И" in page6[5:]:
            page6 = page6.replace("И", " / И")
        elif "Ф" in page6[5:]:
            page6 = page6.replace("Ф", " / Ф")
        if len(page6) != 0:
            page6 = "6) " + page6

        page7 = page[l7:-1].split("<td class=T1 style=';text-align:left'>")
        page7 = page7[-1]

        aud7 = ""
        for i in range(len(aud)):
            if aud[i] in page7:
                aud7 += aud[i]
        if len(aud7) == 6:
            aud7 = " (" + aud7[:3] + "/" + aud7[3:] + ")"
        elif len(aud7) != 0:
            aud7 = " (" + aud7 + ")"

        page7 = [word for word in page7 if 1039 < ord(word[0])]
        page7 = "".join(page7)
        if "Б" in page7[5:]:
            page7 = page7.replace("Б", " / Б")
        elif "Х" in page7[5:]:
            page7 = page7.replace("Х", " / Х")
        elif "И" in page7[5:]:
            page7 = page7.replace("И", " / И")
        elif "Ф" in page7[5:]:
            page7 = page7.replace("Ф", " / Ф")

        if len(page7) != 0:
            page7 = "7) " + page7

        a = "Расписание 11б на " + date + "\n" + "\n"
        a += page1 + aud1 + "\n" + page2 + aud2 + "\n" + page3 + aud3 + "\n" + page4 + aud4 + "\n" + page5 + aud5 + "\n" + page6 + aud6 + "\n" + page7 + aud7 + "\n"

        if "язык" in a:
            a = a.replace("язык", " язык")
        if "литература" in a:
            a = a.replace("литература", " литература")
        if "культура" in a:
            a = a.replace("культура", " культура")
        if "актзал" in a:
            a = a.replace("актзал", " акт.зал")
        if "Алгебраиначалаанализа" in a:
            a = a.replace("Алгебраиначалаанализа", "Алгебра")

        bot.send_message(call.from_user.id, a)

    if call.data == "ege":
        q = str(datetime.now())
        q = q[:10]
        q = q[-2:] + "." + q[-5:-3] + "." + "2020"
        d1 = datetime.strptime(q, "%d.%m.%Y")
        d2 = datetime.strptime("8.06.2020", "%d.%m.%Y")
        q = str((d2 - d1).days) + " дн. (до 8 июня)"
        bot.send_message(call.from_user.id, q)


bot.polling(none_stop=True)