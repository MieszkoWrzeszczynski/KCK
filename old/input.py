import re

def normalize(input: str)->str:
    result = re.findall(r'\w+', input)
    result = list(map(lambda x: x.lower(), result))
    return result


print (normalize("To jest przykładowy tekst"))

tekst = input()
tekst = tekst.lower()
print(tekst.split())