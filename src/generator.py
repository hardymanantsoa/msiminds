import pandas as pd
import numpy as np
import os
from game_logic import check_winner, get_valid_moves, make_move, current_player, is_terminal

# Minimax && alpha-beta 
def minimax_alpha_beta(board, alpha, beta, is_maximizing):
    
    # Check game result
    result = check_winner(board)
    
    # Terminal states
    if result == 'X':
        return 1
    elif result == 'O':
        return -1
    elif result == 'draw':
        return 0
    
    # Max player (X)
    if is_maximizing:
        max_eval = -float('inf')
        
        for move in get_valid_moves(board):
            new_board = make_move(board, move, 'X')
            eval = minimax_alpha_beta(new_board, alpha, beta, False)
            
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            
            # Prune
            if beta <= alpha:
                break
                
        return max_eval
    
    # Min player (O)
    else:
        min_eval = float('inf')
        
        for move in get_valid_moves(board):
            new_board = make_move(board, move, 'O')
            eval = minimax_alpha_beta(new_board, alpha, beta, True)
            
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            
            # Prune
            if beta <= alpha:
                break
                
        return min_eval


# Encode board
def encode_board(board):
    
    features = []
    
    for i in range(9):
        # X position
        features.append(1 if board[i] == 'X' else 0)
        # O position
        features.append(1 if board[i] == 'O' else 0)
        
    return features


# Generate states
def generate_all_states(board, data_list):
    
    # Stop if game ends
    if is_terminal(board):
        return
    
    player = current_player(board)
    
    # Save only X turn
    if player == 'X':
        score = minimax_alpha_beta(board, -float('inf'), float('inf'), True)
        
        x_wins = 1 if score == 1 else 0
        is_draw = 1 if score == 0 else 0
        
        features = encode_board(board)
        data_list.append(features + [x_wins, is_draw])
    
    # Explore moves
    for move in get_valid_moves(board):
        new_board = make_move(board, move, player)
        generate_all_states(new_board, data_list)


# Main
if __name__ == "__main__":
    
    print("Creating dataset...")
    
    data_list = []
    empty_board = [None] * 9
    
    # Generate all states
    generate_all_states(empty_board, data_list)
    
    # Columns
    cols = []
    for i in range(9):
        cols.append(f'c{i}_x')
        cols.append(f'c{i}_o')
    
    cols.append('x_wins')
    cols.append('is_draw')
    
    # DataFrame
    df = pd.DataFrame(data_list, columns=cols)
    
    # Save file
    os.makedirs('ressources', exist_ok=True)
    df.to_csv('ressources/dataset.csv', index=False)
    
    print("Done")