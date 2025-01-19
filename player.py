class PlayerStats:
    def __init__(self):
        self.name = ""
        self.origin = ""
        self.level = ""

        self.life = ""
        self.mana = ""

        self.strength = ""
        self.dexterity = ""
        self.health = ""
        self.intelligence = ""
        self.charisma = ""

        self.ap = None
    
    def register_player_name(self, name):
        self.name = name
    
    def register_player_origin(self, origin):
        if origin == "Dunhart":
            self.strength = 15
            self.dexterity = 8
            self.health = 14
            self.intelligence = 5
            self.charisma = 8
            self.origin = "Dunhart"
        elif origin == "Eldoria":
            self.strength = 6
            self.dexterity = 12
            self.health = 9
            self.intelligence = 15
            self.charisma = 8
            self.origin = "Eldoria"
        elif origin == "Duskvale":
            self.strength = 6
            self.dexterity = 15
            self.health = 8
            self.intelligence = 12
            self.charisma = 9
            self.origin = "Duskvale"
        elif origin == "Hearthstone":
            self.strength = 6
            self.dexterity = 8
            self.health = 9
            self.intelligence = 12
            self.charisma = 15
            self.origin = "Hearthstone"

    def upgrade_ap(self, addition ):
        self.atribute =+ addition