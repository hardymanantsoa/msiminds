import tkinter as tk
from tkinter import font

class MainPage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#2E3440") # Fond sombre premium
        self.create_widgets()

    def create_widgets(self):
        # Bouton "?" parfaitement centré
        self.canvas = tk.Canvas(self, width=50, height=50, bg="#2E3440", highlightthickness=0)
        self.canvas.place(relx=1.0, x=-20, y=20, anchor="ne")
        self.circle = self.canvas.create_oval(2, 2, 48, 48, fill="#4C566A", outline="#4C566A", width=0)
        self.text = self.canvas.create_text(25, 25, text="?", font=("Trebuchet MS", 24, "bold"), fill="#ECEFF4", anchor="center")
        self.canvas.bind("<Button-1>", lambda e: self.show_page("rules"))
        self.canvas.bind("<Enter>", lambda e: self.canvas.itemconfig(self.circle, fill="#5E81AC"))
        self.canvas.bind("<Leave>", lambda e: self.canvas.itemconfig(self.circle, fill="#4C566A"))
        self.canvas.config(cursor="hand2")

        center_frame = tk.Frame(self, bg="#2E3440")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_font = font.Font(family="Trebuchet MS", size=56, weight="bold")
        title_label = tk.Label(center_frame, text="MORPION", font=title_font, bg="#2E3440", fg="#88C0D0")
        title_label.pack(pady=(0, 20))

        subtitle = tk.Label(center_frame, text="Le jeu de stratégie ultime", font=("Trebuchet MS", 16, "italic"), bg="#2E3440", fg="#D8DEE9")
        subtitle.pack(pady=(0, 50))

        button_font = font.Font(family="Trebuchet MS", size=18, weight="bold")
        
        btn_friend = tk.Button(center_frame, text="Jouer avec un ami", font=button_font, bg="#A3BE8C", fg="#2E3440", 
                               activebackground="#8FBCBB", activeforeground="#2E3440", bd=0, width=22, height=2, cursor="hand2",
                               command=lambda: self.show_page("friend"))
        btn_friend.pack(pady=15)

        btn_ai = tk.Button(center_frame, text="Jouer avec l'IA", font=button_font, bg="#B48EAD", fg="#ECEFF4", 
                           activebackground="#81A1C1", activeforeground="#ECEFF4", bd=0, width=22, height=2, cursor="hand2",
                           command=lambda: self.show_page("ai"))
        btn_ai.pack(pady=15)