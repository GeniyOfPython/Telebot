import telebot

inline_buy = telebot.types.InlineKeyboardButton(
    "Замовити",
    callback_data="замовити"
)

inline_go_to_site1 = telebot.types.InlineKeyboardButton(
    "Перейти до сайту",
    url="https://ek.ua/ua/APPLE-IPHONE-13-128GB.htm"
)

inline_go_to_site2 = telebot.types.InlineKeyboardButton(
    "Перейти до сайту",
    url="https://ek.ua/ua/APPLE-IPHONE-11-64GB.htm"
)

inline_go_to_site3 = telebot.types.InlineKeyboardButton(
    "Перейти до сайту",
    url="https://ek.ua/ua/APPLE-IPHONE-14-PRO-128GB.htm"
)

inline_go_to_site4 = telebot.types.InlineKeyboardButton(
    "Перейти до сайту",
    url="https://ek.ua/ua/SAMSUNG-GALAXY-A53-5G-128GB-6GB.htm"
)

inline_go_to_site5 = telebot.types.InlineKeyboardButton(
    "Перейти до сайту",
    url="https://ek.ua/ua/SAMSUNG-GALAXY-S22-ULTRA-256GB.htm"
)

inline_buttons1 = [
    inline_buy, 
    inline_go_to_site1, 
]

inline_buttons2 = [
    inline_buy,
    inline_go_to_site2
]

inline_buttons3 = [
    inline_buy,
    inline_go_to_site3
]

inline_buttons4 = [
    inline_buy,
    inline_go_to_site4
]

inline_buttons5 = [
    inline_buy,
    inline_go_to_site5
]