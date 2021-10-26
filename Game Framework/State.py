import pygame
import GameObject
import Objects
import game
import math
import random
import Text

class State: #REGION: State defination


    def __init__(self, state_manager):
        self.state_manager = state_manager

    def processInput(self, event):
        pass

    def update(self):
        pass

    def render(self, surf):
        pass



class Play_Menu_State(State):

    game_score = 0

    def __init__(self, state_manager):
        super().__init__(state_manager)
        self.object_manager = GameObject.Object_Manager()

        #Values 
        self.angle = 0.0
        self.red = 0
        self.spawnRate = 1.3
        self.timer = 0
        Play_Menu_State.game_score = 0

        #Text
        self.score_text = Text.Text_Render(game.Game.GAME_FONT) #Text for the score
        self.game_over_text = Text.Text_Render(game.Game.GAME_FONT) #Game over text

        #Booleans
        self.is_game_over = False
        self.is_menu = True
        self.should_increment = True

        #Sprites
        self.game_over_sprite = GameObject.Sprite_Object(60, -64, game.Game.GAME_OVER_IMAGE)
        self.game_over_sprite.width = 336
        self.game_over_sprite.height = 64


        #music initializationn
        pygame.mixer.init()
        pygame.mixer.music.load((r'C:\Users\Oswell\Desktop\Python Projects\Game Framework\Assets\Chill.mp3'))
        pygame.mixer.music.play(-1)


        self.sfx = pygame.mixer.Sound((r'C:\Users\Oswell\Desktop\Python Projects\Game Framework\Assets\right block.wav'))

    
        



        #create two player objects
        for i in range(0, 2):
            self.object_manager.create_object(
                Objects.Player((game.Game.WIDTH  / 2) +  math.cos(math.radians(self.angle)) * 128,
                (game.Game.HEIGHT / 2) +  math.sin(math.radians(self.angle)) * 128,
                "Player", i, self.object_manager)
                
            )
            self.angle += 180.0



    def processInput(self, event):
        self.object_manager.processInput(event)
        if(event.type == game.Game.PLAYER_HIT_PLATFORM):
            self.is_game_over = True
        

        if(self.is_game_over):
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                     self.state_manager.set_state(Menu(self.state_manager))
                     pygame.mixer.music.fadeout(500)
                     self.sfx.play(0)
                
                    


    def update(self):
        self.handle_gameplay_logic()
       



    def render(self, surf):

        surf.fill((int(self.red), 0, 255))
        pygame.draw.circle(surf, (255, 0, int(self.red)), (game.Game.WIDTH  / 2, game.Game.HEIGHT/2) , 64)
        self.object_manager.render(surf)
       

        #Render text on the screen for score
        if(not self.is_game_over): 
            self.score_text.draw_text(surf, str(Play_Menu_State.game_score), 
            game.Game.WIDTH/ 2 - 16, 32, (255, 255, 255))

        #Draw the black transparent BG
        if(self.is_game_over):
            self.draw_transparent_bg(surf)
            if(Play_Menu_State.game_score > Menu.hi_score):
                Menu.hi_score = Play_Menu_State.game_score



    

       
                

    def lerp(self, min, max, pos):# for linear interpolation
        return min + (max - min) * pos

    def spawnPlatforms(self):

        self.timer += 1

        if(self.timer >= 60 * self.spawnRate):
            self.timer = 0
            self.object_manager.create_object(Objects.Platform(
                random.randint(0,  game.Game.WIDTH - 128),  -64, "Platform")
            )
        
        #Remove the platforms when they are outside the view
        for object in self.object_manager.game_objects:
            if(object.y >=  game.Game.HEIGHT + 32):
                self.object_manager.destroy_object(object)

    #Handle logic during gameplay    
    def handle_gameplay_logic(self):

        if(not self.is_game_over):

            self.object_manager.update()
            
            if(self.should_increment):
                self.red += 0.5
            else:
                self.red -= 0.5

            if(self.red >= 255 or self.red <= 0):
                self.should_increment = not self.should_increment

            #Spawn the platforms
            self.spawnPlatforms()
        else:
            pygame.mixer.music.set_volume(0.07)
        

                    

    #Draw transparent background 
    def draw_transparent_bg(self, surf):
        s = pygame.Surface((game.Game.WIDTH,  game.Game.HEIGHT))
        s.set_alpha(128)
        surf.blit(s, (0, 0))

        #Draw game over sprite and display player's score
        self.game_over_sprite.draw(surf, game.Game.WIDTH/2 - self.game_over_sprite.width/2, 113)
        self.game_over_text.draw_text(surf, "Your Score", game.Game.WIDTH / 2 - 80,  245, (255, 255, 0))
        self.game_over_text.draw_text(surf, str(Play_Menu_State.game_score), game.Game.WIDTH / 2 - 16,  300, (255, 255, 255))
        self.game_over_text.draw_text(surf, "Press the space key", game.Game.WIDTH / 2 - 170,  game.Game.HEIGHT - 96, (255, 255, 255))



class Menu(State):#Defination for the menu state

    hi_score = 0
    def __init__(self, state_manager):
        super().__init__(state_manager)

        self.title_sprite = GameObject.Sprite_Object(118, -64, game.Game.TITLE_IMAGE)
        self.title_sprite.width = 168
        self.title_sprite.height = 64
        self.red = 0
        self.blue = 0
        self.green = 0
        self.play_caption = Text.Text_Render(game.Game.GAME_FONT) #Text for play caption



    def processInput(self, event):
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                self.state_manager.set_state(Play_Menu_State(self.state_manager))
                


    def update(self):
        self.red += 1
        self.green += 2
        self.blue += 3


        if(self.red >= 255):
            self.red = 0

        if(self.green >= 255):
            self.green = 0

        if(self.blue >= 255):
            self.blue = 0

        

         

    def render(self, surf):
         surf.fill((int(self.red), int(self.green), int(self.blue)))
         self.title_sprite.draw(surf, 
         game.Game.WIDTH/2 - self.title_sprite.width/2, 64 )
         self.play_caption.draw_text(surf, "Press the space key", game.Game.WIDTH / 2 - 170,  game.Game.HEIGHT - 96, (255, 255, 255))
         self.play_caption.draw_text(surf, "Hi-Score " + str(Menu.hi_score), game.Game.WIDTH / 2 - 82,  20, (255, 255, 0))