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

Users_file="users.txt"

class MathQuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Menu")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(
            self.root,
            bg="#87CEEB",
            highlightbackground="black",
            highlightthickness=2
        )
        self.main_frame.pack(fill="both", expand=True)

        self.show_main_menu()

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_menu_button(self, text, y_position, command):
        button = tk.Button(
            self.main_frame,
            text=text,
            font=button_font,
            bg=button_colour,
            fg=text_colour,
            activebackground=button_hover_colour,
            activeforeground=text_colour,
            relief="solid",
            borderwidth=1,
            command=command
        )

        button.place(
            x=button_x,
            y=y_position,
            width=button_width,
            height=button_height
        )

        return button

# This is the displays the title of the GUI
    def show_main_menu(self):
        self.clear_screen()

        title_label = tk.Label(
            self.main_frame,
            text="Welcome to the Math Quiz",
            font=title_font,
            bg="#87CEEB",
            fg=text_colour
        )

        title_label.place(
            x=0,
            y=20,
            width=window_width,
            height=45
        )
        self.create_menu_button("Sign Up", 120, self.open_sign_up)
        self.create_menu_button("Log in", 230, self.open_log_in)
        self.create_menu_button("Leaderboard", 338, self.open_leaderboard)
        self.create_menu_button("Exit", 442, self.exit_program)

    def open_sign_up(self):
        self.clear_screen()

        title_label = tk.Label(
            self.main_frame,
            text="<Sign Up Below>",
            font=title_font,
            bg="#87CEEB",
            fg=text_colour,
            height=50
        )
        username_label = tk.Label(
            self.main_frame, text="Username:", fg="#000000", font=title_font, bg="#87CEEB"
        )
        password_label = tk.Label(
            self.main_frame, text="Password:", fg="#000000", font=title_font, bg="#87CEEB"
        )
        self.username_entry = tk.Entry(
            self.main_frame,
            font=("Arial", 18), relief="solid", borderwidth=1
        )
        self.password_entry = tk.Entry(
            self.main_frame,
            font=("Arial", 18), relief="solid", borderwidth=1, show="*"
        )
        button_signup = tk.Button(
            self.main_frame, text="Confirm", fg="#000000", font=title_font, bg="#87CEEB", relief="solid", borderwidth=1, command=self.save_signup
        )
        button_signup.place(x=375, y=400, width=250, height=50)
        self.password_entry.place(x=350, y=300, width=330, height=50)
        self.username_entry.place(x=350, y=200, width=330, height=50)
        password_label.place(x=100, y=300, width=200, height=50)
        username_label.place(x=100, y=200, width=200, height=50)
        title_label.place(x=0, y=40, width=window_width, height=50)

        self.create_back_button() 
    def save_signup(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        file = open("users.txt", "a")
        file.write(username + "," + password + "\n")
        file.close()

        messagebox.showinfo("Success", "Account saved.")
        self.show_main_menu()

    def open_log_in(self):
        self.clear_screen()

        title_label = tk.Label(
            self.main_frame,
            text="<Log In Below>",
            font=title_font,
            bg="#87CEEB",
            fg=text_colour,
            height=50
        )
        login_username_label = tk.Label(
            self.main_frame, text="Username:", fg="#000000", font=title_font, bg="#87CEEB"
        )
        login_password_label = tk.Label(
            self.main_frame, text="Password:", fg="#000000", font=title_font, bg="#87CEEB"
        )
        self.username_entry_login = tk.Entry(
            self.main_frame,
            font=("Arial", 18), relief="solid", borderwidth=1
        )
        self.password_entry_login = tk.Entry(
            self.main_frame,
            font=("Arial", 18), relief="solid", borderwidth=1, show="*"
        )
        button_login = tk.Button(
            self.main_frame, text="Confirm", fg="#000000", font=title_font, bg="#87CEEB", relief="solid", borderwidth=1, command=self.check_login
        )
        button_login.place(x=375, y=400, width=250, height=50)
        self.password_entry_login.place(x=350, y=300, width=330, height=50)
        self.username_entry_login.place(x=350, y=200, width=330, height=50)
        login_password_label.place(x=100, y=300, width=200, height=50)
        login_username_label.place(x=100, y=200, width=200, height=50)
        title_label.place(x=0, y=40, width=window_width, height=50)

        self.create_back_button()

    def check_login(self):
        username = self.username_entry_login.get().strip()
        password = self.password_entry_login.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        try:
            file = open("users.txt", "r")
            saved_users = file.readlines()
            file.close()
        except FileNotFoundError:
            messagebox.showerror("Error", "No accounts have been created yet.")
            return

        for user in saved_users:
            user = user.strip()

            if user == "":
                continue

            details = user.split(",")

            if len(details) == 2:
                saved_username = details[0]
                saved_password = details[1]

                if username == saved_username and password == saved_password:
                    messagebox.showinfo("Success", "Log in successful.")
                    self.show_main_menu()
                    return

        messagebox.showerror("Error", "Incorrect username or password.")

    def open_leaderboard(self):
        self.clear_screen()

        title_label = tk.Label(
            self.main_frame,
            text="<Leaderboard>",
            font=title_font,
            bg= "#87CEEB",
            fg=text_colour,
            height=50
        )

        title_label.place(x=0, y=40, width=window_width, height=50)

        self.create_back_button()

    def exit_program(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

# This creates the "Back" button allows for user to go back to the previous section
    def create_back_button(self):
        back_button = tk.Button(
            self.main_frame,
            text="Back",
            font=("Arial", 28, "bold"),
            bg="#FF0000",
            fg=text_colour,
            activebackground=button_hover_colour,
            relief="solid",
            borderwidth=1,
            command=self.show_main_menu
        )

        back_button.place(x=30, y=520, width=120, height=45)

# This allows for the "Exit" button to close the program when clicked
    def exit_program(self):
        self.root.destroy()

# This is the main function which allows the program to run
if __name__ == "__main__":
    app = MathQuizApp()
    app.run()