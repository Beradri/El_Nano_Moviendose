import pygame
 
pygame.init()
largo=800;
alto=500
screen = pygame.display.set_mode( (largo, alto) )
imagencita1 = pygame.image.load("supernano.png").convert()

posAlto = 300
posLargo = -300

 


pygame.display.flip() 

 
running = True
while (posLargo<300):
    screen.blit(imagencita1 ,  ( posAlto, posLargo))
    pygame.display.flip() 
    posLargo = posLargo + 0.5
    print(posLargo)       
pygame.quit()


