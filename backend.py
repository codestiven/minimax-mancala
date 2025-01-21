from typing import Tuple
import copy


def move_piece(board: dict, tile: int, turn: str) -> Tuple[dict, bool]:

    pieces = board[turn][tile]
    board[turn][tile] = 0
    location = turn
    go_again = False

    # 2. Moviéndose en sentido contrario a las agujas del reloj, el jugador deposita una de las piedras en cada casilla hasta que se acaben las fichas.
    while pieces > 0:
        go_again = False
        pieces -= 1
        tile += 1

        if tile < len(board[location]):
            board[location][tile] += 1
            continue

        # 3. Si se topa con su propio Mancala (almacén), deposite una ficha en él.
        # Si te topas con el Mancala de tu adversario, sáltalo y continúa avanzando a la siguiente tronera.
        # 4. Si la última pieza que depositas está en tu propia Mancala, haces otro turno.
        if location == turn:
            board[f"{turn}_score"] += 1
            go_again = True
        else:
            pieces += 1

        location = "bottom" if location == "top" else "top"
        tile = -1

    inverse_location = "bottom" if location == "top" else "top"
    if (
        (location == turn)
        and (board[location][tile] == 1)
        and (board[inverse_location][len(board[inverse_location]) - 1 - tile] != 0)
    ):
        board[f"{turn}_score"] += (
            1 + board[inverse_location][len(board[inverse_location]) - 1 - tile]
        )
        board[location][tile] = 0
        board[inverse_location][len(board[inverse_location]) - 1 - tile] = 0

    # 7. El juego termina cuando las seis casillas de un lado del tablero Mancala están vacías.
    # 8. El jugador que aún tenga fichas en su lado del tablero cuando termine la partida captura todas esas fichas.
    if (not any(board["top"])) or (not any(board["bottom"])):
        board["top_score"] += sum(board["top"])
        board["bottom_score"] += sum(board["bottom"])

        board["top"] = [0] * len(board["top"])
        board["bottom"] = [0] * len(board["bottom"])

        go_again = False

    return board, go_again


def is_viable_move(board: dict, tile: int, turn: str) -> bool:

    if tile >= len(board[turn]) or tile < 0:
        return False
    return bool(board[turn][tile])



#heuristicas

def Valor_de_los_almacenes_y_casillas(board, ai_side):
    # Valor de los almacenes y casillas.
    # Evalúa el valor de los almacenes y las casillas del jugador AI en comparación con el oponente.
    # board: El estado actual del tablero.
    # ai_side: El lado del jugador AI.
    ai_store_value = sum(board[ai_side])
    opponent_store_value = sum(board["top" if ai_side == "bottom" else "bottom"])
    ai_board_value = sum(board[ai_side]) + sum(board[ai_side])
    return ai_store_value - opponent_store_value + ai_board_value



def Semillas_capturadas(board, ai_side):
    # Semillas capturadas.
    # Calcula el número de semillas capturadas por el jugador AI en comparación con el oponente.
    # board: El estado actual del tablero.
    # ai_side: El lado del jugador AI.
    ai_captured_seeds = board[ai_side + "_score"]
    opponent_captured_seeds = board["top_score" if ai_side == "bottom" else "bottom_score"]
    return ai_captured_seeds - opponent_captured_seeds


def Movimientos_válidos(board, ai_side):
    # Movimientos válidos.
    # Cuenta la cantidad de movimientos válidos disponibles para el jugador AI en comparación con el oponente.
    # board: El estado actual del tablero.
    # ai_side: El lado del jugador AI.
    ai_valid_moves = sum(1 for move in range(6) if board[ai_side][move] > 0)
    opponent_valid_moves = sum(1 for move in range(6) if board["top" if ai_side == "bottom" else "bottom"][move] > 0)
    return ai_valid_moves - opponent_valid_moves



def Movimientos_hacia_el_almacén(board, ai_side):
    # Movimientos hacia el almacén.
    # Calcula la cantidad de movimientos que permiten que el jugador AI mueva una semilla hacia su almacén en comparación con el oponente.
    # board: El estado actual del tablero.
    # ai_side: El lado del jugador AI.
    ai_moves_to_store = sum(1 for move in range(6) if (move + board[ai_side][move]) % 13 == 6)
    opponent_moves_to_store = sum(1 for move in range(6) if (move + board["top" if ai_side == "bottom" else "bottom"][move]) % 13 == 6)
    return ai_moves_to_store - opponent_moves_to_store


def Distancia_desde_el_almacén(board, ai_side):
    # Distancia desde el almacén.
    # Calcula la distancia promedio de las casillas con semillas desde el almacén del jugador AI en comparación con el oponente.
    # board: El estado actual del tablero.
    # ai_side: El lado del jugador AI.
    ai_distance_from_store = sum(move + 1 for move in range(6) if board[ai_side][move] > 0)
    opponent_distance_from_store = sum(move + 1 for move in range(6) if board["top" if ai_side == "bottom" else "bottom"][move] > 0)
    return opponent_distance_from_store - ai_distance_from_store


def evaluate(board, ai_side):
       # Función de evaluación.
    # Combina los valores de las cinco heurísticas para obtener una puntuación general que representa la "bondad" del estado actual del tablero para el jugador AI.
    # board: El estado actual del tablero.
    # ai_side: El lado del jugador AI.
    return (
        0.2 * Valor_de_los_almacenes_y_casillas(board, ai_side) +
        0.2 * Semillas_capturadas(board, ai_side) +
        0.2 * Movimientos_válidos(board, ai_side) +
        0.2 * Movimientos_hacia_el_almacén(board, ai_side) +
        0.2 * Distancia_desde_el_almacén(board, ai_side)
    )

from typing import Tuple
import copy

def minimax_mancala(board, ai_side, turn, depth) -> Tuple[int, int]:
    AI = ai_side
    PLAYER = "bottom" if AI == "top" else "top"
    best_move = -1

    def alphabeta(board, turn, depth, alpha, beta):
        nonlocal best_move

        if (not any(board["top"])) or (not any(board["bottom"])) or depth <= 0:
            return evaluate(board, AI), best_move

        if AI == turn:
            best_score = float("-inf")
            possible_moves = [
                move for move in range(len(board[AI])) if is_viable_move(board, move, AI)
            ]

            for move in possible_moves:
                board_copy = copy.deepcopy(board)
                board_copy, go_again = move_piece(board_copy, move, turn)

                if go_again:
                    points, _ = alphabeta(board_copy, AI, depth, alpha, beta)
                else:
                    points, _ = alphabeta(board_copy, PLAYER, depth - 1, alpha, beta)

                if points > best_score:
                    best_move = move
                    best_score = points

                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break

            return best_score, best_move

        elif PLAYER == turn:
            best_score = float("inf")
            possible_moves = [
                move
                for move in range(len(board[PLAYER]))
                if is_viable_move(board, move, PLAYER)
            ]

            for move in possible_moves:
                board_copy = copy.deepcopy(board)
                board_copy, go_again = move_piece(board_copy, move, turn)

                if go_again:
                    points, _ = alphabeta(board_copy, PLAYER, depth, alpha, beta)
                else:
                    points, _ = alphabeta(board_copy, AI, depth - 1, alpha, beta)

                if points < best_score:
                    best_move = move
                    best_score = points

                beta = min(beta, best_score)
                if beta <= alpha:
                    break

            return best_score, best_move

    return alphabeta(board, turn, depth, float("-inf"), float("inf"))





