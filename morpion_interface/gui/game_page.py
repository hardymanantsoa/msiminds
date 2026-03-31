import tkinter as tk
from tkinter import font
from game.board import Board
from ai.alphabeta import get_best_move
from ai.ml_model import TicTacToeMLModel

class GamePage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#f0f0f0")
        
        self.board = Board()
        self.ml_model = TicTacToeMLModel()
        self.mode = "friend" 
        self.p1_name = "Joueur 1"
        self.p2_name = "Joueur 2"
        self.difficulty = None
        self.ai_letter = "O"
        
        self.current_player_name = self.p1_name
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
        # Bloc d'interface central style "carte"
        content_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="groove", padx=30, pady=30)
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Titre centré
        self.title_label = tk.Label(content_frame, text="Tour du joueur: X", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#d81b60")
        self.title_label.pack(pady=(0, 20), anchor="center")

        # Les autres éléments alignés à gauche (selon la consigne)
        self.board_frame = tk.Frame(content_frame, bg="#ffffff")
        self.board_frame.pack(pady=10, anchor="w")

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.board_frame, text="", font=("Helvetica", 28, "bold"), width=4, height=2,
                                bd=3, relief="groove", cursor="hand2", bg="#f5f5f5",
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = btn

        self.result_label = tk.Label(content_frame, text="", font=("Helvetica", 18, "bold"), bg="#ffffff")
        self.result_label.pack(pady=(20, 10), anchor="w")

        bottom_frame = tk.Frame(content_frame, bg="#ffffff")
        bottom_frame.pack(pady=(10, 0), anchor="w")

        back_button = tk.Button(bottom_frame, text="Retour", font=("Helvetica", 14, "bold"),
                                bg="#9e9e9e", fg="white", activebackground="#757575",
                                bd=0, width=10, pady=8, cursor="hand2", command=lambda: self.show_page("main"))
        back_button.pack(side="left", padx=(0, 10))

        restart_button = tk.Button(bottom_frame, text="Recommencer", font=("Helvetica", 14, "bold"),
                                   bg="#FF9800", fg="white", activebackground="#F57C00",
                                   bd=0, width=15, pady=8, cursor="hand2", command=self.reset_board)
        restart_button.pack(side="left", padx=10)

    def on_click(self, row, col):
        if self.game_over:
            return
            
        # Bloquer le clic si c'est au tour de l'IA
        if self.mode == "ai" and self.current_letter == self.ai_letter:
            return
            
        square = row * 3 + col
        if self.board.make_move(square, self.current_letter):
            self.buttons[row][col].config(text=self.current_letter, state="disabled", 
                                          disabledforeground="#1565C0" if self.current_letter == "X" else "#C62828",
                                          bg="#e0e0e0")
            
            if self.check_game_end():
                return
                
            self.switch_player()
            
            if self.mode == "ai" and self.current_letter == self.ai_letter and not self.game_over:
                self.title_label.config(text=f"Tour de l'ordinateur...")
                self.update() # Force update to show AI thinking text
                self.after(400, self.ai_move)

    def ai_move(self):
        if self.game_over:
            return
            
        if self.difficulty == "ML":
            square = self.ml_model.predict_move(self.board, self.ai_letter)
        else:
            square = get_best_move(self.board, self.ai_letter, self.difficulty)
            
        if square is not None:
            if self.board.make_move(square, self.ai_letter):
                r, c = square // 3, square % 3
                self.buttons[r][c].config(text=self.ai_letter, state="disabled", 
                                          disabledforeground="#1565C0" if self.ai_letter == "X" else "#C62828",
                                          bg="#e0e0e0")
                
                if self.check_game_end():
                    return
                    
                self.switch_player()

    def check_game_end(self):
        if self.board.current_winner:
            winner_name = self.p1_name if self.board.current_winner == "X" else self.p2_name
            self.result_label.config(text=f"👑 Victoire de {winner_name} !", fg="#2E7D32")
            self.title_label.config(text="Partie terminée")
            self.game_over = True
            
            # Disable remaining buttons
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]['text'] == "":
                        self.buttons[i][j].config(state="disabled")
            return True
            
        elif not self.board.empty_squares():
            self.result_label.config(text="Match Nul !", fg="#E65100")
            self.title_label.config(text="Partie terminée")
            self.game_over = True
            return True
        return False

    def switch_player(self):
        if self.current_letter == "X":
            self.current_letter = "O"
            self.current_player_name = self.p2_name
        else:
            self.current_letter = "X"
            self.current_player_name = self.p1_name
            
        self.title_label.config(text=f"Tour de {self.current_player_name} ({self.current_letter})")

    def reset_board(self):
        self.board.reset()
        self.game_over = False
        self.current_letter = "X"
        self.current_player_name = self.p1_name
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal", bg="#f5f5f5")
                
        self.title_label.config(text=f"Tour de {self.current_player_name} (X)")
        self.result_label.config(text="")
        
        # Si c'est à l'IA de commencer
        if self.mode == "ai" and self.current_letter == self.ai_letter:
            self.title_label.config(text=f"Tour de l'ordinateur...")
            self.update()
            self.after(400, self.ai_move)