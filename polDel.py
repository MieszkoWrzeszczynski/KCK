dict = {
    'ą' : 'a',
    'ć' : 'c',
    'ł' : 'l',
    'ń' : 'n',
    'ó' : 'o',
    'ś' : 's',
    'ź' : 'z',
    'ż' : 'z'
}

def polishDel(sentence):
    output = ''
    sentence = sentence.lower()
    for words in sentence:
        for char in words:
            if char in dict:
                char = dict[char]
            output = output + char;
    return output