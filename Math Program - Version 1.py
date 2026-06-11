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
window_width = 900
window_height = 585
background_colour = "white"
text_colour = "black"
button_colour = "white"
button_hover_colour = "#f2f2f2"
title_font = ("Arial", 28, "bold")
button_font = ("Arial", 22)
button_width = 255
button_height = 68
centre_x = window_width // 2
button_x = centre_x - button_width // 2

class MathQuizApp:
    def __init__(self):
   