dict = {
    'ą' : 'a',
    'ę' : 'e',
    'ć' : 'c',
    'ł' : 'l',
    'ń' : 'n',
    'ó' : 'o',
    'ś' : 's',
    'ź' : 'z',
    'ż' : 'z'
}

def polishDel(sentence):
    return ''.join(list(map(lambda x: dict[x] if x in dict else x, sentence.lower())))