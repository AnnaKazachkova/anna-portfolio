"""Enigma-inspired encoder / decoder with a CustomTkinter GUI.

Algorithm (per character, position = index in the message)
  rotor1 = (key + day_of_month + position) % 26
  rotor2 = (key * 2 + position) % 26
  shift  = rotor1 + rotor2
  encrypt: chr(ord(c) + shift)      decrypt: chr(ord(c) - shift)

Build a standalone app:
  python3 -m pip install pyinstaller
  python3 -m PyInstaller --onefile --windowed enigma_tool.py
"""
from datetime import datetime

import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"


def shift_for(key, day_date, position):
    rotor1 = (key + day_date + position) % 26
    rotor2 = (key * 2 + position) % 26
    return rotor1 + rotor2


def encrypt(message, key, day_date):
    return "".join(
        chr(ord(ch) + shift_for(key, day_date, pos)) for pos, ch in enumerate(message)
    )


def decrypt(message, key, day_date):
    return "".join(
        chr(ord(ch) - shift_for(key, day_date, pos)) for pos, ch in enumerate(message)
    )


class EnigmaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # window
        self.title("Enigma Encryption Tool")
        self.geometry("600x650")
        self.resizable(False, False)

        # Header
        self.title_label = ctk.CTkLabel(
            self, text="Encoder & Decoder", font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(padx=20, pady=(20, 10))

        # Description box
        info_text = (
            "Hello! Our team got inspired by the Enigma encryption machine, especially its rotating rotors. "
            "In the real Enigma, the rotors changed as each letter was typed, so the same letter could "
            "be encrypted differently depending on its position. Our code uses a similar idea with "
            "two 'rotors' that change as we go through the message. Rotor 1 changes based on the secret "
            "key, the day of the month, and the character's position, while rotor 2 changes based on the "
            "key and position. Together, they create a different shift for each character. We are not "
            "recreating the real Enigma algorithm because it would be too complex, but we used its main "
            "idea of changing the encryption as the message progresses."
        )
        self.info_box = ctk.CTkTextbox(self, height=120, width=540, wrap="word")
        self.info_box.insert("0.0", info_text)
        self.info_box.configure(state="disabled")  # read-only
        self.info_box.pack(padx=20, pady=10)

        # Input of key & date
        self.inputs_frame = ctk.CTkFrame(self)
        self.inputs_frame.pack(padx=20, pady=10, fill="x")

        self.key_label = ctk.CTkLabel(
            self.inputs_frame, text="Secret Key (Integer):", font=ctk.CTkFont(weight="bold")
        )
        self.key_label.grid(row=0, column=0, padx=15, pady=10, sticky="w")
        self.key_entry = ctk.CTkEntry(self.inputs_frame, placeholder_text="e.g. 7", width=120)
        self.key_entry.grid(row=0, column=1, padx=15, pady=10, sticky="w")

        # Day of the month (defaults to the current day)
        self.day_label = ctk.CTkLabel(
            self.inputs_frame, text="Day of Month (1-31):", font=ctk.CTkFont(weight="bold")
        )
        self.day_label.grid(row=0, column=2, padx=15, pady=10, sticky="w")
        current_day = str(datetime.now().day)
        self.day_entry = ctk.CTkEntry(self.inputs_frame, placeholder_text="1-31", width=100)
        self.day_entry.insert(0, current_day)
        self.day_entry.grid(row=0, column=3, padx=15, pady=10, sticky="w")

        # Message input
        self.msg_label = ctk.CTkLabel(
            self, text="Message to Process:", font=ctk.CTkFont(weight="bold")
        )
        self.msg_label.pack(padx=20, pady=(10, 0), anchor="w")
        self.message_entry = ctk.CTkEntry(
            self, placeholder_text="Type your broadcast message here...", width=540
        )
        self.message_entry.pack(padx=20, pady=5)

        # Actions
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(padx=20, pady=15)
        self.encrypt_btn = ctk.CTkButton(
            self.button_frame, text=" Encrypt", command=self.handle_encrypt, width=150
        )
        self.encrypt_btn.grid(row=0, column=0, padx=10)
        self.decrypt_btn = ctk.CTkButton(
            self.button_frame, text=" Decrypt", command=self.handle_decrypt, width=150
        )
        self.decrypt_btn.grid(row=0, column=1, padx=10)

        # Output
        self.result_label = ctk.CTkLabel(
            self, text="Output Result:", font=ctk.CTkFont(weight="bold")
        )
        self.result_label.pack(padx=20, pady=(10, 0), anchor="w")
        self.result_output = ctk.CTkTextbox(self, height=100, width=540, state="disabled")
        self.result_output.pack(padx=20, pady=5)

    def get_inputs(self):
        try:
            key = int(self.key_entry.get())
        except ValueError:
            self.show_output("Error: Secret Key must be a valid integer number.")
            return None

        try:
            day_date = int(self.day_entry.get())
            if not (1 <= day_date <= 31):
                raise ValueError
        except ValueError:
            self.show_output("Error: day of the Month must be an integer between 1 and 31.")
            return None

        message = self.message_entry.get()
        if not message:
            self.show_output("Error: Message field cannot be empty.")
            return None

        return message, key, day_date

    def show_output(self, text):
        self.result_output.configure(state="normal")
        self.result_output.delete("0.0", "end")
        self.result_output.insert("0.0", text)
        self.result_output.configure(state="disabled")

    def handle_encrypt(self):
        inputs = self.get_inputs()
        if inputs is None:
            return
        self.show_output(encrypt(*inputs))

    def handle_decrypt(self):
        inputs = self.get_inputs()
        if inputs is None:
            return
        self.show_output(decrypt(*inputs))


if __name__ == "__main__":
    app = EnigmaApp()
    app.mainloop()
