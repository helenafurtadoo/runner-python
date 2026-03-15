import pygame 
pygame.init()

# DISPLAY SURFACE
screen = pygame.display.set_mode((800, 400)) # criando display surfice (janela de exibição)
pygame.display.set_caption("Runner game") # criando o nome do display surfice
clock = pygame.time.Clock()

# FONTE
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) 

# REGULAR SURFICES
sky_surface = pygame.image.load('grafico/ceu.png').convert() #.convert() otimiza o desempenho da img
ground_surface = pygame.image.load('grafico/chao.png').convert()

# SCORE
score_surface = test_font.render('Runner game', False,(64,64,64)) #AA desativado
score_rectangle = score_surface.get_rect(center = (400, 50))

# SNAIL SURFACE
snail_surface = pygame.image.load('grafico\snail\snail1.png').convert_alpha()  
snail_rectangle = snail_surface.get_rect(bottomright = (600, 300))

# PLAYER SURFACE
player_surface = pygame.image.load('grafico\player\player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))



running = True
while running:
    for event in pygame.event.get():
        # CHECANDO O DISPLAY SURFICE PARA PODER FECHAR 
        if event.type == pygame.QUIT:
            running = False
            
        # CHECANDO MOVIMENTOS DO MOUSE
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos): print('colisao')

            
    # PRINTING THE SURFACES
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rectangle,border_radius = 10)
    screen.blit(score_surface, score_rectangle)

    snail_rectangle.x-= 4
    if snail_rectangle.right <= 0: snail_rectangle.left = 800 # se a parte direita retangulo da lesma for <= 0 (), "renascer" a lesma no 800 (mais esquerda possivel do x)
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_rectangle)

    # if player_rectangle.colliderect(snail_rectangle):
    #     print('collision')


   # check if the mouse colides with the player_rectangle
    # mouse_position = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_position): 
    #     print('colisao') 
    

    # ATUALIZANDO TUDO
    pygame.display.update()
    clock.tick(60)