class Hud:
    def __init__(self):
        pass
        

    def print_hud(self, name, origin, level, life, mana, strength, dexterity, health, intelligence, charisma):

        str_name = str(name).ljust(20)
        str_origin = str(origin).ljust(20)
        str_level = str(level).ljust(20)
        str_life = str(life).ljust(20)
        str_mana = str(mana).ljust(20)
        str_strength = str(strength).ljust(20)
        str_dexterity = str(dexterity).ljust(20)
        str_health = str(health).ljust(20)
        str_intelligence = str(intelligence).ljust(20)
        str_charisma = str(charisma).ljust(20)

        hud = f"""
x=================================================================================x========================================================================x
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|         Nombre: {str_name}                                            |                                                                        |
|                                                                                 |                                                                        |
|         Origen: {str_origin}                                            |                                                                        |
|                                                                                 |                                                                        |
|         Nivel: {str_level}                                             |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|         Vida: {str_life}                                              |                                                                        |
|                                                                                 |                                                                        |
|         Maná: {str_mana}                                              |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|         Strength: {str_strength}                                          |                                                                        |
|                                                                                 |                                                                        |
|         Dexterity: {str_dexterity}                                         |                                                                        |
|                                                                                 |                                                                        |
|         Health: {str_health}                                            |                                                                        |
|                                                                                 |                                                                        |
|         Intelligence: {str_intelligence}                                      |                                                                        |
|                                                                                 |                                                                        |
|         Charisma: {str_charisma}                                          |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
x=================================================================================x========================================================================x
        """
        print(hud)