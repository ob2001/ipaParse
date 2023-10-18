import json

with open("x-sampa.json", encoding="utf-8") as json_file:
    data = json.load(json_file)

def get_ipa_char(code):
    return data[code]["ipa"]

def print_ipa_char(code):
    print(data[code]["ipa"])

def parse_str(str):
    pass

def hello_world_by_chars():
    print("["
        + get_ipa_char("<F>")
        + get_ipa_char("\"")
        + get_ipa_char("h") 
        + get_ipa_char("E") 
        + get_ipa_char("%")
        + get_ipa_char("l") 
        + get_ipa_char("o") 
        + " " 
        + get_ipa_char("<R>")
        + get_ipa_char("w") 
        + get_ipa_char("U") 
        + get_ipa_char("r\\")
        + get_ipa_char("l")
        + get_ipa_char("d")
        + "]!")
    
hello_world_by_chars()