
import pygame


class Game_Object: #Game object defination

    def __init__(self, x, y, tag):
        self.x = x
        self.y = y
        self.tag = tag
        self.hit_box = pygame.Rect(x, y, 32, 32)

    def processInput(self, event):
        pass


    def update(self):
        pass

    def render(self, surf):
        pass


class Object_Manager:#Managing game object

    def __init__(self):
        self.game_objects = []

    def processInput(self, event):
        for object in self.game_objects:
            object.processInput(event)


    def update(self):
        for object in self.game_objects:
            object.update()

    def render(self, surf):
        for object in self.game_objects:
            object.render(surf)

    def create_object(self, object):
        self.game_objects.append(object)
    
    def destroy_object(self, object):
        self.game_objects.remove(object)


class Sprite_Object: #Sprite defination 

    def __init__(self, x,  y, image):

        self.x = x
        self.y = y
        self.angle = 0.0
        self.width = 32
        self.height = 32
        self.image = image
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.originX = 0
        self.originY = 0
        


    
    def set_origin(self, o_x,  o_y):
        self.originX = o_x
        self.originY = o_y


    def draw(self, surf, x,  y):

        #transform the image
        scaled_image = pygame.transform.scale(self.image, (self.width,  self.height))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        final_Image = rotated_image


        #update the position 
        self.x = x
        self.y = y
        surf.blit(final_Image, (self.x,  self.y))

        #bounding box position
        self.hit_box.x = self.x
        self.hit_box.x = self.y



    def get_sprite_sheet(self, x, y, width, height):
        
        surf = pygame.Surface((width, height))
        rect = pygame.Rect(x, y, width, height)
        surf.blit(self.image, (0, 0), rect)
        return surf


    def draw_with_cam(self, surf, x,  y, camera):

        #transform the image
        scaled_image = pygame.transform.scale(self.image, (self.width,  self.height))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        final_Image = rotated_image

        final_Image.set_colorkey((0 , 0, 0))

        #update the position 
        self.x = x
        self.y = y
        surf.blit(final_Image, (self.x - camera.x,  self.y - camera.y))

        #bounding box position
        self.hit_box.x = self.x
        self.hit_box.x = self.y