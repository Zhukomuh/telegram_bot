"""wow-guide tg-bot"""

import config
import telebot

from telebot import types
from guides import classes, raids

bot = telebot.TeleBot(config.TOKEN)

markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_raid_guide = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_class_guide = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('🗺 Гайди до рейдів')
btn2 = types.KeyboardButton('📖Гайди до класів')
main_menu_return_btn = types.KeyboardButton('◀️Повернутись до головного меню')

markup_naxx = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_voa = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_os = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_eoe = types.ReplyKeyboardMarkup(resize_keyboard=True)
raid_btn1 = types.KeyboardButton('☠Наксрамас')
ptchwrk_btn = types.KeyboardButton('💀Лоскутик')
grbbls_btn = types.KeyboardButton('💉Гроббулус')
glth_btn = types.KeyboardButton('🐶Глут')
thdds_btn = types.KeyboardButton('🧟‍♂Таддіус')

raid_btn2 = types.KeyboardButton('🐲️ Обсидіанове святилище')
raid_btn3 = types.KeyboardButton('👾 Око вічності')
raid_btn4 = types.KeyboardButton('🌚 Склеп Архавона')

markup_sham = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_hunt = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_rogue = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_mage = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_wlock = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_paly = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_druid = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_dk = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_priest = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_war = types.ReplyKeyboardMarkup(resize_keyboard=True)
class_war_btn = types.KeyboardButton('🪓Воїн')
arms_war_btn = types.KeyboardButton('🗡Озброєння')
fury_war_btn = types.KeyboardButton('⚔Лють')
prot_war_btn = types.KeyboardButton('🛡Захист')

class_paly_btn = types.KeyboardButton('🔨Паладин')
holy_paly_btn = types.KeyboardButton('🌟Святість')
prot_paly_btn = types.KeyboardButton('🛡Захист')
retr_paly_btn = types.KeyboardButton('🔥Відплата')

class_sham_btn = types.KeyboardButton('⚡️Шаман')
elem_sham_btn = types.KeyboardButton('⚡️Стихії')
enh_sham_btn = types.KeyboardButton('🛡Вдосконалення')
heal_sham_btn = types.KeyboardButton('🍃Зцілення')

class_mage_btn = types.KeyboardButton('🧙‍♀Маг')
arcn_mage_btn = types.KeyboardButton('💫Таємная магія')
fire_mage_btn = types.KeyboardButton('🔥Вогонь')
frst_mage_btn = types.KeyboardButton('🧊Лід')

class_wlock_btn = types.KeyboardButton('😈Чорнокнижник')
afl_wlock_btn = types.KeyboardButton('🤢Чаклунство')
demo_wlock_btn = types.KeyboardButton('😈Демонолог')
destr_wlock_btn = types.KeyboardButton('🔥Руйнування')

class_rogue_btn = types.KeyboardButton('🔪Розбійник')
muti_rogue_btn = types.KeyboardButton('⚔Ліквідація')
combat_rogue_btn = types.KeyboardButton('🔪Бій')
assas_rogue_btn = types.KeyboardButton('🥷🏻Скритність')

class_hunt_btn = types.KeyboardButton('🏹Мисливець')
beast_hunt_btn = types.KeyboardButton('🐺Повелитель звірів')
mm_hunt_btn = types.KeyboardButton('🏹Стрільба')
surv_hunt_btn = types.KeyboardButton('🪓Виживання')

class_druid_btn = types.KeyboardButton('🐾Друїд')
boomk_druid_btn = types.KeyboardButton('🌜Баланс')
cat_druid_btn = types.KeyboardButton('🐈Сила звіра: кіт')
bear_druid_btn = types.KeyboardButton('🐻Сила звіра: ведмідь')
restor_druid_btn = types.KeyboardButton('🍁Зцілення')

class_dk_btn = types.KeyboardButton('🧟‍♂Лицар Смерті')
blood_dk_btn = types.KeyboardButton('🩸Кров')
frost_dk_btn = types.KeyboardButton('🧊Лід')
unh_dk_btn = types.KeyboardButton('🤢Нечестивість')

class_priest_btn = types.KeyboardButton('✝Жрець')
disc_priest_btn = types.KeyboardButton('🛡Дисципліна')
holy_priest_btn = types.KeyboardButton('🕯Святість')
shdw_priest_btn = types.KeyboardButton('👻Пітьма')

markup_main.add(btn1, btn2)
markup_raid_guide.add(main_menu_return_btn, raid_btn1, raid_btn2, raid_btn3, raid_btn4)
markup_class_guide.add(main_menu_return_btn, class_dk_btn, class_priest_btn, class_druid_btn, class_hunt_btn,
                       class_rogue_btn, class_wlock_btn, class_mage_btn, class_paly_btn, class_war_btn, class_sham_btn)

markup_naxx.add(main_menu_return_btn, ptchwrk_btn, grbbls_btn, glth_btn, thdds_btn)
markup_os.add(main_menu_return_btn)
markup_eoe.add(main_menu_return_btn)
markup_voa.add(main_menu_return_btn)

markup_sham.add(elem_sham_btn, enh_sham_btn, heal_sham_btn, main_menu_return_btn)
markup_dk.add(blood_dk_btn, frost_dk_btn, unh_dk_btn, main_menu_return_btn)
markup_war.add(arms_war_btn, fury_war_btn, prot_war_btn, main_menu_return_btn)
markup_priest.add(disc_priest_btn, holy_priest_btn, shdw_priest_btn, main_menu_return_btn)
markup_paly.add(holy_paly_btn, prot_paly_btn, retr_paly_btn, main_menu_return_btn)
markup_mage.add(arcn_mage_btn, fire_mage_btn, frst_mage_btn, main_menu_return_btn)
markup_wlock.add(afl_wlock_btn, demo_wlock_btn, destr_wlock_btn, main_menu_return_btn)
markup_hunt.add(beast_hunt_btn, mm_hunt_btn, surv_hunt_btn, main_menu_return_btn)
markup_druid.add(boomk_druid_btn, cat_druid_btn, bear_druid_btn, restor_druid_btn, main_menu_return_btn)
markup_rogue.add(muti_rogue_btn, combat_rogue_btn, assas_rogue_btn, main_menu_return_btn)


@bot.message_handler(commands=["start"])
def wellcome(message):
    bot.send_message(message.chat.id, f"<b> Вітаємо, {message.from_user.first_name},"
                                      f" ми завжди готові допомогти тобі!</b>",
                     parse_mode='html'
                     )
    sti = open('stickers/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "<b> Розкажи, що привело тебе до нас?</b>", parse_mode='html',
                     reply_markup=markup_main)


@bot.message_handler(content_types=['text'])
def chose_guide(message):
    if message.chat.type == 'private':
        if message.text == '🗺 Гайди до рейдів':
            bot.send_message(message.chat.id, '<b>Обери рейд який тебе цікавить!</b>', parse_mode='html',
                             reply_markup=markup_raid_guide)

        elif message.text == '📖Гайди до класів':
            bot.send_message(message.chat.id, '<b>Обери клас який тебе цікавить!</b>', parse_mode='html',
                             reply_markup=markup_class_guide)

        elif message.text == '◀️Повернутись до головного меню':
            bot.send_message(message.chat.id, '<b>Повертаємось до головного меню.</b>', parse_mode='html',
                             reply_markup=markup_main)

        elif message.text == '☠Наксрамас':
            naxx = open('images/naxx.jpg', 'rb')
            bot.send_photo(message.chat.id, naxx,
                           '<b>[муркотіння кота]... О, не хвилюйтеся, містер Бігглсуорт,'
                           ' цього разу я нікому не дозволю вам нашкодити!</b>',
                           parse_mode='html',
                           reply_markup=markup_naxx)

        elif message.text == '🐲️ Обсидіанове святилище':
            sart = open('images/sart.jpg', 'rb')
            bot.send_photo(message.chat.id, sart, '<b>ДРАКАРІС! ...хмм, чи це не звідси?</b>',
                           parse_mode='html',
                           reply_markup=markup_os)

        elif message.text == '👾 Око вічності':
            maly = open('images/eoe_maly.jpg', 'rb')
            bot.send_photo(message.chat.id, maly,
                           '<b>"А що ви планували? Безпардонно увірватися в мої володіння... використовувати '
                           'магію... проти МЕНЕ?!"</b>',
                           parse_mode='html',
                           reply_markup=markup_eoe)

        elif message.text == '🌚 Склеп Архавона':
            voa = open('images/voa.jpeg', 'rb')
            bot.send_photo(message.chat.id, voa,
                           '<b>Вода. Земля. Вогонь. Повітря. Колись давно чотири народи жили у ....</b>',
                           parse_mode='html',
                           reply_markup=markup_eoe)

        elif message.text == '⚡️Шаман':
            sham = open('images/shamy.png', 'rb')
            bot.send_photo(message.chat.id, sham,
                           '<b>Стихії, направте мене!...[гуркіт грому]</b>',
                           parse_mode='html',
                           reply_markup=markup_sham)

        elif message.text == '🪓Воїн':
            war = open('images/war.jpg', 'rb')
            bot.send_photo(message.chat.id, war,
                           '<b>Ривок!.... [Покинути Тіло]</b>',
                           parse_mode='html',
                           reply_markup=markup_war)

        elif message.text == '🧟‍♂Лицар Смерті':
            dk = open('images/dk.jpg', 'rb')
            bot.send_photo(message.chat.id, dk,
                           '<b>ДК це така імбокоробочка з синіми очками🥶</b>',
                           parse_mode='html',
                           reply_markup=markup_dk)

        elif message.text == '✝Жрець':
            prst = open('images/priest.jpg', 'rb')
            bot.send_photo(message.chat.id, prst,
                           '<b>Побічні ефекти можуть включати: сухість у роті, нудоту, блювоту, затримку води, '
                           'болісний свербіж прямої кишки, галюцинації, деменцію, психоз, кому, смерть і неприємний'
                           ' запах з рота. Магія не для всіх. Перед використанням проконсультуйтеся з лікарем.</b>',
                           parse_mode='html',
                           reply_markup=markup_priest)

        elif message.text == '🔨Паладин':
            paly = open('images/paly.jpg', 'rb')
            bot.send_photo(message.chat.id, paly,
                           '<b>Я б\'ю двічі: один по голові, другий по кришці труни!</b>',
                           parse_mode='html',
                           reply_markup=markup_paly)

        elif message.text == '🧙‍♀Маг':
            mage = open('images/mage.jpg', 'rb')
            bot.send_photo(message.chat.id, mage,
                           '<b>Якщо ви не дасте мені спокою, я перетворю вас на безмозку вівцю!</b>',
                           parse_mode='html',
                           reply_markup=markup_mage)

        elif message.text == '😈Чорнокнижник':
            wlock = open('images/wlock.jpg', 'rb')
            bot.send_photo(message.chat.id, wlock,
                           '<b>А що, я люблю людей! [Вбиває мирних жителів]</b>',
                           parse_mode='html',
                           reply_markup=markup_wlock)

        elif message.text == '🏹Мисливець':
            hunt = open('images/hunt.jpg', 'rb')
            bot.send_photo(message.chat.id, hunt,
                           '<b>Хто з мечем до нас прийде... тих простіше застрелити.</b>',
                           parse_mode='html',
                           reply_markup=markup_hunt)

        elif message.text == '🐾Друїд':
            dru = open('images/dru.png', 'rb')
            bot.send_photo(message.chat.id, dru,
                           '<b>Я повинен захистити дику природу!</b>',
                           parse_mode='html',
                           reply_markup=markup_druid)

        elif message.text == '🔪Розбійник':
            rogue = open('images/rogue.jpg', 'rb')
            bot.send_photo(message.chat.id, rogue,
                           '<b>Я вбивав людей і за менше...</b>',
                           parse_mode='html',
                           reply_markup=markup_rogue)
        elif message.text == '⚔Ліквідація':
            bot.send_message(message.chat.id, classes.muti_rogue)
        elif message.text == '💀Лоскутик':
            bot.send_message(message.chat.id, raids.patchwerk)
        elif message.text == '💉Гроббулус':
            bot.send_message(message.chat.id, raids.grobbulus)
        elif message.text == '🐶Глут':
            bot.send_message(message.chat.id, raids.gluth)
        elif message.text == '🧟‍♂Таддіус':
            bot.send_message(message.chat.id, raids.thaddius)


if __name__ == '__main__':
    bot.infinity_polling()
