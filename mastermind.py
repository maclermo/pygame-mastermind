import os
import pygame
import sys

from helpers import Utils
from models import PlayPegColors

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DIR_RES = os.path.join(BASE_DIR, "assets")

WIDTH = 325
HEIGHT = 739
FPS = 30

PLAY_PEGS_THICKNESS = 9
SCORE_PEGS_THICKNESS = 4


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.running = True

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load(os.path.join(DIR_RES, "board.png")).convert()
        self.left_arrow = pygame.image.load(os.path.join(DIR_RES, "left-arrow.png")).convert_alpha()
        self.smiling_face = pygame.image.load(os.path.join(DIR_RES, "thumbs-up.png")).convert_alpha()
        self.sad_face = pygame.image.load(os.path.join(DIR_RES, "thumbs-down.png")).convert_alpha()
        self.open_sans_16 = pygame.font.Font(os.path.join(DIR_RES, "OpenSans-Regular.ttf"), 16)
        self.text_next = self.open_sans_16.render("OK", True, (255, 255, 255))

        self.board = Utils.generate_board()
        self.board_coords = Utils.generate_board_coords()
        self.starting_colors = Utils.starting_colors()
        self.winning_pegs = Utils.generate_winning_pegs_coords()

        self.play_count = 1
        self.game_mode = "peg_select"
        self.won = False
        self.lost = False

        pygame.display.set_caption("MasterMind - The Game")

        while True:
            if Utils.is_winning(self.board[self.play_count - 2]["score"]):
                pygame.display.set_caption("MasterMind - The Game (You Won!)")

                self.won = True
                self.running = False
            elif Utils.is_losing(self.play_count):
                pygame.display.set_caption("MasterMind - The Game (You Lost!)")

                self.lost = True
                self.running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if self.running:
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_pos_x = pygame.mouse.get_pos()[0]
                        mouse_pos_y = pygame.mouse.get_pos()[1]

                        targeted_circles = [
                            self.board_coords[self.play_count - 1]["play"].index(c)
                            for c in self.board_coords[self.play_count - 1]["play"]
                            if mouse_pos_x >= c[0] - PLAY_PEGS_THICKNESS
                            and mouse_pos_x <= c[0] + PLAY_PEGS_THICKNESS
                            and mouse_pos_y >= c[1] - PLAY_PEGS_THICKNESS
                            and mouse_pos_y <= c[1] + PLAY_PEGS_THICKNESS
                            and self.game_mode == "peg_select"
                        ]

                        if self.game_mode == "peg_select" and len(targeted_circles) == 1:
                            self.selected_peg = targeted_circles[0]
                            self.game_mode = "color_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                targeted_circles[0],
                                PlayPegColors.SELECT,
                            )
                        elif self.game_mode == "color_select" and len(targeted_circles) == 1:
                            self.selected_peg = targeted_circles[0]
                            self.game_mode = "peg_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                targeted_circles[0],
                                PlayPegColors.EMPTY,
                            )
                        elif (
                            self.game_mode == "peg_select"
                            and mouse_pos_x >= 230
                            and mouse_pos_x <= 255
                            and mouse_pos_y >= 585
                            and mouse_pos_y <= 605
                        ):
                            colors_filled = [
                                c for c in self.board[self.play_count - 1]["play"] if c is not PlayPegColors.EMPTY
                            ]
                            if len(colors_filled) == 5:
                                score = Utils.row_score(self.starting_colors, colors_filled)

                                Utils.update_board_score_pegs(self.board, self.play_count, score)

                                self.play_count += 1
                        elif (
                            self.game_mode == "color_select"
                            and mouse_pos_x >= 25
                            and mouse_pos_x <= 45
                            and mouse_pos_y >= 585
                            and mouse_pos_y <= 605
                        ):
                            self.game_mode = "peg_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                self.selected_peg,
                                PlayPegColors.WHITE,
                            )
                        elif (
                            self.game_mode == "color_select"
                            and mouse_pos_x >= 50
                            and mouse_pos_x <= 70
                            and mouse_pos_y >= 585
                            and mouse_pos_y <= 605
                        ):
                            self.game_mode = "peg_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                self.selected_peg,
                                PlayPegColors.YELLOW,
                            )
                        elif (
                            self.game_mode == "color_select"
                            and mouse_pos_x >= 75
                            and mouse_pos_x <= 95
                            and mouse_pos_y >= 585
                            and mouse_pos_y <= 605
                        ):
                            self.game_mode = "peg_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                self.selected_peg,
                                PlayPegColors.ORANGE,
                            )
                        elif (
                            self.game_mode == "color_select"
                            and mouse_pos_x >= 100
                            and mouse_pos_x <= 120
                            and mouse_pos_y >= 585
                            and mouse_pos_y <= 605
                        ):
                            self.game_mode = "peg_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                self.selected_peg,
                                PlayPegColors.RED,
                            )
                        elif (
                            self.game_mode == "color_select"
                            and mouse_pos_x >= 125
                            and mouse_pos_x <= 145
                            and mouse_pos_y >= 585
                            and mouse_pos_y <= 605
                        ):
                            self.game_mode = "peg_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                self.selected_peg,
                                PlayPegColors.GREEN,
                            )
                        elif (
                            self.game_mode == "color_select"
                            and mouse_pos_x >= 150
                            and mouse_pos_x <= 170
                            and mouse_pos_y >= 585
                            and mouse_pos_y <= 605
                        ):
                            self.game_mode = "peg_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                self.selected_peg,
                                PlayPegColors.BLUE,
                            )
                        elif (
                            self.game_mode == "color_select"
                            and mouse_pos_x >= 175
                            and mouse_pos_x <= 195
                            and mouse_pos_y >= 585
                            and mouse_pos_y <= 605
                        ):
                            self.game_mode = "peg_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                self.selected_peg,
                                PlayPegColors.PURPLE,
                            )
                        elif (
                            self.game_mode == "color_select"
                            and mouse_pos_x >= 200
                            and mouse_pos_x <= 220
                            and mouse_pos_y >= 585
                            and mouse_pos_y <= 605
                        ):
                            self.game_mode = "peg_select"

                            Utils.set_peg_color(
                                self.board,
                                self.play_count,
                                self.selected_peg,
                                PlayPegColors.BLACK,
                            )

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.text_next, (230, 582))

            pygame.draw.rect(self.screen, Utils.get_peg_color(PlayPegColors.WHITE), (25, 584, 20, 20))
            pygame.draw.rect(
                self.screen,
                Utils.get_peg_color(PlayPegColors.YELLOW),
                (50, 584, 20, 20),
            )
            pygame.draw.rect(
                self.screen,
                Utils.get_peg_color(PlayPegColors.ORANGE),
                (75, 584, 20, 20),
            )
            pygame.draw.rect(self.screen, Utils.get_peg_color(PlayPegColors.RED), (100, 584, 20, 20))
            pygame.draw.rect(
                self.screen,
                Utils.get_peg_color(PlayPegColors.GREEN),
                (125, 584, 20, 20),
            )
            pygame.draw.rect(self.screen, Utils.get_peg_color(PlayPegColors.BLUE), (150, 584, 20, 20))
            pygame.draw.rect(
                self.screen,
                Utils.get_peg_color(PlayPegColors.PURPLE),
                (175, 584, 20, 20),
            )
            pygame.draw.rect(
                self.screen,
                Utils.get_peg_color(PlayPegColors.BLACK),
                (200, 584, 20, 20),
            )

            pygame.display.set_caption("MasterMind - The Game (Round {})".format(self.play_count))

            if not self.won:
                self.screen.blit(self.left_arrow, Utils.move_arrow_to_row(self.play_count))

            for row in range(12):
                for peg in range(5):
                    pygame.draw.circle(
                        self.screen,
                        Utils.get_peg_color(self.board[row]["play"][peg]),
                        self.board_coords[row]["play"][peg],
                        PLAY_PEGS_THICKNESS,
                    )

                for peg in range(5):
                    pygame.draw.circle(
                        self.screen,
                        Utils.get_peg_color(self.board[row]["score"][peg]),
                        self.board_coords[row]["score"][peg],
                        SCORE_PEGS_THICKNESS,
                    )

            if self.won:
                self.screen.blit(self.smiling_face, (2, 257))
            if self.lost:
                self.screen.blit(self.sad_face, (2, 239))
                for row in range(5):
                    pygame.draw.circle(
                        self.screen,
                        Utils.get_peg_color(self.starting_colors[row]),
                        self.winning_pegs[row],
                        PLAY_PEGS_THICKNESS,
                    )

            pygame.display.flip()
            self.clock.tick(FPS)


game = Game()
