# main tic_tac_toe game program
import tkinter as tk
import TicTacToe

def main():
    root = tk.Tk()
    game = TicTacToe.TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()