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
class field:
    def __init__(self, pos_x, pos_y, width, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(screen, BLACK, [self.pos_x, self.pos_y, self.width, self.height], 3)
    #highlight if mouse hovers over current field
    def check_click(self, mouse):
        
        if self.rect.collidepoint(mouse):
            pygame.draw.rect(screen, ORANGE, [self.pos_x + 3, self.pos_y + 3, self.width - 4, self.height - 4], 2)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("mouse was clicked")
                    self.draw_x()
        else:
            pygame.draw.rect(screen, WHITE, [self.pos_x + 3, self.pos_y + 3, self.width - 4, self.height - 4], 2)
    
        # draw an x
    def draw_x(self):
        pygame.draw.line(screen, ORANGE, [self.pos_x + 15, self.pos_y + 15], [self.pos_x + 85, self.pos_y + 85], 6)
        pygame.draw.line(screen, ORANGE, [self.pos_x + 85, self.pos_y + 15], [self.pos_x + 15, self.pos_y + 85], 6)




# Create Names for fields
num_fields = 9
fields_names = [f'field_{i+1}' for i in range(num_fields)]

#creating the empty field variables
fields = [0 for _ in range(len(fields_names))]

# set size of the individual rectangles
field_side = 100

# fill the list of fields with field instances
index = 0
for i in range(3):
    for j in range(3):
        fields[index] = field(i * field_side, j * field_side, field_side, field_side)
        index += 1
    


#field_1 = field(100, 0, 100, 100)



# Game loop

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    # draw two horizontal lines
    '''
    pygame.draw.line(screen, BLACK, [0, 100], [300, 100], 4)
    pygame.draw.line(screen, BLACK, [0, 200], [300, 200], 4)

    # draw two vertical lines
    pygame.draw.line(screen, BLACK, [100, 0], [100, 300], 4)
    pygame.draw.line(screen, BLACK, [200, 0], [200, 300], 4)
    '''




    # draw circle
    pygame.draw.ellipse(screen, BLUE, [215, 15, 70, 70], 6)

    for i in range(len(fields)):
        fields[i].check_click(pygame.mouse.get_pos())


  
    


    # display refresh
    pygame.display.flip()

    #refresh time
    clock.tick(60)


# quit pygame
pygame.quit()

