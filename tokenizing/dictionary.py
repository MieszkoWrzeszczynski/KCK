from os import listdir
from os.path import isfile, join
import os


dirPath = os.path.dirname(os.path.realpath(__file__))
dirPathRaw = dirPath+"\\raw\\"
dirPathTokens = dirPath+"\\tokens\\"


rawFiles = [f for f in listdir(dirPathRaw) if isfile(join(dirPathRaw, f))]
print ("Dir:", dirPath, "\nRaw Files:", rawFiles)


for fileName in rawFiles:
    wordList = []
    with open(dirPathRaw + fileName, 'r') as file:
        for line in file:
            line=line.replace('\n','').replace(',','').split()
            wordList.extend(line)

    wordSet=set(wordList)
#TODO   bez polskich znakow ++
    with open(dirPathTokens + 't_' + fileName.upper(), 'w+') as file:
        for item in wordSet:
            file.write("%s " % item)

tokensFiles = [f for f in listdir(dirPathTokens) if isfile(join(dirPathTokens, f))]
print("t_Tokens: ", tokensFiles)