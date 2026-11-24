import tkinter as tk

# Create the main game window
window = tk.Tk()
window.title("Dress to Impress")
window.geometry("600x500")
window.configure(bg="lightpink")

# Game title
title = tk.Label(
    window,
    text="Dress to Impress",
    font=("Arial", 28, "bold"),
    bg="lightpink",
    fg="deeppink"
)
title.pack(pady=60)

# Welcome message
welcome = tk.Label(
    window,
    text="Welcome to Dress to Impress!\nGet ready to show off your style!",
    font=("Arial", 15),
    bg="lightpink",
    fg="black"
)
welcome.pack(pady=20)
# Function to start the game
def start_game():
    welcome.config(text="Choose an outfit to match the theme!")
    start_button.config(state="disabled")

# Start Game button
start_button = tk.Button(
    window,
    text="Start Game",
    font=("Arial", 16),
    fg="deeppink",
    command=start_game
)
start_button.pack(pady=20)

# Keep the game window open
window.mainloop()
