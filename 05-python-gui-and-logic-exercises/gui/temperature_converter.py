"""Temperature converter (Fahrenheit <-> Celsius) built with CustomTkinter."""
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


def convert():
    try:
        temp = float(entry_temp.get())
        mode = mode_switch.get()

        if mode == "Fahrenheit to Celsius":
            celsius = (5 / 9) * (temp - 32)
            label_result.configure(text=f"The temperature is {celsius:.1f}C.")
        else:
            fahrenheit = (temp * 9 / 5) + 32
            label_result.configure(text=f"The temperature is {fahrenheit:.1f}F.")

    except ValueError:
        label_result.configure(text="Enter a valid number")


def update_labels(choice: str):
    if choice == "Fahrenheit to Celsius":
        label_prompt.configure(text="Fahrenheit temperature:")
        entry_temp.configure(placeholder_text="e.g. 98.6")
    else:
        label_prompt.configure(text="Celsius temperature:")
        entry_temp.configure(placeholder_text="e.g. 37.0")
    label_result.configure(text="")  # Clear previous result


app = ctk.CTk()
app.title("Temperature Converter")
app.geometry("400x320")

mode_switch = ctk.CTkOptionMenu(
    app,
    values=["Fahrenheit to Celsius", "Celsius to Fahrenheit"],
    command=update_labels,
)
mode_switch.pack(pady=15)

label_prompt = ctk.CTkLabel(app, text="Fahrenheit temperature:")
label_prompt.pack(pady=5)

entry_temp = ctk.CTkEntry(app, placeholder_text="e.g. 98.6")
entry_temp.pack(pady=10)

button_convert = ctk.CTkButton(app, text="Convert", text_color="black",
                               fg_color="pink", command=convert)
button_convert.pack(pady=10)

label_result = ctk.CTkLabel(app, text="", font=("Arial", 14, "bold"))
label_result.pack(pady=15)

app.mainloop()
