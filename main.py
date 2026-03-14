import pygame 
pygame.init()


screen = pygame.display.set_mode((800, 400)) # criando display surfice 
pygame.display.set_caption("jogo do corredooooorr") # criando o nome do display surfice
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200)) # criando uma superfici teste para treinar coordenas em BLIT 
test_surface.fill('Red')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    screen.blit(test_surface, (200,100))
    
    pygame.display.update()
    clock.tick(60)