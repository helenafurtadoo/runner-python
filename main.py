import pygame 
pygame.init()


screen = pygame.display.set_mode((800, 400)) # criando display surfice 
pygame.display.set_caption("jogo do corredooooorr") # criando o nome do display surfice
clock = pygame.time.Clock()

sky_surface = pygame.image.load('grafico/ceu.png') 
ground_surface = pygame.image.load('grafico/chao.png')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    
    pygame.display.update()
    clock.tick(60)