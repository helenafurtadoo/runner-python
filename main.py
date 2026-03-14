import pygame 
pygame.init()


screen = pygame.display.set_mode((800, 400)) # criando display surfice 
pygame.display.set_caption("jogo do corredooooorr") # criando o nome do display surfice
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('grafico/ceu.png') 
ground_surface = pygame.image.load('grafico/chao.png')
text_surface = test_font.render('testando o texto', False, 'Black') #AA desativado

snail_surface = pygame.image.load('grafico\snail\snail1.png')
snail_pos_x = 600

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300,50))
    snail_pos_x -= 4 # para andar para a esquerda + velocidade
    if snail_pos_x < -100: snail_pos_x = 800
    screen.blit(snail_surface, (snail_pos_x, 250))
   
    
    pygame.display.update()
    clock.tick(60)