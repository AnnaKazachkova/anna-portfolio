"""Earlier version: the button jumps to a random spot on every click and
stops moving after 5 clicks."""
import random

import customtkinter as ctk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
click_count = 0


def move_button():
    global click_count
    click_count += 1

    if click_count >= 5:
        button.configure(text=f"Stopped at {click_count} clicks!")
    else:
        button.configure(text=f"Clicks: {click_count}")
        random_x = random.randint(20, 260)
        random_y = random.randint(20, 340)
        button.place(x=random_x, y=random_y)


button = ctk.CTkButton(app, text="Click me!", text_color="black",
                       fg_color="pink", command=move_button)
button.place(x=130, y=180)

app.mainloop()
