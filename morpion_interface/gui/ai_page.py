import tkinter as tk
from tkinter import font

class AIPage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        # Bloc centré
        content_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="groove", padx=40, pady=40)
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_font = font.Font(family="Helvetica", size=26, weight="bold")
        tk.Label(content_frame, text="Contre l'Ordinateur", font=title_font, bg="#ffffff", fg="#333").pack(pady=(0, 20), anchor="center")

        tk.Label(content_frame, text="Votre Nom :", bg="#ffffff", font=("Helvetica", 14)).pack(pady=(5, 5), anchor="w")
        self.player_entry = tk.Entry(content_frame, font=("Helvetica", 14), justify="left", width=30, bd=2)
        self.player_entry.pack(pady=5, anchor="w")

        # Difficulté horizontale
        tk.Label(content_frame, text="Difficulté :", bg="#ffffff", font=("Helvetica", 14, "bold")).pack(pady=(15, 5), anchor="w")
        diff_frame = tk.Frame(content_frame, bg="#ffffff")
        diff_frame.pack(pady=5, anchor="w")
        self.difficulty_var = tk.StringVar(value="Facile")
        radio_opts = {"bg": "#ffffff", "font": ("Helvetica", 12), "activebackground": "#ffffff", "cursor": "hand2"}
        tk.Radiobutton(diff_frame, text="Facile", variable=self.difficulty_var, value="Facile", **radio_opts).pack(side="left", padx=(0, 10))
        tk.Radiobutton(diff_frame, text="Moyen", variable=self.difficulty_var, value="Moyen", **radio_opts).pack(side="left", padx=10)
        tk.Radiobutton(diff_frame, text="Difficile", variable=self.difficulty_var, value="Difficile", **radio_opts).pack(side="left", padx=10)
        tk.Radiobutton(diff_frame, text="IA (Modele ML)", variable=self.difficulty_var, value="ML", **radio_opts).pack(side="left", padx=(10, 0))

        # Symbole horizontal
        tk.Label(content_frame, text="Symbole :", bg="#ffffff", font=("Helvetica", 14, "bold")).pack(pady=(15, 5), anchor="w")
        sym_frame = tk.Frame(content_frame, bg="#ffffff")
        sym_frame.pack(pady=5, anchor="w")
        self.symbol_var = tk.StringVar(value="X")
        tk.Radiobutton(sym_frame, text="X (1er)", variable=self.symbol_var, value="X", **radio_opts).pack(side="left", padx=(0, 15))
        tk.Radiobutton(sym_frame, text="O (2ème)", variable=self.symbol_var, value="O", **radio_opts).pack(side="left", padx=15)

        btn_frame = tk.Frame(content_frame, bg="#ffffff")
        btn_frame.pack(pady=(30, 0), anchor="w")

        back_button = tk.Button(btn_frame, text="Retour", font=("Helvetica", 14, "bold"),
                                bg="#9e9e9e", fg="white", activebackground="#757575",
                                bd=0, width=10, pady=8, cursor="hand2",
                                command=lambda: self.show_page("main"))
        back_button.pack(side="left", padx=(0, 10))

        start_button = tk.Button(btn_frame, text="Commencer", font=("Helvetica", 14, "bold"),
                                 bg="#2196F3", fg="white", activebackground="#1976D2",
                                 bd=0, width=15, pady=8, cursor="hand2",
                                 command=self.start_game)
        start_button.pack(side="left", padx=10)

    def start_game(self):
        p1 = self.player_entry.get().strip() or "Joueur"
        difficulty = self.difficulty_var.get()
        symbol = self.symbol_var.get()
        
        if symbol == "X":
            self.master.start_game("ai", p1, "Ordinateur", difficulty, "O")
        else:
            self.master.start_game("ai", "Ordinateur", p1, difficulty, "X")