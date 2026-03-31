import tkinter as tk
from tkinter import font
from game.board import Board
from ai.alphabeta import get_best_move
from ai.ml_model import TicTacToeMLModel

class GamePage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#2E3440")
        
        self.board = Board()
        self.ml_model = TicTacToeMLModel()
        self.mode = "friend" 
        self.p1_name = ""
        self.p2_name = ""
        self.difficulty = None
        self.ai_letter = "O"
        
        self.current_player_name = ""
        self.current_letter = "X"
        self.game_over = False
        
        self.create_widgets()

    def configure_game(self, mode, p1_name, p2_name, difficulty, ai_letter="O"):
        self.mode = mode
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.difficulty = difficulty
        self.ai_letter = ai_letter
        self.reset_board()

    def create_widgets(self):
        shadow = tk.Frame(self, bg="#1a1e26")
        shadow.place(relx=0.5, rely=0.5, anchor="center", width=460, height=550)

        content_frame = tk.Frame(self, bg="#ECEFF4")
        content_frame.place(relx=0.495, rely=0.495, anchor="center", width=460, height=550)

        self.title_label = tk.Label(content_frame, text="Tour de X", font=("Trebuchet MS", 22, "bold"), bg="#ECEFF4", fg="#4C566A")
        self.title_label.pack(pady=(20, 10))

        self.board_frame = tk.Frame(content_frame, bg="#d8dee9", bd=5, relief="flat")
        self.board_frame.pack(pady=10)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.board_frame, text="", font=("Trebuchet MS", 36, "bold"), width=3, height=1,
                                bd=0, relief="flat", cursor="hand2", bg="#FFFFFF", activebackground="#F5F7FA",
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=3, pady=3)
                self.buttons[i][j] = btn

        self.result_label = tk.Label(content_frame, text="", font=("Trebuchet MS", 18, "bold"), bg="#ECEFF4")
        self.result_label.pack(pady=(10, 5))

        bottom_frame = tk.Frame(content_frame, bg="#ECEFF4")
        bottom_frame.pack(pady=(10, 20))

        tk.Button(bottom_frame, text="< Quitter", font=("Trebuchet MS", 14, "bold"),
                  bg="#D8DEE9", fg="#4C566A", activebackground="#E5E9F0",
                  bd=0, width=10, pady=8, cursor="hand2", command=lambda: self.show_page("main")).pack(side="left", padx=10)

        self.restart_btn = tk.Button(bottom_frame, text="REJOUER", font=("Trebuchet MS", 14, "bold"),
                                     bg="#88C0D0", fg="#2E3440", activebackground="#81A1C1",
                                     bd=0, width=12, pady=8, cursor="hand2", command=self.reset_board)
        self.restart_btn.pack(side="left", padx=10)

    def on_click(self, row, col):
        if self.game_over: return
        if self.mode == "ai" and self.current_letter == self.ai_letter: return
            
        square = row * 3 + col
        if self.board.make_move(square, self.current_letter):
            self._update_btn(row, col, self.current_letter)
            if self.check_game_end(): return
            self.switch_player()
            if self.mode == "ai" and self.current_letter == self.ai_letter and not self.game_over:
                self.title_label.config(text="Réflexion de l'IA...")
                self.update()
                self.after(500, self.ai_move)

    def ai_move(self):
        if self.game_over: return
        
        square = self.ml_model.predict_move(self.board, self.ai_letter) if self.difficulty == "ML" else get_best_move(self.board, self.ai_letter, self.difficulty)
            
        if square is not None and self.board.make_move(square, self.ai_letter):
            r, c = square // 3, square % 3
            self._update_btn(r, c, self.ai_letter)
            if self.check_game_end(): return
            self.switch_player()

    def _update_btn(self, r, c, letter):
        color = "#BF616A" if letter == "X" else "#5E81AC"
        self.buttons[r][c].config(text=letter, state="disabled", disabledforeground=color, bg="#E5E9F0")

    def check_game_end(self):
        if self.board.current_winner:
            w = self.p1_name if self.board.current_winner == "X" else self.p2_name
            self.result_label.config(text=f"✨ {w} gagne ! ✨", fg="#A3BE8C")
            self.title_label.config(text="Terminé")
            self.game_over = True
            self._disable_all()
            return True
        elif not self.board.empty_squares():
            self.result_label.config(text="Égalité !", fg="#EBCB8B")
            self.title_label.config(text="Terminé")
            self.game_over = True
            return True
        return False

    def _disable_all(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == "":
                    self.buttons[i][j].config(state="disabled", bg="#ECEFF4")

    def switch_player(self):
        self.current_letter = "O" if self.current_letter == "X" else "X"
        self.current_player_name = self.p2_name if self.current_letter == "O" else self.p1_name
        self.title_label.config(text=f"Tour de {self.current_player_name} ({self.current_letter})")

    def reset_board(self):
        self.board.reset()
        self.game_over = False
        self.current_letter = "X"
        self.current_player_name = self.p1_name
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal", bg="#FFFFFF")
        self.title_label.config(text=f"Tour de {self.current_player_name} (X)")
        self.result_label.config(text="")
        
        if self.mode == "ai" and self.current_letter == self.ai_letter:
            self.title_label.config(text="Réflexion de l'IA...")
            self.update()
            self.after(500, self.ai_move)