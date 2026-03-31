import tkinter as tk
from tkinter import font

class FriendPage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#2E3440")
        self.create_widgets()

    def create_widgets(self):
        shadow = tk.Frame(self, bg="#1a1e26")
        shadow.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

        content_frame = tk.Frame(self, bg="#ECEFF4", bd=0)
        content_frame.place(relx=0.495, rely=0.49, anchor="center", width=450, height=450)

        title_font = font.Font(family="Trebuchet MS", size=28, weight="bold")
        tk.Label(content_frame, text="Versus 🏆", font=title_font, bg="#ECEFF4", fg="#BF616A").pack(pady=(40, 30))

        form_frame = tk.Frame(content_frame, bg="#ECEFF4")
        form_frame.pack()

        tk.Label(form_frame, text="Nom Joueur 1 (X) :", bg="#ECEFF4", font=("Trebuchet MS", 14, "bold"), fg="#4C566A").grid(row=0, column=0, sticky="w", pady=10)
        self.player1_entry = tk.Entry(form_frame, font=("Trebuchet MS", 14), width=15, bd=0, highlightthickness=2, highlightcolor="#81A1C1", highlightbackground="#D8DEE9")
        self.player1_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Nom Joueur 2 (O) :", bg="#ECEFF4", font=("Trebuchet MS", 14, "bold"), fg="#4C566A").grid(row=1, column=0, sticky="w", pady=10)
        self.player2_entry = tk.Entry(form_frame, font=("Trebuchet MS", 14), width=15, bd=0, highlightthickness=2, highlightcolor="#81A1C1", highlightbackground="#D8DEE9")
        self.player2_entry.grid(row=1, column=1, padx=10, pady=10)

        btn_frame = tk.Frame(content_frame, bg="#ECEFF4")
        btn_frame.pack(pady=(50, 0))

        tk.Button(btn_frame, text="< RETOUR", font=("Trebuchet MS", 14, "bold"),
                  bg="#D8DEE9", fg="#4C566A", activebackground="#E5E9F0",
                  bd=0, width=10, pady=10, cursor="hand2", command=lambda: self.show_page("main")).pack(side="left", padx=10)

        tk.Button(btn_frame, text="FIGHT !", font=("Trebuchet MS", 14, "bold"),
                  bg="#A3BE8C", fg="#2E3440", activebackground="#8FBCBB",
                  bd=0, width=15, pady=10, cursor="hand2", command=self.start_game).pack(side="left", padx=10)

    def start_game(self):
        p1 = self.player1_entry.get().strip() or "Joueur X"
        p2 = self.player2_entry.get().strip() or "Joueur O"
        self.master.start_game("friend", p1, p2, None)