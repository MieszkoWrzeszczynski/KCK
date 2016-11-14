#!/usr/bin/python3

subDict = {
	'ą' : 'a',
	'ć' : 'c',
	'ę' : 'e',
	'ł' : 'l',
	'ń' : 'n',
	'ó' : 'o',
	'ś' : 's',
	'ź' : 'z',
	'ż' : 'z',
	 }

def replacePolish(word):
    output=''
    word = word.lower()
    for c in word:
        if c in subDict:
            c = subDict[c]
        output+=c
    return output