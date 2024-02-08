class Board():
    def __init__(self):
        self.cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


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

        #print(count)
        print(self.cells)
        if count == 9:
            return True
        else:
            return False
    


    def check_winner(self):
        #iterate through all cells
        for i in range(3):
            for j in range(3):
                current_cell = self.cells[i][j]
                # iterater over current_cells vicinity
                if current_cell != " ":
                    for k in [-1, 0, 1]:
                        for l in [-1, 0, 1]:
                            # check wether vicinity indices are out of bound
                            if i + k in range(3) and j + l in range(3):
                                m, n = i + k, j + l
                                # check wether current_cell has equal cell in vicinity
                                # avoid that current_cell is compared with itself with second conditional statement
                                if current_cell == self.cells[m][n] and (k != 0 or l != 0):
                                    #check wether indices of next cell in same direction are out fo bound
                                    if m + k in range(3) and n + l in range(3):
                                        # check wether next cell is also equal to current cell
                                        if current_cell == self.cells[m+k][n+l]:
                                            # if so a Winner is found!
                                            #print("Winner %s" %(current_cell))
                                            #print("[%i, %i]" %(i, j))
                                            #print("[%i, %i]" %(m, n))
                                            #print("[%i, %i]" %(m+k, n+l))
                                            return current_cell
        return