import pandas as pd
import numpy as np
import os
from game_logic import check_winner, get_valid_moves, make_move, current_player, is_terminal

# Cache for minimax results: key = tuple(board), value = score (1, -1, 0)
minimax_cache = {}

def minimax_alpha_beta(board, alpha, beta, is_maximizing):
    """
    Minimax with alpha-beta pruning and memoization.
    Returns 1 if X wins, -1 if O wins, 0 for draw under perfect play.
    """
    board_tuple = tuple(board)  # hashable representation for caching

    # Check cache first
    if board_tuple in minimax_cache:
        return minimax_cache[board_tuple]

    # Check terminal state
    result = check_winner(board)
    if result == 'X':
        minimax_cache[board_tuple] = 1
        return 1
    elif result == 'O':
        minimax_cache[board_tuple] = -1
        return -1
    elif result == 'draw':
        minimax_cache[board_tuple] = 0
        return 0

    # Maximizing player (X)
    if is_maximizing:
        max_eval = -float('inf')
        for move in get_valid_moves(board):
            new_board = make_move(board, move, 'X')
            eval = minimax_alpha_beta(new_board, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        minimax_cache[board_tuple] = max_eval
        return max_eval

    # Minimizing player (O)
    else:
        min_eval = float('inf')
        for move in get_valid_moves(board):
            new_board = make_move(board, move, 'O')
            eval = minimax_alpha_beta(new_board, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        minimax_cache[board_tuple] = min_eval
        return min_eval

def encode_board(board):
    """Convert board to binary features: for each cell, two flags (X present, O present)."""
    features = []
    for i in range(9):
        features.append(1 if board[i] == 'X' else 0)
        features.append(1 if board[i] == 'O' else 0)
    return features

def generate_all_states(board, visited, data_list):
    """
    Depth-first generation of all distinct board states.
    visited is a set of tuple(board) to avoid processing the same state twice.
    data_list accumulates features and targets for states where it is X's turn.
    """
    board_tuple = tuple(board)
    if board_tuple in visited:
        return          # already processed
    visited.add(board_tuple)

    player = current_player(board)

    # For states where it's X's turn, evaluate and add to dataset
    if player == 'X':
        score = minimax_alpha_beta(board, -float('inf'), float('inf'), True)
        x_wins = 1 if score == 1 else 0
        is_draw = 1 if score == 0 else 0
        features = encode_board(board)
        data_list.append(features + [x_wins, is_draw])

    # Recurse on all legal moves
    for move in get_valid_moves(board):
        new_board = make_move(board, move, player)
        generate_all_states(new_board, visited, data_list)

if __name__ == "__main__":
    print("Creating dataset...")

    data_list = []
    empty_board = [None] * 9
    visited = set()                # track processed boards

    # Generate all distinct board states
    generate_all_states(empty_board, visited, data_list)

    # Build column names: for each cell (0..8) two features (x and o)
    cols = []
    for i in range(9):
        cols.append(f'c{i}_x')
        cols.append(f'c{i}_o')
    cols.append('x_wins')
    cols.append('is_draw')

    df = pd.DataFrame(data_list, columns=cols)

    os.makedirs('ressources', exist_ok=True)
    df.to_csv('ressources/dataset.csv', index=False)

    print(f"Done. Dataset size: {len(df)} rows.")