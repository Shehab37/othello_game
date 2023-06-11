import tkinter as tk
from tkinter import messagebox
import numpy as np
import math
import copy
import time
import winsound


class OthelloGUI:
    def __init__(self, master):
        self.master = master
        master.title("Othello Game")
        master.geometry("1200x720")
        # icon
        master.iconbitmap("icons/Othello_icon.ico")
        # master.config(bg="white")
        # create a frame for the game board on the left side
        self.board_frame = tk.Frame(master)
        self.board_frame.pack(side="left", padx=0, pady=10)

        # create a canvas for the game board
        self.canvas = tk.Canvas(self.board_frame, width=600, height=600)
        self.canvas.pack()

        # create a frame for the game controls on the right side
        self.controls_frame = tk.Frame(master)
        self.controls_frame.pack(side="left", padx=0, pady=0)

        # create buttons for game mode selection
        self.game_mode = tk.StringVar(value="human_vs_ai")
        self.ai_player = tk.IntVar(value=1)

        # create buttons for Human vs Human
        self.human_vs_human_button = tk.Button(
            self.controls_frame, text="Human vs Human", command=lambda: self.select_game_mode("human_vs_human"), width=15, height=2, bg="green")
        self.human_vs_human_button.grid(row=0, column=0, padx=10, pady=10)

        # create buttons for Human vs AI
        self.human_vs_ai_button = tk.Button(
            self.controls_frame, text="Human vs AI", command=lambda: self.select_game_mode("human_vs_ai"), width=15, height=2)
        self.human_vs_ai_button.grid(row=0, column=1, padx=10, pady=10)

        # AI color selection
        self.ai_as_white_button = tk.Button(
            self.controls_frame, text="AI as White", command=lambda: self.select_ai_player(1), width=10, height=1)
        self.ai_as_black_button = tk.Button(
            self.controls_frame, text="AI as Black", command=lambda: self.select_ai_player(2), width=10, height=1)
        self.ai_level_label = tk.Label(
            self.controls_frame, text="AI Player level:", width=15, height=2)
        self.ai_level_input = tk.Scale(
            self.controls_frame, from_=1, to=16, orient="horizontal", length=200)

        self.maxDuration_label = tk.Label(
            self.controls_frame, text="AI time limit", width=20, height=2)
        self.maxDuration_input = tk.Entry(self.controls_frame, width=15)
        self.maxDuration_input.insert(0, "0.2")

        # create a button for AI vs AI
        self.ai_vs_ai_button = tk.Button(
            self.controls_frame, text="AI vs AI", command=lambda: self.select_game_mode("ai_vs_ai"), width=15, height=2)
        self.ai_vs_ai_button.grid(row=0, column=2, padx=10, pady=10)

        # create a button to start the game
        self.start_button = tk.Button(
            self.controls_frame, text="START GAME", command=self.start_game, width=20, height=3, bg="blue", fg="white")
        self.start_button.grid(row=12, column=0, pady=50)

        # create a button to undo the last move
        self.undo_button = tk.Button(
            self.controls_frame, text="UNDO", command=self.undo, width=20, height=3, bg="orange")
        self.undo_button.grid(row=12, column=1, pady=50)

        # create labels for player scores and current player
        self.score_label1 = tk.Label(
            self.controls_frame, text="Black: 2", width=15, height=2, font=("Arial", 14))
        self.score_label1.grid(row=14, column=0, padx=10, pady=10)

        self.score_label2 = tk.Label(
            self.controls_frame, text="White: 2", width=15, height=2, font=("Arial", 14))
        self.score_label2.grid(row=14, column=1, padx=10, pady=10)

        self.current_player_label = tk.Label(
            self.controls_frame, text="Current Player: Black", width=20, height=2,
            # make the font in the middle of the label
            anchor="center", font=("Arial", 14))
        self.current_player_label.grid(row=13, column=0, padx=0, pady=10)

        self.ai_level_label.grid(row=8, column=0)
        self.ai_level_input.grid(row=8, column=1)
        self.maxDuration_label.grid(row=9, column=0)
        self.maxDuration_input.grid(row=9, column=1)
        self.ai_as_white_button.grid(row=10, column=0)
        self.ai_as_black_button.grid(row=10, column=1)
        self.game = OthelloGame()
        self.draw_board()
        self.gameStack = []
        self.storeGame()

        # make as if human vs human button was clicked
        self.select_game_mode("human_vs_human")

    def select_game_mode(self, mode):
        self.game_mode.set(mode)
        if mode == "human_vs_human":
            self.human_vs_human_button.config(bg="green")
            self.human_vs_ai_button.config(bg=self.master.cget("bg"))
            self.ai_vs_ai_button.config(bg=self.master.cget("bg"))

            self.ai_as_white_button.config(state="disabled")
            self.ai_as_black_button.config(state="disabled")
            self.ai_level_label.config(state="disabled")
            self.ai_level_input.config(state="disabled")
            self.maxDuration_label.config(state="disabled")
            self.maxDuration_input.config(state="disabled")
        elif mode == "human_vs_ai":
            self.human_vs_human_button.config(bg=self.master.cget("bg"))
            self.human_vs_ai_button.config(bg="green")
            self.ai_vs_ai_button.config(bg=self.master.cget("bg"))

            self.ai_as_white_button.config(state="normal")
            self.ai_as_black_button.config(state="normal")
            self.ai_level_label.config(state="normal")
            self.ai_level_input.config(state="normal")
            self.maxDuration_label.config(state="normal")
            self.maxDuration_input.config(state="normal")

        elif mode == "ai_vs_ai":
            self.human_vs_human_button.config(bg=self.master.cget("bg"))
            self.human_vs_ai_button.config(bg=self.master.cget("bg"))
            self.ai_vs_ai_button.config(bg="green")

            self.ai_as_white_button.config(state="disabled")
            self.ai_as_black_button.config(state="disabled")
            self.ai_level_label.config(state="normal")
            self.ai_level_input.config(state="normal")
            self.maxDuration_label.config(state="normal")
            self.maxDuration_input.config(state="normal")

    def select_ai_player(self, player):
        self.ai_player.set(player)
        if player == 1:
            self.ai_as_white_button.config(bg="green")
            self.ai_as_black_button.config(bg=self.master.cget("bg"))
        elif player == 2:
            self.ai_as_white_button.config(bg=self.master.cget("bg"))
            self.ai_as_black_button.config(bg="green")

    def storeGame(self):
        Bcopy = self.game.get_Bcopy()
        self.gameStack.append(Bcopy)

    def undo(self, event=None):
        if len(self.gameStack) > 1:
            self.gameStack.pop()
            Bcopy = copy.deepcopy(self.gameStack[-1])
            self.game = OthelloGame()
            self.game.set_Bcopy(Bcopy)
            self.update_scores()  # update player scores
            self.draw_board()  # draw the board
            self.highlight_valid_squares()  # highlight valid squares after each move
