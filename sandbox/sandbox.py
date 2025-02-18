import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x200")  # Width x Height

# Add a label
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Function to be called when button is clicked


def on_button_click():
    label.config(text="Button Clicked!")


# Add a button
button = ttk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()
