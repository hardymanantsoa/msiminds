import tkinter as tk
from tkinter import font

class MainPage(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page = show_page_callback
        self.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        # Bouton "?" rond dessiné via un Canvas
        self.canvas = tk.Canvas(self, width=40, height=40, bg="#f0f0f0", highlightthickness=0)
        self.canvas.place(relx=1.0, x=-20, y=20, anchor="ne")
        self.circle = self.canvas.create_oval(2, 2, 38, 38, fill="#e0e0e0", outline="#bdbdbd", width=2)
        self.text = self.canvas.create_text(20, 20, text="?", font=("Helvetica", 16, "bold"), fill="#424242")
        self.canvas.bind("<Button-1>", lambda e: self.show_page("rules"))
        self.canvas.bind("<Enter>", lambda e: self.canvas.itemconfig(self.circle, fill="#bdbdbd"))
        self.canvas.bind("<Leave>", lambda e: self.canvas.itemconfig(self.circle, fill="#e0e0e0"))
        
        # Cursor hand
        self.canvas.config(cursor="hand2")

        # Container centré
        center_frame = tk.Frame(self, bg="#f0f0f0")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_font = font.Font(family="Helvetica", size=48, weight="bold")
        title_label = tk.Label(center_frame, text="Morpion", font=title_font, bg="#f0f0f0", fg="#333")
        title_label.pack(pady=(0, 60))

        button_font = font.Font(family="Helvetica", size=16, weight="bold")
        btn_style = {"font": button_font, "bg": "#4CAF50", "fg": "white", 
                     "activebackground": "#388E3C", "activeforeground": "white", 
                     "bd": 0, "width": 22, "height": 2, "cursor": "hand2"}

        friend_button = tk.Button(center_frame, text="Jouer avec amie", command=lambda: self.show_page("friend"), **btn_style)
        friend_button.pack(pady=15)

        ai_button = tk.Button(center_frame, text="Jouer avec ordinateur", command=lambda: self.show_page("ai"), **btn_style)
        ai_button.pack(pady=15)