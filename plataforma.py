import pygame

from funciones_spritesheet import SpriteSheet

class Plataforma(pygame.sprite.Sprite):
    """ Clase que define las caracteristicas de la plataforma del juego. """

    def __init__(self, ruta, sprite_sheet_data):
        """ Plataforma constructor."""
        pygame.sprite.Sprite.__init__(self)

        #sprite_sheet = SpriteSheet("imagenes/tiles_spritesheet.png")
        sprite_sheet = SpriteSheet(ruta)
        # Grab the image for this platform
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
