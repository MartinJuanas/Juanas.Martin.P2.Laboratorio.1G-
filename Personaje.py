import pygame

from config import *
from auxiliar import reescalar_imagen,obtener_rectangulos

class Personaje(pygame.sprite.Sprite):
    def __init__(self, tamaño: tuple,animaciones,posicion_inicial:tuple,velocidad):
        super().__init__()

        
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #gravedad
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.saltos_realizados = 0
        #animaciones
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.bandera_izquierda = False
        #rectangulo
        self.rectangulo = self.animaciones["quieto"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        self.velocidad = velocidad
        #Vida y puntos
        self.vida = 10
        self.puntos = 0

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

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

        
      

    def update(self,pantalla,plataformas):

        match self.que_hace : 
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla,"camina")
                    self.que_hace = "camina"
                    self.bandera_izquierda = False
                self.mover(self.velocidad)

            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla,"camina_izquierda")
                    self.que_hace = "camina_izquierda"
                    self.bandera_izquierda = True
                self.mover(self.velocidad * -1)

            case "salta":
                    if self.saltos_realizados <2 :
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto
                        self.saltos_realizados += 1
                    
            case "quieto":
                if not self.esta_saltando :
                   if self.bandera_izquierda:
                        self.animar(pantalla, "quieto_izquierda")
                   else : 
                       self.animar (pantalla,"quieto")

        self.aplicar_gravedad(pantalla,plataformas) 

    def aplicar_gravedad(self, pantalla, plataformas):
        if self.esta_saltando:
            self.animar(pantalla, "salta")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        for plataforma in plataformas : 
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):  # Verificar la colisión con el rectángulo del piso
                    self.desplazamiento_y = 0
                    self.saltos_realizados = 0
                    self.esta_saltando = False
                    self.lados["main"].bottom = plataforma.lados["main"].top -1
                    break
            elif self.lados["top"].colliderect(plataforma.lados["bottom"]):
                    self.aplicar_gravedad(pantalla,plataformas)
                    break
            elif self.lados["right"].colliderect(plataforma.lados["left"]):
                self.mover(0)
                break
        else:
            self.esta_saltando = True
        




                        

                
            