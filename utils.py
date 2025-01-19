import os
import time

def clear_scr():
    os.system("cls")

def show_slow_text(texto, velocidad = 0.04):  #Write text slowly
    for letra in texto:
        print(letra, end = "", flush = True)
        time.sleep(velocidad)
    print("\n")

def draw_decoration(lines):  #Draw decoration
    for i in range(lines):
        print("=" * 156)

def error_command():
    print("Comando no detectado")