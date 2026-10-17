"""Catch Me If You Can: a button that dodges the cursor.

Hovering over the button moves it to a random spot. After 10 escapes it
"gives up", the hover binding is removed and it can finally be clicked.
"""
import random

import customtkinter as ctk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Catch Me If You Can!")

escape_count = 0


def move_button(event):
    global escape_count
    escape_count += 1

    if escape_count >= 10:
        button.configure(text=f"Fine, I give up! at ({escape_count})")
        # Unbind the hover event so the user can finally click it
        button.unbind("<Enter>")
    else:
        button.configure(text=f"Loser : {escape_count}x times!")
        random_x = random.randint(20, 260)
        random_y = random.randint(20, 340)
        button.place(x=random_x, y=random_y)


button = ctk.CTkButton(app, text="Click me!", text_color="black", fg_color="pink")
button.place(x=130, y=180)

# Bind the hover / mouse-enter event to the move function
button.bind("<Enter>", move_button)

app.mainloop()
