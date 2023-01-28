import telebot
import modules.keyboard as m_key
import modules.bot as m_bot
from modules.find_path import find_path
import modules.inline_keyboard as m_ik



def user_send_message(message):
    if message.text.lower() == "new":
        image1 = find_path(f"images/image1.jpg")
        image2 = find_path(f"images/image1.jpg")
        image3 = find_path(f"images/image1.jpg")
        image4 = find_path(f"images/image1.jpg")
        image5 = find_path(f"images/image1.jpg")
            
        m_bot.bot.send_photo(
            message.chat.id,
            open(image1, "rb"),
            'Телефон',
            reply_markup= m_ik.inline_bar1
        )
        
        m_bot.bot.send_photo(
            message.chat.id,
            open(image2, "rb"),
            'Телефон',
            reply_markup= m_ik.inline_bar2
        )
        
        m_bot.bot.send_photo(
            message.chat.id,
            open(image3, "rb"),
            'Телефон',
            reply_markup= m_ik.inline_bar3
        )
        
        m_bot.bot.send_photo(
            message.chat.id,
            open(image4, "rb"),
            'Телефон',
            reply_markup= m_ik.inline_bar4
        )
        
        m_bot.bot.send_photo(
            message.chat.id,
            open(image5, "rb"),
            'Телефон',
            reply_markup= m_ik.inline_bar5
        )