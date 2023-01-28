import telebot
from modules.inline_buttons import inline_buy, inline_go_to_site1, inline_go_to_site2, inline_go_to_site3, inline_go_to_site4, inline_go_to_site5

inline_bar1 = telebot.types.InlineKeyboardMarkup(
    row_width=2
)

inline_bar2 = telebot.types.InlineKeyboardMarkup(
    row_width=2
)

inline_bar3 = telebot.types.InlineKeyboardMarkup(
    row_width=2
)

inline_bar4 = telebot.types.InlineKeyboardMarkup(
    row_width=2
)

inline_bar5 = telebot.types.InlineKeyboardMarkup(
    row_width=2
)

# for button in inline_buttons1:
#     inline_bar1.add(inline_buttons1[button])

# for button in inline_buttons2:
#     inline_bar2.add(inline_buttons2[button])
    
# for button in inline_buttons3:
#     inline_bar3.add(inline_buttons3[button])
    
# for button in inline_buttons4:
#     inline_bar4.add(inline_buttons4[button])
    
# for button in inline_buttons5:
#     inline_bar5.add(inline_buttons5[button])

inline_bar1.add(inline_buy)
inline_bar1.add(inline_go_to_site1)

inline_bar2.add(inline_buy)
inline_bar2.add(inline_go_to_site2)

inline_bar3.add(inline_buy)
inline_bar3.add(inline_go_to_site3)

inline_bar4.add(inline_buy)
inline_bar4.add(inline_go_to_site4)

inline_bar5.add(inline_buy)
inline_bar5.add(inline_go_to_site5)