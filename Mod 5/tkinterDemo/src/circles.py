import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tkinter Demo – Concentric Circles")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Centre of the canvas
cx, cy = 200, 200

# Draw concentric circles
radii = [150, 120, 90, 60, 30]
colours = ["#4e79a7", "#59a14f", "#f28e2b", "#e15759", "#76b7b2"]

for r, colour in zip(radii, colours):
    canvas.create_oval(
        cx - r, cy - r,
        cx + r, cy + r,
        outline=colour,
        width=4
    )

root.mainloop()
