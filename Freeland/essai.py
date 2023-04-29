import pygame
import pytmx
import pyscroll
from game import Game
pygame.init()

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()

from player import Player


class Game:

    def __init__(self):
        # creation de la fenetre du jeu, modification de sa taille, et titre
        #pouvoir mettre des elements a l'interieur grace au self egalement
        self.screen=pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Freeland")

        #chargement de la carte (tmx):
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        #generer un joueur
        self.player = Player()

        #dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)


    def run(self):
        #boucle du jeu
        running = True
        while running:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png')
        self.image = self.get_image(0,0)
        #position
        self.rect= self.image.get_rect()
    def get_image(self,x,y):
        #selectionner le personnage qu'on veut dans l'image
        image = pygame.Surface([32,32]).convert_alpha()
        image.blit(self.sprite_sheet,(0,0),(x,y,32,32))
        return image

from player import Player


class Game:

    def __init__(self):
        # creation de la fenetre du jeu, modification de sa taille, et titre
        #pouvoir mettre des elements a l'interieur grace au self egalement
        self.screen=pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Freeland")

        #chargement de la carte (tmx):
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        #generer un joueur
        self.player = Player()

        #dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)


    def run(self):
        #boucle du jeu
        running = True
        while running:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()