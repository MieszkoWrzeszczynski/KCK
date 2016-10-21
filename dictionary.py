import csv

words = {}
file_name = 'dict.tsv'


def save():
    with open(file_name, 'w+') as file:
        writer = csv.writer(file, delimiter='\t', lineterminator='\n')
        for key, value in words.items():
            writer.writerow([key, value])


def load():
    with open(file_name, 'r') as file:
        for line in file:
            line = line.split()
            add(line[0], line[1])


def add(word, command):
    if word not in words:
        words[word] = command
        #print('({0},{1}) - Added!'.format(word, command))
    else:
        print('\'{0}\' key already exists in dictionary as ({0},{1})'.format(word, words[word]))


load()
print(words)
