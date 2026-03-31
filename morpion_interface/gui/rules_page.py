import tkinter as tk
from tkinter import font

class RulesPage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#f0f0f0")  # Fond global harmonisé
        self.create_widgets()

    def create_widgets(self):
        # Bloc centré
        content_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="groove", padx=40, pady=40)
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_font = font.Font(family="Helvetica", size=32, weight="bold")
        title_label = tk.Label(content_frame, text="Règles du jeu", font=title_font, bg="#ffffff", fg="#333")
        title_label.pack(pady=(0, 30), anchor="center")

        rules_text = (
            "Le Morpion se joue à deux joueurs.\n\n"
            "• Le Joueur X commence toujours.\n"
            "• Le premier à aligner 3 symboles\n"
            "  (horizontal, vertical, diagonal) gagne.\n"
            "• Si toutes les cases sont remplies\n"
            "  sans alignement, c’est une partie nulle."
        )
        label = tk.Label(content_frame, text=rules_text, bg="#ffffff", font=("Helvetica", 14), justify="left", fg="#444")
        label.pack(pady=10, anchor="w") # Alignement à gauche

        close_button = tk.Button(content_frame, text="Retour", font=("Helvetica", 14, "bold"),
                                 bg="#f44336", fg="white", activebackground="#d32f2f", 
                                 activeforeground="white", bd=0, width=15, pady=8, cursor="hand2",
                                 command=lambda: self.show_page("main"))
        close_button.pack(pady=(20, 0), anchor="w")