from rivescript import RiveScript
from polDel import polishDel

bot = RiveScript()
bot.load_directory("./resources")
bot.sort_replies()

while True:
    msg = polishDel(input('Profesor> '))
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print('Student>', reply)
