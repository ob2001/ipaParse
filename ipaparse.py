import tomli

with open("x-sampa.toml", mode = 'rb') as fp:
    data = tomli.load(fp)

tokens = data.keys()

def get_ipa_char(code):
    return data[code]["ipa"]

def parse_str(str):
    res = ''
    i = 0
    while i < len(str):
        if str[i:i+4] in tokens:
            res += data[str[i:i+4]]["ipa"]
            i += 4
        elif str[i:i+3] in tokens:
            res += data[str[i:i+3]]["ipa"]
            i += 3
        elif str[i:i+2] in tokens:
            res += data[str[i:i+2]]["ipa"]
            i += 2
        elif str[i] in tokens:
            res += data[str[i]]["ipa"]
            i += 1
        else:
            res += ' '
            i += 1
    
    return res

def get_diacritic_by_code(code):
    for key, val in data.items():
        # print(key, val)
        if isinstance(val, dict) and val.get("code") != None and val.get("code") == code:
            return key
    return ''

print("[" + parse_str("<F>\"hE%5o <R>w@`ld") + "]!")