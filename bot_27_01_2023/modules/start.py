import telebot
import modules.bot as m_bot
import modules.user_send_message as m_usm
import modules.keyboard as m_key


@m_bot.bot.message_handler(commands=["start"])
def start(message):
    m_bot.bot.send_message(
        message.chat.id,
        "Hello!",
        reply_markup=m_key.menu_bar
    )
    
    m_bot.bot.register_next_step_handler(
        message,
        m_usm.user_send_message
    )
    
    