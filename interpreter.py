from rivescript import RiveScript
from polDel import polishDel

import re

bot = RiveScript(utf8=True)
bot.unicode_punctuation = re.compile(r'[.,!?;:]')
bot.load_directory("./resources")
bot.sort_replies()

while True:
    msg = polishDel(input('Profesor> '))
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print('Student>', reply)
