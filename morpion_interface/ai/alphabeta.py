import math
import random

AI_PLAYER = "O"
HUMAN_PLAYER = "X"

def get_best_move(state, player, difficulty):
    global AI_PLAYER, HUMAN_PLAYER
    AI_PLAYER = player
    HUMAN_PLAYER = "O" if player == "X" else "X"
    
    if difficulty == "Facile":
        moves = state.available_moves()
        if moves:
            return random.choice(moves)
        return None
        
    depth_limit = 2 if difficulty == "Moyen" else 9
    
    # Pour démarrer rapidement sur un plateau vide
    if len(state.available_moves()) == 9:
        return random.choice([0, 2, 4, 6, 8])
        
    best_move = None
    best_score = -math.inf
    
    for possible_move in state.available_moves():
        state.make_move(possible_move, AI_PLAYER)
        score = alphabeta(state, depth_limit - 1, -math.inf, math.inf, False)
        # Undo move
        state.state[possible_move] = " "
        state.current_winner = None
        
        if score > best_score:
            best_score = score
            best_move = possible_move
            
    return best_move

def alphabeta(board, depth, alpha, beta, maximizingPlayer):
    if board.current_winner:
        return 10 + depth if board.current_winner == AI_PLAYER else -10 - depth
    elif not board.empty_squares() or depth == 0:
        return 0

    if maximizingPlayer:
        max_eval = -math.inf
        for possible_move in board.available_moves():
            board.make_move(possible_move, AI_PLAYER)
            eval_score = alphabeta(board, depth - 1, alpha, beta, False)
            board.state[possible_move] = " "
            board.current_winner = None
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for possible_move in board.available_moves():
            board.make_move(possible_move, HUMAN_PLAYER)
            eval_score = alphabeta(board, depth - 1, alpha, beta, True)
            board.state[possible_move] = " "
            board.current_winner = None
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval
