import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import base64

pygame.init()
pygame.mixer.music.load("song.mp3") #onehundredthousand
pygame.mixer.music.play(-1)
pygame.display.set_mode((800, 600))

level = -1
text = ""
text2=""
auswahl=""
cipher = ""
eingabe_phase = 0  
font = pygame.font.SysFont(None, 48)

def otp_encrypt(message, keyy):
    message_bytes = message.encode('utf-8')
    key_bytes = keyy.encode('utf-8')
    encrypted = bytes([m ^ k for m, k in zip(message_bytes, key_bytes)])
    return base64.b64encode(encrypted).decode('ascii')

def otp_decrypt(message, keyy):
    message=base64.b64decode(message).decode('ascii')
    message_bytes = message.encode('utf-8')
    key_bytes = keyy.encode('utf-8')
    encrypted = bytes([m ^ k for m, k in zip(message_bytes, key_bytes)])
    return encrypted.decode('ascii')

def draw():
    global text,text2,cipher,eingabe_phase,auswahl
    screen.clear()
    if level == -1:
        text = ""
        text2=""
        auswahl=""
        cipher = ""
        screen.blit("title", (0, 0))
        eingabe_phase=0
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("back", (0, 0))
        if eingabe_phase==0:
            screen.draw.text("Do you want a) encode or b) decode?", center=(400, 130), fontsize=24, color=(25, 200, 255))
            screen.draw.text(auswahl, center=(400, 180), fontsize=32, color=(200, 200, 200))
        if eingabe_phase == 1:
            screen.draw.text("Enter text to encrypt:", center=(400, 130), fontsize=24, color=(25, 200, 255))
            screen.draw.text(text, center=(400, 180), fontsize=32, color=(200, 200, 200))
        elif eingabe_phase == 2:
            screen.draw.text("Enter key (same length):", center=(400, 130), fontsize=24, color=(25, 200, 255))
            screen.draw.text(text2, center=(400, 180), fontsize=32, color=(200, 200, 200))
        elif eingabe_phase == 3:
            screen.draw.text("Encrypted Text:", center=(400, 130), fontsize=24, color=(25, 200, 255))
            screen.draw.text(cipher, center=(400, 180), fontsize=24, color=(255, 255, 0))
        elif eingabe_phase == 4:
            screen.draw.text("Your text must be the same length like the key!", center=(400, 130), fontsize=24, color=(25, 200, 255))
            #screen.draw.text(cipher, center=(400, 180), fontsize=24, color=(255, 255, 0))
    elif level==2:
        screen.blit("back",(0,0))
        if eingabe_phase == 1:
            screen.draw.text("Enter text to decrypt:", center=(400, 130), fontsize=24, color=(25, 200, 255))
            screen.draw.text(text, center=(400, 180), fontsize=32, color=(200, 200, 200))
        elif eingabe_phase == 2:
            screen.draw.text("Enter key (same length):", center=(400, 130), fontsize=24, color=(25, 200, 255))
            screen.draw.text(text2, center=(400, 180), fontsize=32, color=(200, 200, 200))
        elif eingabe_phase == 3:
            screen.draw.text("Decrypted Text:", center=(400, 130), fontsize=24, color=(25, 200, 255))
            screen.draw.text(cipher, center=(400, 180), fontsize=24, color=(255, 255, 0))

def update():
    global level, eingabe_phase
    if level == -1 and keyboard.space:
        level = 0
    elif level == 0 and keyboard.RETURN:
        level = 1
        eingabe_phase = 0
    elif eingabe_phase==0 and level==1:
        if keyboard.A:
            eingabe_phase=1
            level=1
        if keyboard.B:
            level=2
            eingabe_phase=1

def on_key_down(key, unicode):
    global text, eingabe_phase, level,text2,cipher
    if key == keys.BACKSPACE and eingabe_phase==1:
        text = text[:-1]
    elif key == keys.BACKSPACE and eingabe_phase==2:
        text2 = text2[:-1]
    elif key == keys.RETURN:
        if eingabe_phase==0:
            eingabe_phase=1
        elif eingabe_phase== 1:
            eingabe_phase=2
        elif eingabe_phase == 2:
            eingabe_phase=3
            if level==1:
                cipher=otp_encrypt(text,text2)
            if level==2:
                cipher=otp_decrypt(text,text2)
        elif eingabe_phase>2:
            level=-1
    if eingabe_phase==3 and len(text)!=len(text2) and level==1:
        eingabe_phase=4
    elif unicode:
        if eingabe_phase==1:
            text += unicode
        if eingabe_phase==2:
            text2 += unicode

print(cipher)

pgzrun.go()
