from models import PlayPegColors, ScorePegColors
from random import randrange


class Utils:
    def starting_colors():
        starting_colors = []

        for _ in range(5):
            starting_colors.append(randrange(8) + 1)

        starting_colors = [PlayPegColors(color) for color in starting_colors]

        return starting_colors

    def row_score(starting_colors, row_colors):
        partial_matches = 0
        exact_matches = 0

        starting_colors_copy = starting_colors.copy()
        row_colors_copy = row_colors.copy()

        for color_index in range(5):
            if row_colors[color_index] is starting_colors[color_index]:
                exact_matches += 1
                row_colors_copy[color_index] = -1
                starting_colors_copy[color_index] = -2

        for color_index in range(5):
            if starting_colors_copy[color_index] in row_colors_copy:
                partial_matches += 1
                row_colors_copy[color_index] = -1
                starting_colors_copy[color_index] = -2

        black_pegs = [ScorePegColors.BLACK for _ in range(exact_matches)]
        white_pegs = [ScorePegColors.WHITE for _ in range(partial_matches)]

        return black_pegs + white_pegs

    def set_peg_color(data, play_count, peg, color):
        data[play_count - 1]["play"][peg] = color

    def get_peg_color(color):
        if color.name == "EMPTY":
            return (147, 93, 88)
        if color.name == "WHITE":
            return (255, 255, 255)
        if color.name == "YELLOW":
            return (255, 255, 0)
        if color.name == "ORANGE":
            return (255, 165, 0)
        if color.name == "RED":
            return (255, 0, 0)
        if color.name == "GREEN":
            return (0, 128, 0)
        if color.name == "BLUE":
            return (30, 144, 255)
        if color.name == "PURPLE":
            return (178, 102, 255)
        if color.name == "BLACK":
            return (0, 0, 0)
        if color.name == "SELECT":
            return (197, 143, 138)

    def is_winning(row):
        black_pegs = [peg for peg in row if peg is ScorePegColors.BLACK]

        if len(black_pegs) == 5:
            return True

        return False

    def is_losing(play_count):
        if play_count == 13:
            return True

        return False

    def update_board_score_pegs(board, play_count, score_pegs):
        for i in range(len(score_pegs)):
            board[play_count - 1]["score"][i] = score_pegs[i]

    def generate_board():
        board = []

        for _ in range(13):
            row_data = {
                "play": [PlayPegColors.EMPTY for _ in range(5)],
                "score": [ScorePegColors.EMPTY for _ in range(5)],
            }
            board.append(row_data)

        return board

    def move_arrow_to_row(current_turn):
        if current_turn == 1:
            return (278, 537)
        if current_turn == 2:
            return (278, 503)
        if current_turn == 3:
            return (278, 471)
        if current_turn == 4:
            return (278, 438)
        if current_turn == 5:
            return (278, 405)
        if current_turn == 6:
            return (278, 372)
        if current_turn == 7:
            return (278, 339)
        if current_turn == 8:
            return (278, 305)
        if current_turn == 9:
            return (278, 272)
        if current_turn == 10:
            return (278, 239)
        if current_turn == 11:
            return (278, 206)
        if current_turn == 12:
            return (278, 172)
        if current_turn == 13:
            return (-500, -500)

    def generate_winning_pegs_coords():
        winning_pegs = [(142, 130), (172, 130), (201, 130), (231, 130), (261, 130)]

        return winning_pegs

    def generate_board_coords():
        board_coords = [
            {
                "play": [
                    (142, 545),
                    (172, 545),
                    (201, 545),
                    (231, 545),
                    (261, 545),
                ],
                "score": [
                    (46, 546),
                    (62, 546),
                    (79, 546),
                    (96, 546),
                    (112, 546),
                ],
            },
            {
                "play": [
                    (142, 512),
                    (172, 512),
                    (201, 512),
                    (231, 512),
                    (261, 512),
                ],
                "score": [
                    (46, 512),
                    (62, 512),
                    (79, 512),
                    (96, 512),
                    (112, 512),
                ],
            },
            {
                "play": [
                    (142, 480),
                    (172, 480),
                    (201, 480),
                    (231, 480),
                    (261, 480),
                ],
                "score": [
                    (46, 480),
                    (62, 480),
                    (79, 480),
                    (96, 480),
                    (112, 480),
                ],
            },
            {
                "play": [
                    (142, 447),
                    (172, 447),
                    (201, 447),
                    (231, 447),
                    (261, 447),
                ],
                "score": [
                    (46, 447),
                    (62, 447),
                    (79, 447),
                    (96, 447),
                    (112, 447),
                ],
            },
            {
                "play": [
                    (142, 414),
                    (172, 414),
                    (201, 414),
                    (231, 414),
                    (261, 414),
                ],
                "score": [
                    (46, 414),
                    (62, 414),
                    (79, 414),
                    (96, 414),
                    (112, 414),
                ],
            },
            {
                "play": [
                    (142, 381),
                    (172, 381),
                    (201, 381),
                    (231, 381),
                    (261, 381),
                ],
                "score": [
                    (46, 381),
                    (62, 381),
                    (79, 381),
                    (96, 381),
                    (112, 381),
                ],
            },
            {
                "play": [
                    (142, 348),
                    (172, 348),
                    (201, 348),
                    (231, 348),
                    (261, 348),
                ],
                "score": [
                    (46, 348),
                    (62, 348),
                    (79, 348),
                    (96, 348),
                    (112, 348),
                ],
            },
            {
                "play": [
                    (142, 315),
                    (172, 315),
                    (201, 315),
                    (231, 315),
                    (261, 315),
                ],
                "score": [
                    (46, 315),
                    (62, 315),
                    (79, 315),
                    (96, 315),
                    (112, 315),
                ],
            },
            {
                "play": [
                    (142, 282),
                    (172, 282),
                    (201, 282),
                    (231, 282),
                    (261, 282),
                ],
                "score": [
                    (46, 282),
                    (62, 282),
                    (79, 282),
                    (96, 282),
                    (112, 282),
                ],
            },
            {
                "play": [
                    (142, 249),
                    (172, 249),
                    (201, 249),
                    (231, 249),
                    (261, 249),
                ],
                "score": [
                    (45, 249),
                    (61, 249),
                    (78, 249),
                    (95, 249),
                    (111, 249),
                ],
            },
            {
                "play": [
                    (142, 216),
                    (172, 216),
                    (201, 216),
                    (231, 216),
                    (261, 216),
                ],
                "score": [
                    (45, 215),
                    (61, 215),
                    (78, 215),
                    (95, 215),
                    (111, 215),
                ],
            },
            {
                "play": [
                    (142, 182),
                    (172, 182),
                    (201, 182),
                    (231, 182),
                    (261, 182),
                ],
                "score": [
                    (44, 181),
                    (60, 181),
                    (77, 181),
                    (94, 181),
                    (110, 181),
                ],
            },
        ]

        return board_coords
