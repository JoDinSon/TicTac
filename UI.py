import pygame

# initalize pygame
pygame.init()

#set colors here
# 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
BLUE = (100, 149, 237)

# Open window
screen = pygame.display.set_mode((300, 300))
# fill it white
screen.fill(WHITE)


# Show Title
pygame.display.set_caption("TicTacToe")

#set refresh
clock = pygame.time.Clock()

# create individual fields to geht mouse location
class field():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 100, 100)

    #highlight if mouse hovers over current field
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            pygame.draw.rect(screen, ORANGE, [0, 0, 99, 99], 4)
        else:
            pygame.draw.rect(screen, WHITE, [0, 0, 99, 99], 4)



field_1 = field()



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

    # draw an x
    pygame.draw.line(screen, ORANGE, [15, 15], [85, 85], 6)
    pygame.draw.line(screen, ORANGE, [85, 15], [15, 85], 6)

    # draw circle
    pygame.draw.ellipse(screen, BLUE, [215, 15, 70, 70], 6)

   
    field_1.check_click(pygame.mouse.get_pos())


  
    


    # display refresh
    pygame.display.flip()

    #refresh time
    clock.tick(60)


# quit pygame
pygame.quit()

