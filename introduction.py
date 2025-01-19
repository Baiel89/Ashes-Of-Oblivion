from utils import clear_scr, show_slow_text, draw_decoration
import time

class GameIntro:
    def __init__(self):
        pass

    def print_introduction_text(self):  #Script of the introduction
        draw_decoration(3)

        show_slow_text("EN UN MUNDO EN GUERRA ENTRE MORTALES Y DIOSES...")
        time.sleep(6)

        show_slow_text("DONDE LA PAZ ERA INPENSABLE Y EL CONFLICTO ERA CONSTANTE")
        time.sleep(6)
        clear_scr()
        draw_decoration(3)

        show_slow_text("EL DESASTRE OCURRIÓ")
        time.sleep(6)

        show_slow_text("LA BARRERA ENTRE LOS REINOS SE ABRIÓ, DEMONIOS, ESPECTROS I CRIATURAS OLVIDADAS DEAMBULARON POR LA TIERRA DURANTE CINCO MIL AÑOS...")
        time.sleep(6)
        clear_scr()
        draw_decoration(3)

        show_slow_text("ESTAS MISMAS CRIATURAS FUERON LAS QUE TE ARREBATARON TODO...")
        time.sleep(6)

        show_slow_text("DESPUÉS DE AÑOS DE GUERRAS, DESTRUCCIÓN I MUERTE, LLEGÓ EL ALMA SUPERVIVIENTE DE EIRENE, DIOSA DE LA PAZ CARGADA DE ODIO Y VENGANZA")
        time.sleep(6)
        clear_scr()
        draw_decoration(3)

        show_slow_text("CONSIGUIÓ PURIFICAR A LOS SERES CORROMPIDOS I MANTUVO LA PAZ DURANTE MUCHO TIEMPO Y LAS BARRERAS ENTRE LOS REINOS VOLVIERON A SELLARSE ")
        time.sleep(6)

        show_slow_text("ESTO NO DURÓ MUCHO, ANUBIS, HERALDO DE LA DESTRUCCIÓN INVOCÓ A SUS EMISARIOS DE LA MUERTE Y RETIRARON AL ALMA VENGATIVA DE EIRENE DE SU REINADO DE PAZ")
        time.sleep(6)
        clear_scr()
        draw_decoration(3)

        show_slow_text("ANUBIS CONSIGUIÓ VOLVER LA DESTRUCCIÓN A LA TIERRA")
        time.sleep(6)

        show_slow_text("ERES UNO DE LOS QUE QUEDAN CON VIDA DESPUÉS DEL DESASTRE")
        time.sleep(6)
        clear_scr()
        draw_decoration(3)

        show_slow_text("TU OBJETIVO ES DEVOLVER EL ALMA DE EIRENE A SU TRONO Y DEVOLVER LA PAZ A LA TIERRA")
        time.sleep(6)

    def print_name_selector(self):
        draw_decoration(3)
        show_slow_text("¿Cuál es tu nombre?")

    def print_origin_options(self):
        draw_decoration(3)

        show_slow_text("ELIGE TUS ORIGENES:")

        print("1.Dunhart:\n")
        show_slow_text("     Un pueblo montañoso rodeado de minas, conocido por sus guerreros endurecidos y la forja de armas contundentes.")
        print("     *Strength = 15 - Dexterity = 8 - Health = 14 - Intelligence = 5 - Charisma = 8\n")
        time.sleep(0.2)

        print("2.Eldoria\n")
        show_slow_text("     Una ciudad flotante sobre el mar, famosa por su sabiduría arcana y antiguos templos.")
        print("     Strength = 6 - Dexterity = 12 - Health = 9 - *Intelligence = 15 - Charisma = 8\n")
        time.sleep(0.2)

        print("3.Duskvale\n")
        show_slow_text("     Una ciudad oculta entre sombras, famosa por sus callejones angostos y edificios altos, hogar de ladrones.")
        print("     Strength = 6 - *Dexterity = 15 - Health = 8 - Intelligence = 12 - Charisma = 9\n")
        time.sleep(0.2)

        print("4.Hearthstone\n")
        show_slow_text("     Un pueblo tranquilo rodeado de campos, conocido por su hospitalidad y sus divertidas fiestas.")
        print("     Strength = 6 - Dexterity = 8 - Health = 9 - Intelligence = 12 - *Charisma = 15\n")


    def add_ap(self, ap, strength, dexterity, health, intelligence, charisma):
        draw_decoration(3)
        print("Tienes", ap, "puntos de atributo disponibles:")
        print("\n")
        print("1:Strength:", strength)
        print("\n")
        print("2:Dexterity:", dexterity)
        print("\n")
        print("3:Health:", health)
        print("\n")
        print("4:Intelligence:", intelligence)
        print("\n")
        print("5:Charisma:", charisma)
        print("\n")

    def player_resume(self, name, origin, strength, dexterity, health, intelligence, charisma):
        draw_decoration(3)
        print("\n")
        print("Nombre:", name)
        print("\n")
        print("Origen:", origin)
        print("\n")
        draw_decoration(1)
        print("Atributos:")
        draw_decoration(1)
        print("\n")
        print("Strength:", strength)
        print("\n")
        print("Dexterity:", dexterity)
        print("\n")
        print("Health:", health)
        print("\n")
        print("Intelligence:", intelligence)
        print("\n")
        print("Charisma:", charisma)
        print("\n")
        draw_decoration(3)
        print("\n")
        print("¿Estás seguro de que este es tu personaje? (Y/N)")