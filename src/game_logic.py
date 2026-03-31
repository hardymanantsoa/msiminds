# Fonctions de base pour le jeu de Morpion

def check_winner(board):
    """
    Vérifie s'il y a un gagnant sur le plateau.
    board: liste de 9 éléments ('X', 'O', ou None)
    Retourne: 'X', 'O', 'draw', ou None (partie en cours)
    """
    # Lignes gagnantes (8 combinaisons possibles)
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    for combo in win_combinations:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]  # 'X' ou 'O' gagne
    
    # Vérifier si match nul (plateau plein)
    if all(cell is not None for cell in board):
        return 'draw'
    
    return None  # Partie en cours


def get_valid_moves(board):
    """
    Retourne la liste des coups valides (cases vides).
    """
    return [i for i in range(9) if board[i] is None]


def is_terminal(board):
    """
    Vérifie si la partie est terminée.
    """
    return check_winner(board) is not None


def make_move(board, position, player):
    """
    Joue un coup et retourne un NOUVEAU plateau (ne modifie pas l'original).
    """
    new_board = board.copy()
    new_board[position] = player
    return new_board


def current_player(board):
    """
    Détermine à qui c'est le tour de jouer.
    X commence toujours en premier.
    """
    x_count = sum(1 for cell in board if cell == 'X')
    o_count = sum(1 for cell in board if cell == 'O')
    
    if x_count == o_count:
        return 'X'
    else:
        return 'O'