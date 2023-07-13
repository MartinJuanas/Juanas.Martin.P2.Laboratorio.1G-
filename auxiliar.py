import pygame
import random


#######################

def girar_imagenes (lista_original,flip_x,flip_y):
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada



##########################

def reescalar_imagen(lista_imagenes,tamaño:tuple):

    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i],tamaño)
    


##########################


def obtener_rectangulos (principal)->dict:
    diccionario = {}
    
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left,principal.bottom-12,principal.width,12)
    diccionario["right"] = pygame.Rect(principal.right-4,principal.top,4,principal.height)
    diccionario["left"] = pygame.Rect(principal.left,principal.top, 4,principal.height)
    diccionario["top"] = pygame.Rect(principal.left,principal.top,principal.width,12)

    return diccionario


######################

personaje_quieto = [pygame.image.load("src\images\PersonajeJuego\Quieto\\0.png"),        
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\1.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\2.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\3.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\4.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\5.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\6.png"),
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\7.png"),
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\8.png"),
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\9.png"),
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\10.png"),
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\11.png"),
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\12.png"),
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\13.png"),
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\14.png"),
                    pygame.image.load("src\images\PersonajeJuego\Quieto\\15.png")
                    ]


personaje_camina = [pygame.image.load("src\images\PersonajeJuego\Caminar\\0.png"),        
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\1.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\2.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\3.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\4.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\5.png"), 
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\6.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\7.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\8.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\9.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\10.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\11.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\12.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\13.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\14.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\15.png"),
                    pygame.image.load("src\images\PersonajeJuego\Caminar\\16.png"),

                    ]


personaje_salta =[ pygame.image.load("src\images\PersonajeJuego\Saltar\\0.png")]



personaje_camina_izquierda = girar_imagenes(personaje_camina,True,False)

personaje_salta_izquierda = girar_imagenes(personaje_salta,True,False)

personaje_quieto_izquierda = girar_imagenes(personaje_quieto,True,False)

#################################################################################### sprites enemigo

enemigo_camina_izquierda = [pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\0.png"),        
                    pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\1.png"), 
                    pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\2.png"), 
                    pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\3.png"), 
                    pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\4.png"), 
                    pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\5.png"), 
                    pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\6.png"),
                    pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\7.png"),
                    pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\8.png"),
                    pygame.image.load("src\images\Enemigos\\fantasma\camina_izquierda_fantasma\\9.png"),
                    ]

enemigo_camina_derecha= girar_imagenes(enemigo_camina_izquierda,True,False)

####################################################################################### sprites boss
boss_camina_izquierda = [pygame.image.load("src\images\Enemigos\\boss\\0.png"),        
                    pygame.image.load("src\images\Enemigos\\boss\\1.png"), 
                    pygame.image.load("src\images\Enemigos\\boss\\2.png"), 
                    pygame.image.load("src\images\Enemigos\\boss\\3.png"), 
                    pygame.image.load("src\images\Enemigos\\boss\\4.png"), 
                    ]

boss_camina_derecha = girar_imagenes(boss_camina_izquierda,True,False)

########################################################################################### sprites Frutas


fruta_iddle  = [pygame.image.load("src\images\Frutas\\0.png"),
                pygame.image.load("src\images\Frutas\\1.png"),
                pygame.image.load("src\images\Frutas\\2.png"),
                pygame.image.load("src\images\Frutas\\3.png"),
                pygame.image.load("src\images\Frutas\\4.png"),
                pygame.image.load("src\images\Frutas\\5.png"),
                pygame.image.load("src\images\Frutas\\6.png"),
                pygame.image.load("src\images\Frutas\\7.png"),
                pygame.image.load("src\images\Frutas\\8.png"),
                pygame.image.load("src\images\Frutas\\9.png"),
                pygame.image.load("src\images\Frutas\\10.png"),
                pygame.image.load("src\images\Frutas\\11.png"),
                pygame.image.load("src\images\Frutas\\12.png"),
                pygame.image.load("src\images\Frutas\\13.png"),
                pygame.image.load("src\images\Frutas\\14.png"),
                pygame.image.load("src\images\Frutas\\15.png"),
                pygame.image.load("src\images\Frutas\\16.png")]


################################################################################################################sprite ataque boss


ataque_boss_iddle = [pygame.image.load("src\images\Enemigos\\boss\\ataque1\\0.png"),
                     pygame.image.load("src\images\Enemigos\\boss\\ataque1\\1.png"),
                     pygame.image.load("src\images\Enemigos\\boss\\ataque1\\2.png"),
                     pygame.image.load("src\images\Enemigos\\boss\\ataque1\\3.png"),
                     pygame.image.load("src\images\Enemigos\\boss\\ataque1\\4.png"),
                     pygame.image.load("src\images\Enemigos\\boss\\ataque1\\5.png")]

