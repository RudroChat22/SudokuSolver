import tkinter as tk
from tkinter import messagebox
from sudoku import solve,check  # Import your solving function

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        # Initialize the grid of entry widgets
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

        # Add Solve and Clear buttons
        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=10, column=2, columnspan=2, pady=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_grid)
        self.clear_button.grid(row=10, column=5, columnspan=2, pady=10)

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                # Create an entry widget for each cell
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=5, pady=5)
                self.entries[row][col] = entry

    def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)

    def get_grid(self):
        grid = []
        for row in range(9):
            grid_row = []
            for col in range(9):
                val = self.entries[row][col].get()
                if val.isdigit():
                    grid_row.append(int(val))
                else:
                    grid_row.append(0)
            grid.append(grid_row)
        return grid

    def set_grid(self, grid):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                if grid[row][col] != 0:
                    self.entries[row][col].insert(0, str(grid[row][col]))

    def solve(self):
        grid = self.get_grid()
        if solve(grid):  # Call the imported solving function
            self.set_grid(grid)
        else:
            messagebox.showerror("Error", "No solution exists for this Sudoku puzzle")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
