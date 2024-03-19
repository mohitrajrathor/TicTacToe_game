import tkinter as tk
import tkinter.messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None]*3 for _ in range(3)]
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.frame, text=' ', font=('Arial', 20), width=5, height=3,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.pack()

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                tkinter.messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.highlight_winner()
                self.reset_game()
            elif self.check_draw():
                tkinter.messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O':
                    self.computer_move()

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def highlight_winner(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.current_player:
                    self.buttons[i][j].config(bg='green')
                else:
                    self.buttons[i][j].config(bg='red')

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', bg='SystemButtonFace')
        self.current_player = 'X'
        if self.current_player == 'O':
            self.computer_move()

    def computer_move(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if available_moves:
            row, col = random.choice(available_moves)
            self.make_move(row, col)