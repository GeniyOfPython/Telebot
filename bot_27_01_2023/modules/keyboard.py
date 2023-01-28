import telebot
import modules.buttons_keyboard as m_btk

menu_bar = telebot.types.ReplyKeyboardMarkup()

menu_bar.add(m_btk.button_new)
menu_bar.add(m_btk.button_sale)
menu_bar.add(m_btk.button_discount)