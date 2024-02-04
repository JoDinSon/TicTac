import os
import pygame
os.system ("clear")

class Board():
    def __init__(self):
        self.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def display(self):
        print (" %s | %s | %s " %(self.cells[0][0], self.cells[0][1], self.cells[0][2]))
        print ("------------")
        print (" %s | %s | %s " %(self.cells[1][0], self.cells[1][1], self.cells[1][2]))
        print ("------------")
        print (" %s | %s | %s " %(self.cells[2][0], self.cells[2][1], self.cells[2][2]))

    def update_board(self, choice, sign):
        count = 1
        for i in range(3):
            for j in range(3):
                if count == choice:
                    #print("[%i, %i]" %(i, j))
                    if self.cells[i][j] != " ":
                        return False
                    else:
                        self.cells[i][j] = sign
                        return True
                else:
                    count = count + 1
                    #continue
        return False #brauche ich das hier überhaupt?


    def is_full(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] != " ":
                    count = count + 1

        print(count)
        if count == 9:
            return True
        else:
            return False
        


            


board = Board()
count = 0
def check_winner():
    #iterate through all cells
    for i in range(3):
        for j in range(3):
            current_cell = board.cells[i][j]
            # iterater over current_cells vicinity
            if current_cell != " ":
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        # check wether vicinity indices are out of bound
                        if i + k in range(3) and j + l in range(3):
                            m, n = i + k, j + l
                            # check wether current_cell has equal cell in vicinity
                            # avoid that current_cell is compared with itself with second conditional statement
                            if current_cell == board.cells[m][n] and (k != 0 or l != 0):
                                #check wether indices of next cell in same direction are out fo bound
                                if m + k in range(3) and n + l in range(3):
                                    # check wether next cell is also equal to current cell
                                    if current_cell == board.cells[m+k][n+l]:
                                        # if so a Winner is found!
                                        #print("Winner %s" %(current_cell))
                                        #print("[%i, %i]" %(i, j))
                                        #print("[%i, %i]" %(m, n))
                                        #print("[%i, %i]" %(m+k, n+l))
                                        return current_cell
    return 
                               
#print("winner: %s" %(check_winner()))


def print_header():
    print ("Willkommen zu Tic-Tac-Toe\n")

def refresh_screen():
    #Clear the screen
    os.system("clear")

    #Print the header
    print_header()

    
    #print("Winner: %s" %(check_winner()))

    #Show the board
    board.display()


while True:
    refresh_screen()

    #Get X input
    while True:
        try:
            x_choice = int(input("\nX) Bitte wähle 1 - 9. > "))
            if board.update_board(x_choice, "X"):
                break
            else:
                refresh_screen()
                print("\nUngültiger Zug!")
                pass
        except:
            refresh_screen()
            pass
   

    #Update board
    

    refresh_screen()

    if board.is_full():
        print("\nUnentschieden\n")
        break

    if check_winner() == "X":
        print("\n Der Gewinner ist X\n")
        break


    #Get O input
    
    while True:
            try:
                o_choice = int(input("\nO) Bitte wähle 1 - 9. > "))
                if board.update_board(o_choice, "O"):
                    break
                else:
                    refresh_screen()
                    print("\nUngültiger Zug!")
                    pass
            except:
                refresh_screen()
                pass
   

    #Update board
    board.update_board(o_choice, "O")


    refresh_screen()


    if check_winner() == "O":
        print("Der Gewinner ist O\n")
        break

   
    




