from rivescript import RiveScript
from app_resources.assets import polishDel
import re

class ProgramBot():

    def __init__(self):
        self.brain = RiveScript(utf8=True)
        self.brain.unicode_punctuation = re.compile(r'[.,!?;*]')
        self.brain.load_file("app_resources/bot_resources/program_bot.rive")
        self.brain.sort_replies()

    def answer(self,input):
        reply = self.brain.reply("localuser", polishDel(input))
        print('Program:',reply)