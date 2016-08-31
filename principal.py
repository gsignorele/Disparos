import pygame

import constantes
from jugador import Player
from enemigo import Enemy
from pared import Pared
from plataforma import Plataforma
from plataforma_movimiento import PlataformaConMovimiento
from bullet import Bullet 

""" Clase principal en el que se debe ejecutar el juego. """
pygame.init()

# Configuramos el alto y largo de la pantalla
size = [constantes.ANCHO_PANTALLA, constantes.ALTURA_PANTALLA]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Proyecto Video-Juegos")

#listas de sprites
lista_sprites_activos  = pygame.sprite.Group()
lista_sprites_enemigos = pygame.sprite.Group()
lista_enemigos_mortales = pygame.sprite.Group()
lista_balas = pygame.sprite.Group()

#Creamos un enemigo
enemigo_principal = Enemy("imagenes/pajaro.png")
enemigo_principal.rect.x = 300
enemigo_principal.rect.y = 200
lista_sprites_activos.add(enemigo_principal)
#lista_sprites_enemigos.add(enemigo_principal)
lista_enemigos_mortales.add(enemigo_principal)

enemigo_secundario = Enemy("imagenes/pajaro.png")
enemigo_secundario.rect.x = 420
enemigo_secundario.rect.y = 400
lista_sprites_activos.add(enemigo_secundario)
#lista_sprites_enemigos.add(enemigo_secundario)
lista_enemigos_mortales.add(enemigo_secundario)

#paredes
pared = Pared(250,0,10,450)
lista_sprites_activos.add(pared)
lista_sprites_enemigos.add(pared)

# Creamos al jugador con la imagen p1_walk.png
jugador_principal = Player("imagenes/p1_walk.png", lista_sprites_enemigos, lista_enemigos_mortales, lista_balas, lista_sprites_activos)
jugador_principal.rect.x = 0
jugador_principal.rect.y = constantes.ALTURA_PANTALLA - jugador_principal.rect.height
lista_sprites_activos.add(jugador_principal)

#plataformas  
GRASS_MIDDLE = (648, 648, 70, 40)
plataforma = Plataforma("imagenes/tiles_spritesheet.png", GRASS_MIDDLE)
plataforma.rect.x = 100 
plataforma.rect.y = 100
lista_sprites_activos.add(plataforma)
lista_sprites_enemigos.add(plataforma)


#plataforma con movimitnto  
GRASS_MIDDLE = (648, 648, 70, 40)
plataformaMov = PlataformaConMovimiento("imagenes/tiles_spritesheet.png", GRASS_MIDDLE, jugador_principal)
plataformaMov.rect.x = 600 
plataformaMov.rect.y = 400
lista_sprites_activos.add(plataformaMov)
lista_sprites_enemigos.add(plataformaMov)
plataformaMov.limite_izquierdo = 500
plataformaMov.limite_derecho = 660
# velocidad
plataformaMov.mover_x = -1          
           

STONE_MIDDLE = (576, 576, 70, 70)
plataformaMovOtro = PlataformaConMovimiento("imagenes/tiles_spritesheet.png", STONE_MIDDLE, jugador_principal)
plataformaMovOtro.rect.x = 100 
plataformaMovOtro.rect.y = 500
lista_sprites_activos.add(plataformaMovOtro)
lista_sprites_enemigos.add(plataformaMovOtro)
plataformaMovOtro.limite_inferior = 600
plataformaMovOtro.limite_superior = 450
# velocidad
plataformaMovOtro.mover_y = -1          


#Variable booleano que nos avisa cuando el usuario aprieta el botOn salir.
salir = False
clock = pygame.time.Clock()

# -------- Loop Princiapl -----------
while not salir:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            salir = True 

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_principal.retroceder()
            if evento.key == pygame.K_RIGHT:
                jugador_principal.avanzar()
            if evento.key == pygame.K_DOWN:
                jugador_principal.bajar()
            if evento.key == pygame.K_UP:
                jugador_principal.subir()
                
            if evento.key == pygame.K_SPACE:
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = jugador_principal.rect.x + jugador_principal.rect.width
                bullet.rect.y = jugador_principal.rect.y + 50
                # Add the bullet to the lists
                lista_sprites_activos.add(bullet)
                lista_balas.add(bullet)


        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                jugador_principal.parar()
            if evento.key == pygame.K_RIGHT:
                jugador_principal.parar()
            if evento.key == pygame.K_DOWN:
                jugador_principal.parar()
            if evento.key == pygame.K_UP:
                jugador_principal.parar()


    # Actualiza todo el jugador
    screen.fill(constantes.AZUL)
    lista_sprites_activos.update()
    
    # Para que el jugador no se vaya de los limites de la ventana 
    if jugador_principal.rect.x <= 0:
        jugador_principal.rect.x = 0    
    if jugador_principal.rect.y >= constantes.ALTURA_PANTALLA  - enemigo_principal.rect.height:        
        jugador_principal.rect.y = constantes.ALTURA_PANTALLA  - enemigo_principal.rect.height
    if jugador_principal.rect.x >= constantes.ANCHO_PANTALLA - enemigo_principal.rect.width:
        jugador_principal.rect.x = constantes.ANCHO_PANTALLA - enemigo_principal.rect.width    
    if jugador_principal.rect.y <= 0:        
        jugador_principal.rect.y = 0

    # TODO EL CODIGO PARA DIBUJAR DEBE IR DEBAJO DE ESTE COMENTARIO.
    lista_sprites_activos.draw(screen)   
    
    
    clock.tick(60)

    pygame.display.flip()

pygame.quit()

