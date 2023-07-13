import pygame
import random

from config import *
from modo import *
from ataqueBosses import*


#Diccionario animaciones ataque boss
diccionario_animaciones_ataque_boss = {}
diccionario_animaciones_ataque_boss["iddle"] = ataque_boss_iddle





class Level:
    def __init__(self,pantalla,personaje_principal,imagen_fondo,lista_plataformas,lista_frutas,lista_enemigos=None,lista_bosses=None):
        self._slave = pantalla      

        self.personaje = personaje_principal
        self.plataformas = lista_plataformas
        self.fondo= imagen_fondo
        self.frutas = lista_frutas
        self.enemigos = lista_enemigos
        self.bosses = lista_bosses

        self.sprites = pygame.sprite.Group()
        self.ataques_boss = pygame.sprite.Group()


    def generar_ataque_boss (self):
        if len(self.ataques_boss) == 0 :
            for i in range(MAX_PROYECTILES):
                x = random.randrange(16,WIDTH-16)
                y =  random.randrange(-1000,100)
                ataque_boss = AtaqueBosses(diccionario_animaciones_ataque_boss,(32,64),(x,y),5)
                self.ataques_boss.add(ataque_boss)
                self.sprites.add(ataque_boss)  
                print("Colisionando con a vision del boss")


    def kill_elementos_fuera_de_pantalla(self):
        for ataque in self.ataques_boss:
            if ataque.lados["top"].top >= HEIGHT:
                ataque.kill()




    def update (self,lista_eventos):
        for evento in lista_eventos :
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
                cambiar_modo()
        

        self.kill_elementos_fuera_de_pantalla()
        self.leer_inputs()
        self.actualizar_pantalla()
        self.handler_colisiones()


    def leer_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.personaje.que_hace = "derecha"
        elif keys[pygame.K_LEFT]:
            self.personaje.que_hace = "izquierda"
            self.salta_izquierda = True
        elif keys[pygame.K_UP] :
            self.personaje.que_hace = "salta"
        else:
            self.personaje.que_hace = "quieto"


    def dibujar_rectangulos(self):

        if get_modo()==True:

            for lado in self.personaje.lados:
                pygame.draw.rect(self._slave,ROJO,self.personaje[lado],2)
            
            for plataforma in self.plataformas:
                for lado in plataforma.lados :
                    pygame.draw.rect(self._slave,ROJO,self.plataforma.lados[lado],2 )
            


    def actualizar_pantalla(self):
            

        self._slave.blit(self.fondo, (0, 0))
            
        self.personaje.update(self._slave,self.plataformas)
            

        for plataforma in self.plataformas:
            plataforma.dibujar(self._slave)

        for enemigo in self.enemigos:
            enemigo.update(self._slave)

        for boss in self.bosses:
            boss.update_boss(self._slave)

        for fruta in self.frutas : 
            fruta.update(self._slave)

        for ataque in self.ataques_boss:
            ataque.update(self._slave)

        pygame.display.flip()



    def handler_colisiones(self):
        for enemigo in self.enemigos:
            if self.personaje.lados["main"].colliderect(enemigo.lados["main"]):
                self.personaje.vida -= 1
                print(f"La vida que le queda a player es de: {self.personaje.vida}")

            if self.personaje.lados["bottom"].colliderect(enemigo.lados["top"]):
                self.enemigos.remove(enemigo)
                self.personaje.puntos += enemigo.puntos
                self.personaje.desplazamiento_y = 0
                print(f"Los puntos que te quedan son: {self.personaje.puntos}")
                
        for boss in self.bosses:
            if self.personaje.lados["main"].colliderect(boss.lados["main"]):
                self.personaje.vida -= 2
                print(f"La vida que le queda a player es de: {self.personaje.vida}")

            if self.personaje.lados["bottom"].colliderect(boss.lados["top"]):
                boss.vida -=1
                self.personaje.puntos += boss.puntos
                self.personaje.desplazamiento_y = 0
                print("Boss tocado")
                print(f"puntos del boss: {boss.vida}")

                if boss.vida < 1:
                    self.bosses.remove(boss)
                    print("boss muerto")

            if self.personaje.lados["main"].colliderect(boss.rectangulo_ataque):
                self.generar_ataque_boss()

        for fruta in self.frutas:
            if self.personaje.lados["main"].colliderect(fruta.lados["main"]):
                self.frutas.remove(fruta)
                self.personaje.puntos += fruta.puntos
                print(f"Los puntos que te quedan son: {self.personaje.puntos}")


        for ataque in self.ataques_boss:
            if self.personaje.lados["main"].colliderect(ataque.lados["main"]):
                self.personaje.vida -= 2
                print(f"La vida que le queda a player es de: {self.personaje.vida}")
        
    



        #self.still_alive(self.personaje)