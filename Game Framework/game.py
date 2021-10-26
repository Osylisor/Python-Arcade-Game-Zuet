import pygame
import StateManager
import State

class Game:

    WIDTH, HEIGHT = 416, 672
    FPS = 60

    pygame.font.init()


    #Load assests here
    PLAYER_IMAGE_RED = pygame.image.load((r'C:\Users\Oswell\Desktop\Python Projects\Game Framework\Assets\Ball Player Red.png'))
    PLAYER_IMAGE_BLUE = pygame.image.load((r'C:\Users\Oswell\Desktop\Python Projects\Game Framework\Assets\Ball Player Blue.png'))
    PLATFORM_IMAGE = pygame.image.load((r'C:\Users\Oswell\Desktop\Python Projects\Game Framework\Assets\Platform.png'))
    TITLE_IMAGE = pygame.image.load((r'C:\Users\Oswell\Desktop\Python Projects\Game Framework\Assets\Title.png'))
    GAME_OVER_IMAGE = pygame.image.load((r'C:\Users\Oswell\Desktop\Python Projects\Game Framework\Assets\Game Over.png'))


    #Loading font
    GAME_FONT = pygame.font.SysFont('cosmicsans', 52)


    #Uner defined event for colliding with platforms 
    PLAYER_HIT_PLATFORM = pygame.USEREVENT + 1


    def __init__(self):
      
        self.state_manger = StateManager.Stage_Manger()

        self.state_manger.set_state(State.Menu(self.state_manger))
        print("Game has been initialized!")


    def proceesInput(self, event):
        self.state_manger.processInput(event)

                

    def update(self):
        self.state_manger.update()


    def render(self, surf):
        self.state_manger.render(surf)


    def quit(self):
        pygame.quit()

    def get_width(cls):
        return cls.WIDTH

    def get_height(cls):
        return cls.HEIGHT