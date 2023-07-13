from typing import Any
from auxiliar import *
import pygame


class AtaqueBosses(pygame.sprite.Sprite):
    def __init__(self, animaciones, tamaño: tuple,posicion_spawn:tuple,speed:int = 10):
        super().__init__()


        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        #movimiento
        self.speed_y = speed
        self.aceleracion = 1.2
        #animacion ? 
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.contador_animacion = 0
        self.que_hace = "iddle"
         #rectangulo
        rectangulo = self.animaciones["iddle"][0].get_rect()
        rectangulo.x = posicion_spawn[0]
        rectangulo.y = posicion_spawn[1]
        self.lados = obtener_rectangulos(rectangulo)
       

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].y += velocidad   
    

    def update(self,pantalla) :
        self.aceleracion += 0.
        self.mover(self.speed_y*self.aceleracion)
        self.animar(pantalla, "iddle")
        
   
    def stop(self):
        self.speed_y = 0

    def reescalar_animaciones(self):
        for clave in self.animaciones : 
            reescalar_imagen(self.animaciones[clave],(self.ancho,self.alto))

    def animar(self,pantalla,que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_animacion>=largo:
            self.contador_animacion = 0

        pantalla.blit(animacion[self.contador_animacion],self.lados["main"])
        self.contador_animacion += 1
    
   


    
    