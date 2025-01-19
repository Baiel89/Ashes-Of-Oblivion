################################################################################################
import time
from menu import print_menu
from utils import clear_scr, error_command, show_slow_text
from introduction import GameIntro
from sound_player import SoundPlayer
from player import PlayerStats
from characters import Characters
from hud import Hud
################################################################################################
run = True
menu = True
introduction = False
play = False
################################################################################################
intro_opening = True
intro_name_selector = False
intro_origin = False
intro_add_ap = False
intro_player_resume = False
################################################################################################
user_input = None

game_intro = GameIntro()
sound_player = SoundPlayer()
player_stats = PlayerStats()
characters = Characters()
hud = Hud()

sound_player.play_menu_theme()

while run:

    while menu:
        clear_scr()
        print_menu()
        user_input = input("--> ")

        if user_input == "1":
            print("Estás seguro de que quieres iniciar una nueva partida?, tu progreso anterior será borrado (Y/N)")
            user_input = input("--> ")
            if user_input == "Y" or user_input == "y":
                sound_player.pause_menu_theme()
                sound_player.play_intro_theme()
                player_stats.upgrade_ap(2)
                introduction = True
                menu = False
            elif user_input == "N" or user_input == "n":
                pass
            else:
                error_command()
                time.sleep(1)
                pass

        elif user_input == "4":
            run = False
            quit()

        elif user_input == "R" or user_input == "r":
            pass

        else:
            error_command()
            time.sleep(1)
            pass
        
    while introduction:
        if intro_opening:
            clear_scr()
            #game_intro.print_introduction_text()
            intro_opening = False
            intro_name_selector = True
        
        if intro_name_selector:
            clear_scr()
            game_intro.print_name_selector()
            user_input = input("-->")
            if len(user_input) > 20:
                print("El nombre introducido es demasiado largo, porfavor introduce otro nombre")
                print("\n")
                time.sleep(2)
            elif len(user_input) <= 0:
                print("No se pude dejar vacío el nombre, porfavor introduce un nombre válido")
                print("\n")
                time.sleep(2)
            else:
                player_stats.register_player_name(user_input)
                intro_name_selector = False
                intro_origin = True

        if intro_origin:
            clear_scr()
            game_intro.print_origin_options()
            user_input = input("--> ")

            if user_input == "1":
                print("¿Estás seguro de que tu ciudad de origen és Dunhart? (Y/N)")
                user_input = input("-->")
                if user_input == "Y" or user_input == "y":
                    player_stats.register_player_origin("Dunhart")
                    intro_origin = False
                    intro_add_stats_points = True
                elif user_input == "N" or user_input == "n":
                    pass
                else:
                    error_command()
                    time.sleep(1)
                    pass

            elif user_input == "2":
                print("¿Estás seguro de que tu ciudad de origen és Eldoria? (Y/N)")
                user_input = input("-->")
                if user_input == "Y" or user_input == "y":
                    player_stats.register_player_origin("Eldoria")
                    intro_origin = False
                    intro_add_stats_points = True
                elif user_input == "N" or user_input == "n":
                    pass
                else:
                    error_command()
                    time.sleep(1)
                    pass

            elif user_input == "3":
                print("¿Estás seguro de que tu ciudad de origen és Duskvale? (Y/N)")
                user_input = input("-->")
                if user_input == "Y" or user_input == "y":
                    player_stats.register_player_origin("Duskvale")
                    intro_origin = False
                    intro_add_stats_points = True
                elif user_input == "N" or user_input == "n":
                    pass
                else:
                    error_command()
                    time.sleep(1)
                    pass
            
            elif user_input == "4":
                print("¿Estás seguro de que tu ciudad de origen és Hearthstone? (Y/N)")
                user_input = input("-->")
                if user_input == "Y" or user_input == "y":
                    player_stats.register_player_origin("Hearthstone")
                    intro_origin = False
                    intro_add_stats_points = True
                elif user_input == "N" or user_input == "n":
                    pass
                else:
                    error_command()
                    time.sleep(1)
                    pass
            
            else:
                error_command()
                time.sleep(1)
                pass

        if intro_add_ap:
            clear_scr()
            if stats_points != 0:
                game_intro.add_ap(player_stats.ap, player_stats.strength, player_stats.dexterity, player_stats.health, player_stats.intelligence, player_stats.charisma)
            user_input = input("-->")
            if user_input == "1" and stats_points > 0:
                player_stats.strength += 1
                stats_points -= 1
                pass
            
            elif user_input == "2" and stats_points > 0:
                player_stats.dexterity += 1
                stats_points -= 1
                pass

            elif user_input == "3" and stats_points > 0:
                player_stats.health += 1
                stats_points -= 1
                pass

            elif user_input == "4" and stats_points > 0:
                player_stats.intelligence += 1
                stats_points -= 1
                pass

            elif user_input == "5" and stats_points > 0:
                player_stats.charisma += 1
                stats_points -= 1
                pass

            else:
                error_command()
                time.sleep(1)
                pass

            if stats_points > 0:
                clear_scr()
                game_intro.add_stats_points(stats_points, player_stats.strength, player_stats.dexterity, player_stats.health, player_stats.intelligence, player_stats.charisma)

            elif stats_points == 0:
                time.sleep(2)
                intro_add_stats_points = False
                intro_add_stats_points = True

        if intro_player_resume:
            clear_scr()
            game_intro.player_resume(player_stats.name, player_stats.origin, player_stats.strength, player_stats.dexterity, player_stats.health, player_stats.intelligence, player_stats.charisma)
            user_input = input("-->")
            if user_input == "Y" or user_input == "y":
                intro_player_resume = False
                introduction = False
                play = True
            elif user_input == "N" or user_input == "n":
                stats_points = 2
                intro_name_selector = True
                intro_player_resume = False
            else:
                error_command()
                time.sleep(1)
                pass

    while play:
        clear_scr()
        hud.print_hud(player_stats.name, player_stats.origin, player_stats.level, player_stats.life, player_stats.mana, player_stats.strength, player_stats.dexterity, player_stats.health, player_stats.intelligence, player_stats.charisma)
        user_input = input("-->")