import random
import pygame
from pygame.rect import Rect
import GameObject
import math
import State
import game


class Player(GameObject.Game_Object): #Player Object
    
    def __init__(self, x, y, tag, index, object_manger):
        super().__init__(x, y, tag)
        self.index = index
        self.angle = 0
        self.angular_vel = 5.0
        self.timer = 0
        self.object_manger = object_manger
        self.hit_box = Rect(x, y, 32, 32)

        if(self.index == 0):
            self.angle = 0
            self.sprite = GameObject.Sprite_Object(self.x, self.y, game.Game.PLAYER_IMAGE_RED)
        elif(self.index == 1):
            self.angle = 180
            self.sprite = GameObject.Sprite_Object(self.x, self.y, game.Game.PLAYER_IMAGE_BLUE)
    


    def update(self):
        
        key_pressed = pygame.key.get_pressed()

        if(key_pressed[pygame.K_RIGHT]):
            self.angle += self.angular_vel
            self.increment_score()
        if(key_pressed[pygame.K_LEFT]):
            self.angle -= self.angular_vel
            self.increment_score()

        #Set the position of the player
        self.x = (game.Game.WIDTH  / 2 - 16) +  math.cos(math.radians(self.angle)) * 128
        self.y = (game.Game.HEIGHT / 2) +  math.sin(math.radians(self.angle)) * 128
        self.hit_box.x = self.x
        self.hit_box.y = self.y


        self.check_collision()

        
            
        

    def render(self, surf):
        self.sprite.image = self.sprite.get_sprite_sheet(0, 0, 32, 32)
        self.sprite.image.set_colorkey((0 ,0 , 0))
        self.sprite.draw(surf, self.x,  self.y)

    def increment_score(self):
        self.timer += 1

        if(self.timer >= 60 * 0.06):
            self.timer = 0
            State.Play_Menu_State.game_score += 1
    
    def check_collision(self):
        for object in self.object_manger.game_objects:
            if(object.tag == "Platform"):
                if self.hit_box.colliderect(object.hit_box):
                    pygame.event.post(pygame.event.Event(game.Game.PLAYER_HIT_PLATFORM))
                    


    


class Platform(GameObject.Game_Object):#Platform defination
    
    def __init__(self, x, y, tag):
        super().__init__(x, y, tag)
        self.sprite = GameObject.Sprite_Object(self.x, self.y, game.Game.PLATFORM_IMAGE)
        self.vel_y  = 3
        self.sprite.width = random.randint(64, 128)
        self.hit_box = pygame.Rect(self.x, self.y, self.sprite.width, 32)
        self.hit_box.width = self.sprite.width

    def update(self):
        
        self.y += self.vel_y
        self.hit_box.x = self.x
        self.hit_box.y = self.y

    def render(self, surf):
        self.sprite.image = self.sprite.get_sprite_sheet(0, 0,  32, 32)
        self.sprite.image.set_colorkey((0, 0, 0))
        self.sprite.draw(surf, self.x,  self.y)
