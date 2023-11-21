from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20,)

        # Score Label:
        self.score = Label()
        self.score.config(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        # Canvas Widget
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Create a white rectangle to serve as the background
        self.canvas.create_rectangle(
            0, 0, 300, 250, fill='white', outline='white')

        # Create text on the canvas
        self.question_text = self.canvas.create_text(150, 125, text="Your Question Here", font=(
            "Arial", 20, "italic"), fill=THEME_COLOR)

        # Buttons
        self.true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(
            text="Right", image=self.true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(
            text="Wrong", image=self.false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
