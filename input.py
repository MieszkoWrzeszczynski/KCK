import re

def normalize(input: str)->str:
    result = re.findall(r'\w+', input)
    result = list(map(lambda x: x.lower(), result))
    return result