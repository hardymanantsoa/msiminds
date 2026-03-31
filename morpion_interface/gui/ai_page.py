import tkinter as tk
from tkinter import font

class AIPage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#2E3440")
        self.create_widgets()

    def create_widgets(self):
        shadow = tk.Frame(self, bg="#1a1e26")
        shadow.place(relx=0.5, rely=0.5, anchor="center", width=460, height=520)

        content_frame = tk.Frame(self, bg="#ECEFF4", bd=0)
        content_frame.place(relx=0.495, rely=0.49, anchor="center", width=460, height=520)

        title_font = font.Font(family="Trebuchet MS", size=26, weight="bold")
        tk.Label(content_frame, text="Humain vs Machine 🤖", font=title_font, bg="#ECEFF4", fg="#B48EAD").pack(pady=(30, 20))

        form_frame = tk.Frame(content_frame, bg="#ECEFF4")
        form_frame.pack(fill="x", padx=30)

        tk.Label(form_frame, text="Votre Nom :", bg="#ECEFF4", font=("Trebuchet MS", 14, "bold"), fg="#4C566A").pack(anchor="w", pady=(5, 0))
        self.player_entry = tk.Entry(form_frame, font=("Trebuchet MS", 14), width=20, bd=0, highlightthickness=2, highlightcolor="#B48EAD", highlightbackground="#D8DEE9")
        self.player_entry.pack(fill="x", pady=5)

        tk.Label(form_frame, text="Niveau d'Intelligence :", bg="#ECEFF4", font=("Trebuchet MS", 14, "bold"), fg="#4C566A").pack(anchor="w", pady=(15, 0))
        diff_frame = tk.Frame(form_frame, bg="#ECEFF4")
        diff_frame.pack(anchor="w", pady=5)
        self.difficulty_var = tk.StringVar(value="Facile")
        opts = {"bg": "#ECEFF4", "fg": "#2E3440", "font": ("Trebuchet MS", 12), "activebackground": "#ECEFF4", "cursor": "hand2", "selectcolor": "#ffffff"}
        tk.Radiobutton(diff_frame, text="Facile", variable=self.difficulty_var, value="Facile", **opts).pack(side="left")
        tk.Radiobutton(diff_frame, text="Moyen", variable=self.difficulty_var, value="Moyen", **opts).pack(side="left")
        tk.Radiobutton(diff_frame, text="Difficile", variable=self.difficulty_var, value="Difficile", **opts).pack(side="left")
        tk.Radiobutton(diff_frame, text="IA (ML)", variable=self.difficulty_var, value="ML", **opts).pack(side="left")

        tk.Label(form_frame, text="Symbole :", bg="#ECEFF4", font=("Trebuchet MS", 14, "bold"), fg="#4C566A").pack(anchor="w", pady=(15, 0))
        sym_frame = tk.Frame(form_frame, bg="#ECEFF4")
        sym_frame.pack(anchor="w", pady=5)
        self.symbol_var = tk.StringVar(value="X")
        tk.Radiobutton(sym_frame, text="X (Commence)", variable=self.symbol_var, value="X", **opts).pack(side="left", padx=(0, 20))
        tk.Radiobutton(sym_frame, text="O (Second)", variable=self.symbol_var, value="O", **opts).pack(side="left")

        btn_frame = tk.Frame(content_frame, bg="#ECEFF4")
        btn_frame.pack(pady=(30, 0))

        tk.Button(btn_frame, text="< RETOUR", font=("Trebuchet MS", 14, "bold"),
                  bg="#D8DEE9", fg="#4C566A", activebackground="#E5E9F0",
                  bd=0, width=10, pady=10, cursor="hand2", command=lambda: self.show_page("main")).pack(side="left", padx=10)

        tk.Button(btn_frame, text="DÉFIER !", font=("Trebuchet MS", 14, "bold"),
                  bg="#B48EAD", fg="#ECEFF4", activebackground="#81A1C1",
                  bd=0, width=15, pady=10, cursor="hand2", command=self.start_game).pack(side="left", padx=10)

    def start_game(self):
        p1 = self.player_entry.get().strip() or "Humain"
        difficulty = self.difficulty_var.get()
        symbol = self.symbol_var.get()
        if symbol == "X":
            self.master.start_game("ai", p1, "L'IA", difficulty, "O")
        else:
            self.master.start_game("ai", "L'IA", p1, difficulty, "X")