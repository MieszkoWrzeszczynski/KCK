print("Hello, world!")

contributors = ['Mieszko','Adam','Maciej']

for contributor in contributors:
    print(contributor)

contributors.append('Tomasz')

import nltk
tekst = " Dzisiaj w Pozanniu jest okropna pogoda"
tokenz =  nltk.word_tokenize(tekst)
print(tokenz)
