from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas Widget
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2)

        # Create a white rectangle to serve as the background
        self.canvas.create_rectangle(
            0, 0, 300, 250, fill='white', outline='white')

        # Create text on the canvas
        self.canvas.create_text(150, 125, text="Your Question Here", font=(
            "Arial", 20, "italic"), fill='black')

        # Buttons
        self.true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(text="Right", image=self.true_img)
        self.true_btn.grid(column=0, row=2)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(text="Wrong", image=self.false_img)
        self.false_btn.grid(column=1, row=2)

        self.window.mainloop()
