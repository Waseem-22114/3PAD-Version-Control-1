'''
# Author: Waseem Patel
# Date: 09/06/2026
# Purpose: To create a Math quiz / game to help students have fun doing math in an interactive way
'''

# Import tkinter and ttk for GUI creation.
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

# These are the dimensions, possible colours, fonts, etc of the entire GUI
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 585

BACKGROUND_COLOUR = "white"
TEXT_COLOUR = "black"
BUTTON_COLOUR = "white"
BUTTON_HOVER_COLOUR = "#f2f2f2"

TITLE_FONT = ("Arial", 28, "bold")
BUTTON_FONT = ("Arial", 22)

BUTTON_WIDTH = 255
BUTTON_HEIGHT = 68

CENTRE_X = WINDOW_WIDTH // 2
BUTTON_X = CENTRE_X - BUTTON_WIDTH // 2


class MathQuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Menu")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(
            self.root,
            bg="#87CEEB",
            highlightbackground="black",
            highlightthickness=2
        )
        self.main_frame.pack(fill="both", expand=True)

        self.show_main_menu()

   