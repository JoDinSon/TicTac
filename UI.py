import pygame

# initalize pygame
pygame.init()

#set colors here
# 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Open window
screen = pygame.display.set_mode((300, 300))
# fill it white
screen.fill(WHITE)


# Show Title
pygame.display.set_caption("TicTacToe")

#set refresh
clock = pygame.time.Clock()


# Game loop

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    # draw two horizontal lines
    pygame.draw.line(screen, BLACK, [0, 100], [300, 100], 4)
    pygame.draw.line(screen, BLACK, [0, 200], [300, 200], 4)

    # draw two vertical lines
    pygame.draw.line(screen, BLACK, [100, 0], [100, 300], 4)
    pygame.draw.line(screen, BLACK, [200, 0], [200, 300], 4)

    # display refresh
    pygame.display.flip()

    

    #refresh time
    clock.tick(60)


# quit pygame
pygame.quit()

