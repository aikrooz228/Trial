import tkinter as tk
from PIL import Image, ImageTk  # Importing necessary classes from Pillow

# Initialize the main window
window = tk.Tk()
window.geometry("500x600")
window.title("COS Dictionaries")

# Add a welcome label
label = tk.Label(window, text="Welcome to COS Dictionary to check on Amazing words",font="Georgia,23",bg="Beige",fg="Brown")

label.pack(pady=1)

# Path to the JPEG image file
image_path = r"C:\Users\USER\Downloads\sandy-millar-Kl4LNdg6on4-unsplash.jpg"

# Load the image using Pillow and convert it to PhotoImage
img = Image.open(image_path)
bg_image = ImageTk.PhotoImage(img)

# Create a Label widget to display the background image
background = tk.Label(window, image=bg_image)
background.place(relheight=1, relwidth=1)
background.pack()



# Start the application
window.mainloop()
