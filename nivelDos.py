import pygame


from nivel import *
from config import *
from auxiliar import *
from plataforma import *
from modo import *
from Personaje import *
from enemigo import *
from boss import *
from frutas import*
from nivel import *



class NivelDos(Level):

    def __init__(self,pantalla:pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()
        

        self.screen = pygame.display.set_mode((W,H))
        self.fondo = pygame.image.load("src\images\Fondo\mapa2.png")
        self.fondo = pygame.transform.scale(self.fondo, (W,H))

        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
        diccionario_animaciones["camina"] = personaje_camina
        diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
        diccionario_animaciones["salta"] = personaje_salta
        diccionario_animaciones["salta_izquierda"] = personaje_salta_izquierda
        ##########

        #Diccionario Animaciones Enemigo
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["camina_derecha"] = enemigo_camina_derecha
        diccionario_animaciones_enemigo["camina_izquierda"] = enemigo_camina_izquierda




        #Diccionario animaciones Boss 
        diccionario_animaciones_boss = {}
        diccionario_animaciones_boss["camina_derecha"] = boss_camina_derecha
        diccionario_animaciones_boss["camina_izquierda"] = boss_camina_izquierda

        #Diccionario animaciones fruta
        diccionario_animaciones_fruta = {}
        diccionario_animaciones_fruta["iddle"] = fruta_iddle





        mi_personaje = Personaje(TAM_PJ,diccionario_animaciones,POS_INICIO_PJ,10)


        frutas = [Frutas((24,24),diccionario_animaciones_fruta,(340,320)),
                  Frutas((24,24),diccionario_animaciones_fruta,(250,320)),
                  Frutas((24,24),diccionario_animaciones_fruta,(390,150)),
                  Frutas((24,24),diccionario_animaciones_fruta,(850,320)),
                  Frutas((24,24),diccionario_animaciones_fruta,(900,320)),
                  Frutas((24,24),diccionario_animaciones_fruta,(192,320)),
                  Frutas((24,24),diccionario_animaciones_fruta,(150,70)),
                      ]
        
       

        bosses = []

        

        enemigos = []
        
    
        

        plataformas = [Plataformas("src\images\plataforma\Plataforma1.png", (0, 470)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (192, 470)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (384, 470)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (576, 470)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (768, 470)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (960, 470)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (192, 350)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (384, 200)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (576, 200)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (768, 350)),
                      Plataformas("src\images\plataforma\Plataforma1.png", (0, 100))
                      ]

        

        super().__init__(pantalla,mi_personaje,self.fondo,plataformas,frutas,enemigos,bosses)