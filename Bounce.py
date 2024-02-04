import tkinter as tk
import random

class BouncingBallApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=600, height=400, bg='black')
        self.canvas.pack()
        self.balls = []  # List to hold ball properties
        self.is_running = False  # Animation state

        # Create multiple balls
        for _ in range(5):  # Adjust the number of balls here
            size = random.randint(20, 50)  # Random size for each ball
            x = random.randint(size, 600-size)
            y = random.randint(size, 400-size)
            ball = self.canvas.create_oval(x, y, x+size, y+size, fill='white')
            dx = random.randint(1, 3) * random.choice([-1, 1])
            dy = random.randint(1, 3) * random.choice([-1, 1])
            self.balls.append([ball, dx, dy, size])

        # Create a start button
        self.start_button = tk.Button(master, text="Start", command=self.start_animation)
        self.start_button.pack()
        self.start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def start_animation(self):
        self.is_running = True
        self.start_button.destroy()  # Remove the start button
        self.run_animation()

    def run_animation(self):
        if self.is_running:
            for ball in self.balls:
                self.animate_ball(ball)
            self.detect_collisions()
            self.master.after(20, self.run_animation)

    def animate_ball(self, ball):
        self.canvas.move(ball[0], ball[1], ball[2])
        pos = self.canvas.coords(ball[0])
        if pos[3] >= 400 or pos[1] <= 0:
            ball[2] = -ball[2]  # Reverse y direction
        if pos[2] >= 600 or pos[0] <= 0:
            ball[1] = -ball[1]  # Reverse x direction

    def detect_collisions(self):
        for i, ball1 in enumerate(self.balls):
            for j, ball2 in enumerate(self.balls):
                if i != j:  # Avoid self-collision
                    x1, y1, _, _ = self.canvas.coords(ball1[0])
                    x2, y2, _, _ = self.canvas.coords(ball2[0])
                    dx = x1 - x2
                    dy = y1 - y2
                    distance = (dx**2 + dy**2)**0.5
                    if distance < (ball1[3] + ball2[3]) / 2:  # Check if balls are touching
                        ball1[1], ball2[1] = ball2[1], ball1[1]  # Swap x velocities
                        ball1[2], ball2[2] = ball2[2], ball1[2]  # Swap y velocities

if __name__ == "__main__":
    root = tk.Tk()
    app = BouncingBallApp(root)
    root.mainloop()