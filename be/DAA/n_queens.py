def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check the current column for a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False
        
        # Check the left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check the right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False
        
        return True

    def solve(board, row):
        if row == n:
            solutions.append(["".join("Q" if cell == 1 else "." for cell in row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    solutions = []
    empty_board = [[0] * n for _ in range(n)]
    solve(empty_board, 0)
    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()

n = int(input("Enter the value of N for N-Queens: "))
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
print_solutions(solutions)
