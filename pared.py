import pygame
import constantes

class Pared (pygame.sprite.Sprite):
    mover_x = 0
    mover_y = 0
    
    def __init__(self, x, y, largo, alto):
        """ Constructor para la pared con la que el protagonista puede encontrarse """
        #  Llama al constructor padre
        pygame.sprite.Sprite.__init__(self)
         
        self.image = pygame.Surface([largo, alto])
        self.image.fill(constantes.BLANCO)
 
        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x