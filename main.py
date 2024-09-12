import time
import home_street
last_action = "none"
print("-----------")
print("Project-TXT")
print("-----------")
print("'A text based sandbox roleplaying game'")
print("")

def char():
    print("")
    print("-----------------")
    print("Character Creator")
    print("-----------------")
    print("")
    char_name=input("Character Name: ")
    print("")
    print("Character Gender")
    print("| 1 - Male | 2 - Female | 3 - Enby |")
    char_gender=input("Input: ")

    if char_gender == "1":
        char_gender = "Male"
    elif char_gender == "2":
        char_gender = "Female"
    elif char_gender == "3":
        char_gender == "Enby"
    else:
        print("invaild Character")
    return char_name, char_gender

char_name, char_gender = char() 

print("")
time.sleep(2)
print(f"your name is {char_name} and you are {char_gender}")
time.sleep(2)
print("you live in a small midwest town in the United States...")
time.sleep(2)
print("to the east of your small residental home is a railyard")
print("past that is endless forest for as far as you can see")
time.sleep(2)
print("to the south of the Town is a lot of farm land")
print("far past the farmland is InterState-90")
time.sleep(2)
print("All other directions lead to endless forest")
time.sleep(3)
print("")
print("you are in you room. you share your small residental house with your parents.")
print("your parents are pretty 'old timey', your mother spends most of her time cleaning the house and cooking")
print("while your father does nothing all day but sitting on the couch, watching American Football and drinking")
print("")
time.sleep(2)
print("")
print("you are in you room")
print("")
print("Info: the bar below shows where you can go")
print("| 1 - leave house | 2 - living room | 3 - dinneing room | ")
print("Info: the bar below shows what you can do")
print("| A - play on Gameboy | B - sleep |")
print("")
time.sleep(5)
print("there is not a story line yet, so just mess around")
print("")
time.sleep(5)
print("you are in you room")
print("| 1 - leave house |")
print("")
last_action = input("Input: ")
if last_action == "1"
    street_home()


