from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./resources")
bot.sort_replies()

while True:
    msg = input('Profesor> ')
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print('Student>', reply)