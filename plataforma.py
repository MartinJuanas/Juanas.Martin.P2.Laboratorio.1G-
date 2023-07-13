import pygame
from config import *
from auxiliar import obtener_rectangulos

class Plataformas(pygame.sprite.Sprite):
    def __init__(self, imagen_path, posicion):
        super().__init__()
        self.imagen = pygame.image.load(imagen_path)
        self.rect = self.imagen.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        self.lados = obtener_rectangulos(self.rect)

        # Agregar rectángulos en la parte superior
        ancho_rect_superior = 10
        alto_rect_superior = 15



        self.rect_superior_izq = pygame.Rect(self.rect.left, self.rect.top - alto_rect_superior, ancho_rect_superior // 3, alto_rect_superior)
        self.rect_superior_der = pygame.Rect(self.rect.right - ancho_rect_superior // 3, self.rect.top - alto_rect_superior, ancho_rect_superior // 3, alto_rect_superior)



    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)

        # Dibujar los rectángulos de la parte superior (opcional)
        # pygame.draw.rect(pantalla, ROJO, self.rect_superior_izq)
        # pygame.draw.rect(pantalla, ROJO, self.rect_superior_der)
