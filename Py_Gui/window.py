import tkinter as tk

# Create the main window (root)
root = tk.Tk()

# Set the window title
root.title("My Tkinter Window")

# Set the window size
root.geometry("400x300")

# Create a frame inside the root window
frame = tk.Frame(root, bg="lightblue", width=300, height=200)
frame.pack(pady=20)  # Add some padding
label = tk.Label(frame, text="Enter your details below:", font=("Arial", 14))
label.pack(pady=10)
entry = tk.Entry(frame, width=30)
entry.pack(pady=5)
def on_button_click():
    print("Button clicked!")

button = tk.Button(frame, text="Submit", command=on_button_click)
button.pack(pady=10)
root.iconbitmap("path_to_icon.ico")

# Start the Tkinter main loop
root.mainloop()
