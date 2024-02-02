import tkinter as tk

class BouncingBallApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=600, height=400, bg='black')
        self.canvas.pack()
        self.ball = self.canvas.create_oval(270, 170, 330, 230, fill='white')  # Center the ball
        self.dx = 2
        self.dy = 2
        self.is_running = False  # Animation state

        # Create a start button
        self.start_button = tk.Button(master, text="Start", command=self.start_animation)
        self.start_button.pack()

        # Position the button in the middle of the canvas
        self.start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def start_animation(self):
        self.is_running = True
        self.start_button.destroy()  # Remove the start button after pressing it
        self.run_animation()

    def run_animation(self):
        if self.is_running:
            self.animate_ball()
            self.master.after(20, self.run_animation)

    def animate_ball(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        pos = self.canvas.coords(self.ball)
        if pos[3] >= 400 or pos[1] <= 0:
            self.dy = -self.dy
        if pos[2] >= 600 or pos[0] <= 0:
            self.dx = -self.dx

if __name__ == "__main__":
    root = tk.Tk()
    app = BouncingBallApp(root)
    root.mainloop()
