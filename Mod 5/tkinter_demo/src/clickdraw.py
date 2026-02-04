import tkinter as tk

def draw_dot(event):
    r = 6  # radius of the dot
    x, y = event.x, event.y
    canvas.create_oval(
        x - r, y - r,
        x + r, y + r,
        fill="dodgerblue",
        outline=""
    )

root = tk.Tk()
root.title("Click to Draw")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Bind left mouse button click
canvas.bind("<Button-1>", draw_dot)

root.mainloop()
