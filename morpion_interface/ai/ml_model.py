import os
import pickle

class TicTacToeMLModel:
    def __init__(self, model_dir=None):
        if model_dir is None:
            # Résoudre le chemin relatif : remonter de ai/ -> morpion_interface/ -> msiminds/ puis modèles
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            self.model_dir = os.path.join(base_dir, "models")
        else:
            self.model_dir = model_dir
            
        self.model_x_wins = None
        self.model_is_draw = None
        self.load_model()

    def train(self):
        # Cette fonction reste prévue pour du réentraînement via les carnets ( notebooks )
        pass

    def load_model(self):
        try:
            x_wins_path = os.path.join(self.model_dir, "best_model_x_wins.pkl")
            is_draw_path = os.path.join(self.model_dir, "best_model_is_draw.pkl")
            
            if os.path.exists(x_wins_path):
                with open(x_wins_path, "rb") as f:
                    self.model_x_wins = pickle.load(f)
            
            if os.path.exists(is_draw_path):
                with open(is_draw_path, "rb") as f:
                    self.model_is_draw = pickle.load(f)
                    
            print(f"Modèles ML chargés depuis {self.model_dir} !")
        except Exception as e:
            print(f"Erreur lors du chargement des modèles ML : {e}")

    def save_model(self):
        pass

    def _board_to_features(self, board_state):
        try:
            import pandas as pd
            features = {}
            for i in range(9):
                features[f'c{i}_x'] = 1 if board_state[i] == "X" else 0
                features[f'c{i}_o'] = 1 if board_state[i] == "O" else 0
            
            # Ordonner selon features_cols.pkl (c0_x, c0_o, c1_x, ...)
            ordered_cols = []
            for i in range(9):
                ordered_cols.extend([f'c{i}_x', f'c{i}_o'])
                
            df = pd.DataFrame([features])
            return df[ordered_cols]
        except ImportError:
            return None

    def predict_move(self, board, ai_letter):
        """ Évalue toutes les cases vides via les classifieurs ML et retourne le meilleur coup. """
        if not self.model_x_wins:
            return self._fallback_move(board)

        best_move = None
        best_score = -float('inf')
        
        for move in board.available_moves():
            board.make_move(move, ai_letter)
            features = self._board_to_features(board.state)
            
            if features is None:
                board.state[move] = " "
                board.current_winner = None
                return self._fallback_move(board)
            
            # Prédiction de la victoire de X
            try:
                if hasattr(self.model_x_wins, "predict_proba"):
                    probs_x = self.model_x_wins.predict_proba(features)
                    p_x_wins = probs_x[0][1] if probs_x.shape[1] > 1 else probs_x[0][0]
                else:
                    p_x_wins = float(self.model_x_wins.predict(features)[0])
            except:
                p_x_wins = 0

            # Prédiction du match nul
            try:
                if self.model_is_draw and hasattr(self.model_is_draw, "predict_proba"):
                    probs_d = self.model_is_draw.predict_proba(features)
                    p_draw = probs_d[0][1] if probs_d.shape[1] > 1 else probs_d[0][0]
                else:
                    p_draw = float(self.model_is_draw.predict(features)[0]) if self.model_is_draw else 0
            except:
                p_draw = 0

            # Score heuristique ML 
            if ai_letter == "X":
                # Le but de X est de maximiser la P(X_wins) et secondairement P(Match nul)
                score = p_x_wins + (p_draw * 0.1)
            else:
                # Le but de O est de minimiser P(X_wins) et contourner le nul si possible
                # (P(o_wins) = 1 - p_x_wins - p_draw) => on minimise (p_x_wins + p_draw)
                score = -(p_x_wins + p_draw)
                
            # Annuler le coup pour continuer la simulation
            board.state[move] = " "
            board.current_winner = None
            
            if score > best_score:
                best_score = score
                best_move = move
                
        # Retourne le meilleur coup s'il l'a trouvé
        if best_move is not None:
            return best_move
            
        return self._fallback_move(board)
        
    def _fallback_move(self, board):
        import random
        moves = board.available_moves()
        return random.choice(moves) if moves else None
