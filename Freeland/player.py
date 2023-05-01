import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0])

        #position
        self.rect= self.image.get_rect()
        self.position = [x, y]
        self.image ={
            'down': self.get_image(0,0),
            'left': self.get_image(0,33.25),
            'right':self.get_image(0,66.50),
            'up':self.get_image(0,99.75)
        }
        self.speed = 2

    def change_animation(self,name):
        self.image = self.images[name]
        self.image.set_colorkey((0,0,0))


    def move_right(self): self.position[0]+= self.speed
    def move_left(self): self.position[0]-=self.speed
    def move_up(self): self.position[1]-=self.speed
    def move_down(self):self.position[1] +=self.speed



    def update(self):
        self.rect.topleft = self.position
    def get_image(self,x,y):
        #selectionner le personnage qu'on veut dans l'image
        image = pygame.Surface([32,32]).convert_alpha()
        image.blit(self.sprite_sheet,(0,0),(x,y,32,32))
        return image