import pygame 
pygame.init()


def display_score():
    current_time = int(pygame.time.get_ticks() / 100)- start_time 
    score_surface = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rectangle)

# DISPLAY SURFACE
screen = pygame.display.set_mode((800, 400)) # criando display surfice (janela de exibição)
pygame.display.set_caption("Runner game") # criando o nome do display surfice
clock = pygame.time.Clock()
game_active = False
start_time = 0

# FONTE
test_font = pygame.font.Font('font/Pixeltype.ttf',50) 

# REGULAR SURFICES
sky_surface = pygame.image.load('grafico/ceu.png').convert() #.convert() otimiza o desempenho da img
ground_surface = pygame.image.load('grafico/chao.png').convert()

# SCORE
# score_surface = test_font.render('Runner game', False,(64,64,64)) #AA desativado
# score_rectangle = score_surface.get_rect(center = (400, 50))

# SNAIL SURFACE
snail_surface = pygame.image.load('grafico\snail\snail1.png').convert_alpha()  
snail_rectangle = snail_surface.get_rect(bottomright = (600,300))
 
# PLAYER SURFACE
player_surface = pygame.image.load('grafico\player\player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))
# PLAYER GRAVITY
player_gravity = 0


# ==== INTRO SCREEN ====
player_stand = pygame.image.load('grafico\player\player_stand.png').convert_alpha() # 1.importando a imagem do player
player_stand = pygame.transform.rotozoom(player_stand,0,2) # 2.pegando a imagem, e a transformando com pygame.transoform.rotozoom(faz uma rotacao da imagem)
player_stand_rectangle = player_stand.get_rect(center = (400,200)) # 3.criando o retangulo em volta da imagem player

game_name = test_font.render('Mario Bross da shoppe', False, (111,196,169))
game_name_rectangle = game_name.get_rect(center = (400,80))

# se n tem score, pede para apertar espaço para comecar. Se tem score, mostra o score
game_message = test_font.render('Press space to run',  False, (111,196,169) )
game_message_rectangle = game_message.get_rect(center = (400,34 0))
running = True
while running:
    for event in pygame.event.get():
        # CHECANDO O DISPLAY SURFICE PARA PODER FECHAR 
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            # CHECANDO MOVIMENTOS DO MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                    player_gravity = -20

            # CHECANDO INPUT KEYBOARD
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300: # aqui o player so pode pular dnv, quando estiver tocando no chao. Para evitar pular muito, e sair da tela
                    player_gravity = -20
        else: # caso seja game over, aperta espaco para voltar ao inicio
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800 # faz a lesma "renacer" para o lado, dando a impressao de voltar o jogo ao inicio
                start_time = int(pygame.time.get_ticks() / 100 )

    if game_active:         
        # PRINTING THE SURFACES
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rectangle,border_radius = 10)
        # screen.blit(score_surface, score_rectangle)

        snail_rectangle.x-= 4
        if snail_rectangle.right <= 0: snail_rectangle.left = 800 # se a parte direita retangulo da lesma for <= 0 (), "renascer" a lesma no 800 (mais esquerda possivel do x)
        screen.blit(snail_surface, snail_rectangle)

        # ==== PLAYER ==== 
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300 # se o player estiver em um ponto >= 300, colocar ele de volta no 300 (pos y) | BARREIRA PARA MANTES O PLAYER NA ALTURA DO CHAO
        screen.blit(player_surface, player_rectangle)


        # ==== COLISAO ====
        # se o player colidir com a lesma == game over
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
            screen.fill('Blue')
        
        display_score()      
    else:
        screen.fill((94,129,162))  
        screen.blit(player_stand, player_stand_rectangle) # desenhado passos 1,2,3 do PLAYER
        screen.blit(game_name, game_name_rectangle)
        screen.blit(game_message, game_message_rectangle)

 
    # ATUALIZANDO TUDO
    pygame.display.update()
    clock.tick(60)