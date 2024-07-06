import tkinter as tk
from functools import partial
from tkinter import messagebox

class TicTacToeAI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe AI")
        self.window.geometry('600x600')
        self.center_window()
        self.window.configure(bg='#ADD8E6') 
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.button_color = '#FFB6C1'  
        self.text_color = '#000080'  
        self.buttons = [tk.Button(self.window, text='', font='Arial 20', width=10, height=5, bg=self.button_color, fg=self.text_color, command=partial(self.make_move, i)) for i in range(9)]
        self.reset_button = tk.Button(self.window, text='Reset', font='Arial 20', bg='#FFA07A', fg=self.text_color, command=self.reset_board)  
        self.draw_board()
        self.window.mainloop()

    def draw_board(self):
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col, padx=10, pady=10)
        self.reset_button.grid(row=3, column=0, columnspan=3, pady=20)

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def reset_board(self):
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text='', state=tk.NORMAL, bg=self.button_color, fg=self.text_color)

    def make_move(self, index):
        if self.board[index] == '' and self.current_player == 'X':
            self.board[index] = 'X'
            self.buttons[index].config(text='X', state=tk.DISABLED, bg='#98FB98')  
            if not self.check_winner():
                self.current_player = 'O'
                self.window.after(500, self.ai_move)

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(9):
            if self.board[i] == '':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ''
                if score > best_score:
                    best_score = score
                    best_move = i
        if best_move is not None:
            self.board[best_move] = 'O'
            self.buttons[best_move].config(text='O', state=tk.DISABLED, bg='#FF6347')  
        if not self.check_winner():
            self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner_temp(board)
        if winner:
            return {'X': -1, 'O': 1, 'Tie': 0}[winner]
        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ''
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ''
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for (a, b, c) in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != '':
                for button in self.buttons:
                    button.config(state=tk.DISABLED)
                self.show_winner_message(self.board[a])
                return self.board[a]
        if '' not in self.board:
            self.show_winner_message('Tie')
            return 'Tie'
        return None

    def check_winner_temp(self, board):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for (a, b, c) in win_conditions:
            if board[a] == board[b] == board[c] != '':
                return board[a]
        if '' not in board:
            return 'Tie'
        return None

    def show_winner_message(self, winner):
        if winner == 'X':
            messagebox.showinfo("Game Over", "You win!")
        elif winner == 'O':
            messagebox.showinfo("Game Over", "You lose!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_board()

TicTacToeAI()
