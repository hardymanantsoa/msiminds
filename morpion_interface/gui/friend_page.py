import tkinter as tk
from tkinter import font

class FriendPage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        # Bloc centré
        content_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="groove", padx=40, pady=40)
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_font = font.Font(family="Helvetica", size=28, weight="bold")
        tk.Label(content_frame, text="Jouer avec Amie", font=title_font, bg="#ffffff", fg="#333").pack(pady=(0, 30), anchor="center")

        tk.Label(content_frame, text="Nom Joueur 1 (X) :", bg="#ffffff", font=("Helvetica", 14)).pack(pady=(10, 5), anchor="w")
        self.player1_entry = tk.Entry(content_frame, font=("Helvetica", 14), width=25, bd=2)
        self.player1_entry.pack(pady=5, anchor="w")

        tk.Label(content_frame, text="Nom Joueur 2 (O) :", bg="#ffffff", font=("Helvetica", 14)).pack(pady=(15, 5), anchor="w")
        self.player2_entry = tk.Entry(content_frame, font=("Helvetica", 14), width=25, bd=2)
        self.player2_entry.pack(pady=5, anchor="w")

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
        p1 = self.player1_entry.get().strip() or "Joueur 1"
        p2 = self.player2_entry.get().strip() or "Joueur 2"
        self.master.start_game("friend", p1, p2, None)