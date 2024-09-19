
class player_char:
    def __init__(self):
        #! player set
        self.char_name = 'none'
        self.char_gender = 'none'
        self.char_age = 'none'

        #! inventory stuff
        self.char_inventory = []
        self.char_money = 50.0

        #! skills
        self.char_math_skill = 0
        self.char_history_skill = 0
        self.char_english_skill = 0
        self.char_science_skill = 0

        #! dynamic char State
        self.char_health = 100
        self.char_stress = 0.0
        self.char_happiness = 50.0
        self.char_strength = 50.0
        self.char_stamina = 100.0

        #! char Reputation
        self.char_reputation_school = 0.0
        self.char_reputation_authorities = 0.0
        self.char_reputation_criminal = 0.0

        #! not displayed init
 

    def player_set(self):
        print("")
        self.char_name = input("Character Name: ")
        print("")
        print("| 1- Male | 2 - Female | 3 - Enby | 4 - Other |")
        gender_choice = input("Select Gender (1-4): ")
        
        if gender_choice == '1':
            self.char_gender = "Male"
        elif gender_choice == '2':
            self.char_gender = "Female"
        elif gender_choice == '3':
            self.char_gender = "Enby"
        elif gender_choice == '4':
            self.char_gender = "Other"
        else:
            print("Invalid choice, try again.")
            self.player_set()  # Re-run the function if input is invalid

        print("")
        self.char_age = input("Character Age: ")


