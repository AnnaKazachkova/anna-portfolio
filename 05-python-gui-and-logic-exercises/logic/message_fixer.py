"""String and list manipulation: correct a message and append a sign-off."""

message = "MESSAGE RECEIVED:\nPython\tis difficult to learn. \nBut Python is difficult to use!"
print(message)

wordlist = "But Python is difficult to use!".split()
message = message.split()
wordlist[3] = "fun"
wordlist.append("Good luck!")
message[7:] = wordlist
newmessage = " ".join(message)
print(newmessage, "\ncorrected message.")
