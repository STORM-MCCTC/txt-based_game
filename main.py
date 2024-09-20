from src.char import player_char
from src.clothing import clothing
from src.items import items
from src.start import start
from browser import document
#from browser.widgets.dialog import InfoDialog

clothing()
items()
pant, Shirt, Outerwear, Footwear_under, Footwear, underware_upper, underware_lower, Accessories_head, Accessories_face, Accessories_face_mask, Accessories_back, Accessories_neck, Accessories_hands, Dress, coverall = clothing()
pant_item, Shirt_item, Outerwear_item, Footwear_under_item, Footwear_item, underware_upper_item, underware_lower_item, Accessories_head_item, Accessories_face_item, Accessories_face_mask_item, Accessories_back_item, Accessories_neck_item, Accessories_hands_item, Dress_item, coverall_item, Long_blunt_weapons, short_blunt_weapons, long_blade_weapons, short_blade_weapons = items()

player = player_char()

player.player_set()

print(f"""
Character Info:
---------------
Name: {player.char_name}
Gender: {player.char_gender}
Age: {player.char_age}

Inventory:
---------------
Items: {player.char_inventory}
Money: ${player.char_money}

Skills:
---------------
Math: {player.char_math_skill}
History: {player.char_history_skill}
English: {player.char_english_skill}
Science: {player.char_science_skill}

Character State:
---------------
Health: {player.char_health}
Stress: {player.char_stress}
Happiness: {player.char_happiness}
Strength: {player.char_strength}
Stamina: {player.char_stamina}

Reputation:
---------------
School Reputation: {player.char_reputation_school}
Authorities Reputation: {player.char_reputation_authorities}
Criminal Reputation: {player.char_reputation_criminal}
""")
print("")
start(player.char_name, player.char_gender, player.char_age)



document["line01"].text = "Character Info:"
document["line02"].text = "---------------"
document["line03"].text = f"Name: {player.char_name}"
document["line04"].text = f"Gender: {player.char_gender}"
document["line05"].text = f"Age: {player.char_age}"
document["line06"].text = ""  # Blank line
document["line07"].text = ""  # Blank line
document["line08"].text = "Inventory:"
document["line09"].text = "---------------"
document["line10"].text = f"Items: {', '.join(player.char_inventory)}"  
document["line11"].text = f"Money: ${player.char_money}"
document["line12"].text = ""  # Blank line
document["line13"].text = ""  # Blank line
document["line14"].text = "Skills:"
document["line15"].text = "---------------"
document["line16"].text = f"Math: {player.char_math_skill}"
document["line17"].text = f"History: {player.char_history_skill}"
document["line18"].text = f"English: {player.char_english_skill}"
document["line19"].text = f"Science: {player.char_science_skill}"
document["line20"].text = ""  # Blank line
document["line21"].text = ""  # Blank line
document["line22"].text = "Character State:"
document["line23"].text = "---------------"
document["line24"].text = f"Health: {player.char_health}"
document["line25"].text = f"Stress: {player.char_stress}"
document["line26"].text = f"Happiness: {player.char_happiness}"
document["line27"].text = f"Strength: {player.char_strength}"
document["line28"].text = f"Stamina: {player.char_stamina}"
document["line29"].text = ""  # Blank line
document["line30"].text = ""  # Blank line
document["line31"].text = "Reputation:"
document["line32"].text = "---------------"
document["line33"].text = f"School Reputation: {player.char_reputation_school}"
document["line34"].text = f"Authorities Reputation: {player.char_reputation_authorities}"
document["line35"].text = f"Criminal Reputation: {player.char_reputation_criminal}"





