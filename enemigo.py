import pygame
import math

from config import *
from auxiliar import reescalar_imagen,obtener_rectangulos

class Enemigo(pygame.sprite.Sprite):
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
        #vida y puntos
        self.puntos = puntos



    def reescalar_animaciones(self):
        for clave in self.animaciones : 
            reescalar_imagen(self.animaciones[clave],(self.ancho,self.alto))

    def animar(self,pantalla,que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos>=largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos],self.lados ["main"])
        self.contador_pasos += 1
    
    def update(self, pantalla):
        if self.que_hace == "camina_derecha":
            self.animar(pantalla, "camina_derecha")
            self.mover(self.velocidad)
        elif self.que_hace == "camina_izquierda":
            self.animar(pantalla, "camina_izquierda")
            self.mover(self.velocidad)

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
            self.desplazamiento_hecho += abs(velocidad)  # Usar valor absoluto para contar el desplazamiento

        if self.desplazamiento_hecho > 700:
            self.velocidad *= -1
            self.desplazamiento_hecho = 0

        if self.velocidad > 0:
            self.que_hace = "camina_derecha"
        else:
            self.que_hace = "camina_izquierda"
                
   