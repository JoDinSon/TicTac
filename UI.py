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




# create individual fields to geht mouse location
class field:
    def __init__(self, pos_x, pos_y, width, height, number):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.number = number
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(screen, BLACK, [self.pos_x, self.pos_y, self.width, self.height], 3)

    
    def check_click(self, mouse, ev, player) -> bool:
        
        if self.rect.collidepoint(mouse):
            #highlight if mouse hovers over current field
            pygame.draw.rect(screen, ORANGE, [self.pos_x + 3, self.pos_y + 3, self.width - 4, self.height - 4], 2)
            # if there is a click event draw an x inside th field
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player == "X":
                        self.draw_x()
                        return True
                    else:
                        self.draw_o()
                        return True
        else:
            pygame.draw.rect(screen, WHITE, [self.pos_x + 3, self.pos_y + 3, self.width - 4, self.height - 4], 2)
            return False
        # draw an x
    def draw_x(self):
        pygame.draw.line(screen, ORANGE, [self.pos_x + 15, self.pos_y + 15], [self.pos_x + 85, self.pos_y + 85], 6)
        pygame.draw.line(screen, ORANGE, [self.pos_x + 85, self.pos_y + 15], [self.pos_x + 15, self.pos_y + 85], 6)
    
    def draw_o(self):
        # draw circle
        pygame.draw.ellipse(screen, BLUE, [215, 15, 70, 70], 6)






'''

# Game loop

active = True
while active:
    # put all events in a ev variable
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            active = False

   
 

    for i in range(len(fields)):
        # call ceck_click method on all fields and give it the mouse position and the event list
        fields[i].check_click(pygame.mouse.get_pos(), ev)




    # display refresh
    pygame.display.flip()

    #refresh time
    clock.tick(60)


# quit pygame
pygame.quit()

'''

