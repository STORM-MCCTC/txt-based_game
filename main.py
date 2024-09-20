from src.char import player_char
from src.clothing import clothing
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