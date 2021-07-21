import pygame

#for importing images
from imgs import images


pygame.init()
# essential


# main function of the game:
def main():

    # run :
    run = True

    # background and screen :
    HEIGHT = 256
    WEIGHT = 512
    screen = pygame.display.set_mode((WEIGHT,HEIGHT))

    # clock and fps :
    clock = pygame.time.Clock()


    while run :

        # importing background image
        #screen.blit(images["background"],(0,0))

        # for quiting the game (essential) :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                quit()


        pygame.display.update()
        clock.tick(60)

main()

