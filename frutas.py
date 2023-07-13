import pygame
from config import *
from auxiliar import obtener_rectangulos, reescalar_imagen

class Frutas(pygame.sprite.Sprite):
    def __init__(self, tamaño: tuple,animaciones,posicion_inicial:tuple):
        super().__init__()
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #animaciones
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.contador_animacion = 0
        self.que_hace = "iddle"
        #rectangulo
        rectangulo = self.animaciones["iddle"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        self.puntos = 10
        
    def reescalar_animaciones(self):
        for clave in self.animaciones : 
            reescalar_imagen(self.animaciones[clave],(self.ancho,self.alto))

    def animar(self,pantalla,que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_animacion>=largo:
            self.contador_animacion = 0

        pantalla.blit(animacion[self.contador_animacion],self.lados ["main"])
        self.contador_animacion += 1
    
    def update(self, pantalla):
        self.animar(pantalla, "iddle")
        
       
   