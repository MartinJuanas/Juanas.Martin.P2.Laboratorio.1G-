import pygame
import sys
import random




from config import *
from auxiliar import *
from plataforma import *
from modo import *
from Personaje import *
from enemigo import *
from boss import *
from frutas import*
from nivel import *

from nivelUno import *
from nivelDos import *
from nivelTres import *


class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)


        #Fuentes
        self.font = pygame.font.Font("src\\fonts\kablamo.ttf",48)

        self.is_runnig = False

        #niveles
        self.nivel_actual = NivelTres(self.screen)

        self.reloj = pygame.time.Clock()
        
    


    def play(self):
        self.is_runing = True
        while self.is_runing:

            eventos=pygame.event.get()



            self.reloj.tick(FPS)
            self.handler_events()
           

            self.nivel_actual.update(eventos)
        


    def handler_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

