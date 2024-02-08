import pygame
from UI import field
from game import *


#set refresh
clock = pygame.time.Clock()

#Create Names for fields
num_fields = 9
fields_names = [f'field_{i+1}' for i in range(num_fields)]

#creating the empty field variables
fields = [0 for _ in range(len(fields_names))]

# set size of the individual rectangles
field_side = 100

# fill the list of fields with field instance
index = 0
for i in range(3):
    for j in range(3):
        fields[index] = field(i * field_side, j * field_side, field_side, field_side, i * j + 1)
        index += 1

# Create Board for tracking the game
board = Board()

# Gameloop

active = True
player = "X"
while active:
    # put all events in a ev variable
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            active = False

 

    for i in range(len(fields)):
        # call ceck_click method on all fields and give it the mouse position and the event list
        if fields[i].check_click(pygame.mouse.get_pos(), ev, player):
            board.update_board(i + 1, player)
            if board.is_full():
                print("\nUnentschieden\n")
                active = False
                break

            if board.check_winner() == "X":
                print("\n Der Gewinner ist X\n")
                active = False
                break

            if board.check_winner() == "O":
                print("\nDer Gewinner ist O\n")
                active = False
                break

            # switch player
            if player == "X":
                player = "O"
            elif player == "O":
                player = "X"





    



    # display refresh
    pygame.display.flip()

    #refresh time
    clock.tick(60)


# quit pygame
pygame.quit()