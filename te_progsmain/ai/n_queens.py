class n_queens:
    def __init__(self) -> None:
        self.size = int(input("Enter size of board in nxn format:"))
        self.board = [[False]*self.size for i in range (self.size)]

    def print_board(self):
        for row in self.board:
            for element in row:
                if element == True:
                    print("Q", end = " ")
                else:
                    print("_", end = " ")
            print()
        print()

    def is_safe(self, row: int, col: int) -> bool:
        for i in self.board:
            if (i[col] == True):
                return False
            
        i = row
        j = col
        while (i>=0 and j<self.size):
            if (self.board[i][j] == True):
                return False
            i = i-1
            j = j+1
            
        i = row
        j = col
        while (i>=0 and j>=0):
            if (self.board[i][j] == True):
                return False
            i = i-1
            j = j-1

        return True    
    
    def solve(self, row: int):
        if (row == self.size):
            self.print_board()
            return
        
        for col in range(self.size):
            if (self.is_safe(row, col) == True):
                self.board[row][col] = True
                self.solve(row+1)
                self.board[row][col] = False

if __name__ == "__main__":
    solver = n_queens()
    solver.solve(0)
    


