import tkinter as tk
from gui.main_page import MainPage
from gui.rules_page import RulesPage
from gui.friend_page import FriendPage
from gui.ai_page import AIPage
from gui.game_page import GamePage

class TicTacToeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Morpion")
        self.geometry("500x600")

        # Créer toutes les pages
        self.pages = {}
        self.pages["main"] = MainPage(self, self.show_page)
        self.pages["rules"] = RulesPage(self, self.show_page)
        self.pages["friend"] = FriendPage(self, self.show_page)
        self.pages["ai"] = AIPage(self, self.show_page)
        self.pages["game"] = GamePage(self, self.show_page)

        # Placer toutes les pages au même endroit
        for page in self.pages.values():
            page.place(x=0, y=0, relwidth=1, relheight=1)

        # Afficher la page principale
        self.show_page("main")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

    def start_game(self, mode, p1, p2, difficulty=None, ai_letter="O"):
        game_page = self.pages["game"]
        game_page.configure_game(mode, p1, p2, difficulty, ai_letter)
        self.show_page("game")

if __name__ == "__main__":
    app = TicTacToeApp()
    app.mainloop()