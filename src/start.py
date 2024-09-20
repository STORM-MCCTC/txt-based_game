from browser import window

def wait(seconds, callback):
    window.setTimeout(callback, seconds * 1000)

def start(char_name, char_gender, char_age):
    char_name = char_name
    char_gender = char_gender
    char_age = char_age
    print(char_name)