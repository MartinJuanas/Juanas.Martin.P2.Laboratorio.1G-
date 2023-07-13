import pygame
import random
from config import *
from auxiliar import reescalar_imagen,obtener_rectangulos

from ataqueBosses import *

class Boss(pygame.sprite.Sprite):
    def __init__(self, tamaño: tuple,animaciones,posicion_inicial:tuple,velocidad,puntos):
        super().__init__()
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #animaciones
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.contador_pasos = 0
        self.que_hace = "camina_derecha"
        
        #rectangulo
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        self.velocidad = velocidad
        self.desplazamiento_hecho = 0
        # estadisticas y puntos
        self.puntos = puntos
        self.vida = 10
        #gravedad
        self.gravedad = True
        self.limite = True
        #RectangulosAtaque
        self.rectangulo_ataque = pygame.Rect(0, 0, 300, 30)
        self.rectangulo_ataque.x = self.lados["main"].right
        self.rectangulo_ataque.y = self.lados["main"].centery - (self.rectangulo_ataque.height // 2)


    def actualizar_lados(self):
        for lado in self.lados:
            self.lados[lado].x = self.lados["main"].x
            self.lados[lado].y = self.lados["main"].y


    def reescalar_animaciones(self):
        for clave in self.animaciones : 
            reescalar_imagen(self.animaciones[clave],(self.ancho,self.alto))

    def animar_boss(self,pantalla,que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos>=largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos],self.lados ["main"])
        self.contador_pasos += 1



    def update_vision_boss(self,que_hace):

        if que_hace == "camina_izquierda" :
            self.rectangulo_ataque.x = self.lados["main"].left - self.rectangulo_ataque.width
            self.rectangulo_ataque.y = self.lados["main"].centery - (self.rectangulo_ataque.height // 2)
        elif que_hace =="camina_derecha":
            self.rectangulo_ataque.x = self.lados["main"].right
            self.rectangulo_ataque.y = self.lados["main"].centery - (self.rectangulo_ataque.height // 2)
            
    
    def update_boss(self, pantalla):
        if self.que_hace == "camina_derecha":
            self.animar_boss(pantalla, "camina_derecha")
            self.mover_boss(self.velocidad)
            self.update_vision_boss(self.que_hace)
        elif self.que_hace == "camina_izquierda":
            self.animar_boss(pantalla, "camina_izquierda")
            self.mover_boss(self.velocidad)
            self.update_vision_boss(self.que_hace)

        #pygame.draw.rect(pantalla, (255, 0, 0), self.rectangulo_ataque)


    def mover_boss(self, velocidad):
        if self.gravedad:
            if self.lados["main"].bottom <= HEIGHT:
                self.lados["main"].y += velocidad
            else:
                self.gravedad = not self.gravedad
                self.velocidad_x = random.randrange(5, 15)
                self.velocidad_y = random.randrange(5, 15)
        else:
            if self.lados["main"].top >= 0:
                self.lados["main"].y -= velocidad
            else:
                self.gravedad = not self.gravedad
                self.velocidad_x = random.randrange(5, 15)
                self.velocidad_y = random.randrange(5, 15)

        if self.limite:
            if self.lados["main"].right <= WIDTH:
                self.lados["main"].x += velocidad
            else:
                self.limite = not self.limite
                self.velocidad_x = random.randrange(5, 15)
                self.velocidad_y = random.randrange(5, 15)
                self.que_hace = "camina_izquierda"
        else:
            if self.lados["main"].left >= 0:
                self.lados["main"].x -= velocidad
            else:
                self.limite = not self.limite
                self.velocidad_x = random.randrange(5, 15)
                self.velocidad_y = random.randrange(5, 15)
                self.que_hace = "camina_derecha"

        self.actualizar_lados()
                           