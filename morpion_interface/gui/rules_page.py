import tkinter as tk
from tkinter import font

class RulesPage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#2E3440")
        self.create_widgets()

    def create_widgets(self):
        # Ombre tombante
        shadow = tk.Frame(self, bg="#1a1e26")
        shadow.place(relx=0.5, rely=0.5, anchor="center", width=420, height=470)
        
        # Carte centrale
        content_frame = tk.Frame(self, bg="#ECEFF4", bd=0)
        content_frame.place(relx=0.495, rely=0.49, anchor="center", width=420, height=470)

        title_font = font.Font(family="Trebuchet MS", size=32, weight="bold")
        tk.Label(content_frame, text="Règles du jeu", font=title_font, bg="#ECEFF4", fg="#2E3440").pack(pady=(30, 20))

        rules_text = (
            "🎯 Le Morpion se joue à 2 joueurs.\n\n"
            "❌ Le Joueur X commence toujours.\n"
            "👑 Le premier à aligner 3 symboles\n"
            "    (horizontal, vertical, diagonal)\n"
            "    remporte la victoire !\n\n"
            "🤝 S'il n'y a plus de cases vides\n"
            "    sans gagnant, c'est un nul."
        )
        tk.Label(content_frame, text=rules_text, bg="#ECEFF4", font=("Trebuchet MS", 14), justify="left", fg="#4C566A").pack(pady=10)

        btn = tk.Button(content_frame, text="COMPRIS !", font=("Trebuchet MS", 14, "bold"),
                        bg="#5E81AC", fg="white", activebackground="#81A1C1", 
                        bd=0, width=15, pady=10, cursor="hand2",
                        command=lambda: self.show_page("main"))
        btn.pack(pady=(40, 0))