import pygame

class Player(pygame.sprite.DirtySprite):
    def __init__(self,width,height,pos,*group):
        super().__init__(*group)
        self.image = pygame.Surface((width,height))
        self.rect = self.image.get_rect(center = pos)
        self._layer = 0

class Game():
    def __init__(self):
        self.done = False
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((640,480))

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player1 = Player(150,150,(150,100),self.all_sprites)
        self.player1.image.fill((0,0,255))
        self.player1._layer = 3


        self.player2 = Player(100,100,(150,100),self.all_sprites)
        self.player2.image.fill((0,255,0))
        self.player2._layer = 2


        self.player3 = Player(50,50,(150,100),self.all_sprites)
        self.player3.image.fill((255,0,0))
        self.player3._layer = 1

    def mouse_event(self):
        if pygame.event.get(pygame.QUIT):
            self.done = True

    def draw(self):
        self.screen.fill((255,255,255))
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def run(self):
        while not self.done:
            self.clock.tick(self.fps)
            self.draw()
            self.mouse_event()


if __name__=='__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()