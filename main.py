import pygame 
pygame.init()

# DISPLAY SURFACE
screen = pygame.display.set_mode((800, 400)) # criando display surfice (janela de exibição)
pygame.display.set_caption("jogo do corredooooorr") # criando o nome do display surfice
clock = pygame.time.Clock()

# FONTE
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) 

# REGULAR SURFICES
sky_surface = pygame.image.load('grafico/ceu.png').convert() #.convert() otimiza o desempenho da img
ground_surface = pygame.image.load('grafico/chao.png').convert()
text_surface = test_font.render('Jogo do corredorrrrr', False, 'Purple') #AA desativado

# SNAIL SURFACE
snail_surface = pygame.image.load('grafico\snail\snail1.png').convert_alpha()  
snail_pos_x = 600


# PLAYER SURFACE
player_surface = pygame.image.load('grafico\player\player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))


running = True
while running:
    for event in pygame.event.get():
        # CHECANDO O DISPLAY SURFICE PARA PODER FECHAR 
        if event.type == pygame.QUIT:
            running = False
            
    # PRINTING THE SURFACES
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (200,50))
    snail_pos_x -= 4 # para andar para a esquerda + velocidade
    if snail_pos_x < -100: snail_pos_x = 800
    screen.blit(snail_surface, (snail_pos_x, 250))
    screen.blit(player_surface, player_rectangle)
   
    
    # ATUALIZANDO TUDO
    pygame.display.update()
    clock.tick(60)