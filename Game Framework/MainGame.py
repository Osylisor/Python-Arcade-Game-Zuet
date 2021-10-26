import pygame
import game



pygame.init()
pygame.mixer.init()

main_game = game.Game()

SURF = pygame.display.set_mode((main_game.WIDTH, main_game.HEIGHT))
pygame.display.set_caption("My Game")




clock = pygame.time.Clock()
   
run = True
while(run):
    clock.tick(main_game.FPS)

    for event in pygame.event.get():

        if(event.type == pygame.QUIT):
                run = False

        main_game.proceesInput(event)
        
    main_game.update()
    main_game.render(SURF)
    pygame.display.update()



pygame.quit()
