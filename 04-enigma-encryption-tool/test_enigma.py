"""Round-trip tests for the cipher logic (no GUI needed to run them).

Run with:  python -m pytest   (requires customtkinter installed, as the
module imports it) or simply  python test_enigma.py
"""
from enigma_tool import decrypt, encrypt


def test_known_value():
    # Matches the GUI screenshot: key=15, day=16, "Hello" -> "Qpy{" followed
    # by U+0080 (a non-printable control character, so it looks invisible).
    assert encrypt("Hello", 15, 16) == "Qpy{\x80"


def test_round_trip():
    msg = "Broadcast at dawn, 07:30!"
    for key in (0, 7, 15, 99):
        for day in (1, 16, 31):
            assert decrypt(encrypt(msg, key, day), key, day) == msg


if __name__ == "__main__":
    test_known_value()
    test_round_trip()
    print("all tests passed")
