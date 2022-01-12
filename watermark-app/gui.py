from tkinter import *

root = Tk()
root.title("WaterMarker")
root.geometry("600x400")

# the labels
logo_label = Label(root, text="WaterMarker")
logo_label.grid(row=0)

description = Label(root, text="add pictorial and textual watermarks to your pictures")
description.grid(row=1)

text_watermark = Text(root, height=1, width=50)
text_watermark.grid(row=2)

root.mainloop()