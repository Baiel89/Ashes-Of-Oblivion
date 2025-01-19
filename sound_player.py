import pygame

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.05)

    def play_menu_theme(self):
        menu_theme = 'assets/audios/menu-theme.mp3'
        pygame.mixer.music.load(menu_theme)
        pygame.mixer.music.play(-1)
        
    def pause_menu_theme(self):
        menu_theme = 'assets/audios/menu-theme.mp3'
        pygame.mixer.music.load(menu_theme)
        pygame.mixer.music.pause()

    def play_intro_theme(self):
        intro_theme = 'assets/audios/intro-theme.mp3'
        pygame.mixer.music.load(intro_theme)
        pygame.mixer.music.play(-1)
    
    def pause_intro_theme(self):
        intro_theme = 'assets/audios/intro-theme.mp3'
        pygame.mixer.music.load(intro_theme)
        pygame.mixer.music.pause()