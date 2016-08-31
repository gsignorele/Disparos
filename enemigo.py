import pygame
from funciones_spritesheet import SpriteSheet
import constantes

class Enemy(pygame.sprite.Sprite):
    mover_x = 0
    mover_y = 0
    
    def __init__(self, ruta):
        """ Plataforma constructor."""
        pygame.sprite.Sprite.__init__(self)        
        sprite_sheet = SpriteSheet(ruta)       
        
        self.image = sprite_sheet.obtener_imagen_enemigo(0, 0, 70, 80)        
        self.rect = self.image.get_rect()
    
    """    
    def update(self):      
      # Movimientos Izquierda/Derecha
      self.rect.x += self.mover_x     
      self.rect.y += self.mover_y
    """