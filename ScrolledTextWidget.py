import tkinter as tk
from tkinter.scrolledtext import ScrolledText

turtle = tk.Tk()
turtle.title("ScrolledText Widget")

st = ScrolledText(turtle, width = 50, height=10)
st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

turtle.mainloop()