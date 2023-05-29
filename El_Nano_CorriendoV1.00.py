import pygame
import time
import random
 
pygame.init()
largo=800;
alto=500
screen = pygame.display.set_mode( (largo, alto) )
ElNano = pygame.image.load("supernano.png").convert_alpha()
Verstappen = pygame.image.load("Verstappen.png").convert_alpha()
Hamilton = pygame.image.load("hamilton.png").convert_alpha()
Background = pygame.image.load("pista.png").convert()
first = pygame.image.load("1.png").convert()
second = pygame.image.load("2.png").convert()
third = pygame.image.load("3.png").convert()

posAlto = 300
posLargo = -300
posLargo2 = -300
posLargo3 = -300
sum1 = 0.76

sum1 = random.uniform(0.5, 2.0)
sum2 = random.uniform(0.5, 2.0)
sum3 = random.uniform(0.5, 2.0)
Pos1 = 0
Pos2 = 0
Pos3 = 0

Funcionando = True


pygame.display.flip() 


 
running = True
while Funcionando:
    screen.blit(Background ,  ( 0, 0))
    screen.blit(ElNano ,  ( posAlto, posLargo))
    screen.blit(Verstappen ,  ( posAlto-160, posLargo2))
    screen.blit(Hamilton ,  ( posAlto+175, posLargo3))
    pygame.display.flip() 
    posLargo = posLargo + sum1
    posLargo2 = posLargo2 + sum2
    posLargo3 = posLargo3 + sum3
    print(posLargo) 
    if (posLargo>300 and posLargo2<300 and posLargo3<300):
        pos1 = 1
    if (posLargo2>300 and posLargo<300 and posLargo3<300):
        pos2 = 1
    if (posLargo3>300 and posLargo2<300 and posLargo<300):
        pos1 = 1
    if (posLargo>300 and posLargo2>300 and posLargo3>300):
        Funcionando = False      
if (pos1=1):
    screen.blit(first ,  ( 370, 50))
pygame.display.flip()
time.sleep(2)
pygame.quit()


#1º - Hacer que los coches sean más pequeños
#2º - arreglar y terminar marcador


