import tkinter as tk
import random

class SpaceInvaders:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Invaders")
        self.canvas = tk.Canvas(root, width=600, height=400, bg='black')
        self.canvas.pack()

        self.player = self.canvas.create_rectangle(270, 350, 330, 380, fill='green')
        self.bullets = []
        self.enemies = []
        self.score = 0
        self.game_over = False

        self.create_enemies()
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)

        self.update()

    def move_left(self, event):
        if self.canvas.coords(self.player)[0] > 0:  # Check left boundary
            self.canvas.move(self.player, -20, 0)

    def move_right(self, event):
        if self.canvas.coords(self.player)[2] < 600:  # Check right boundary
            self.canvas.move(self.player, 20, 0)

    def shoot(self, event):
        x1 = self.canvas.coords(self.player)[0]
        y1 = self.canvas.coords(self.player)[1]
        x2 = self.canvas.coords(self.player)[2]
        y2 = self.canvas.coords(self.player)[3]
        bullet = self.canvas.create_rectangle(x1 + 20, y1 - 10, x2 - 20, y2 - 10, fill='yellow')
        self.bullets.append(bullet)
        self.move_bullet(bullet)

    def move_bullet(self, bullet):
        self.canvas.move(bullet, 0, -10)
        if self.canvas.coords(bullet)[1] <= 0:  # Check if bullet is off screen
            self.canvas.delete(bullet)
            self.bullets.remove(bullet)
        else:
            self.check_collision(bullet)
            self.root.after(50, lambda: self.move_bullet(bullet))

    def check_collision(self, bullet):
        bullet_coords = self.canvas.coords(bullet)
        for enemy in self.enemies:
            enemy_coords = self.canvas.coords(enemy)
            if (bullet_coords[0] < enemy_coords[2] and bullet_coords[2] > enemy_coords[0] and
                    bullet_coords[1] < enemy_coords[3] and bullet_coords[3] > enemy_coords[1]):
                self.canvas.delete(bullet)
                self.canvas.delete(enemy)
                self.bullets.remove(bullet)
                self.enemies.remove(enemy)
                self.score += 1
                print(f"Score: {self.score}")
                break

        # Check if all enemies are destroyed
        if not self.enemies:
            self.game_over = True
            print("Game Over! You won!")

    def create_enemies(self):
        for i in range(5):
            enemy = self.canvas.create_rectangle(50 + i * 100, 50, 100 + i * 100, 100, fill='red')
            self.enemies.append(enemy)

    def move_enemies(self):
        for enemy in self.enemies:
            self.canvas.move(enemy, 0, 1)  # Move enemies downwards
            # Check if any enemy has reached the bottom of the canvas
            enemy_coords = self.canvas.coords(enemy)
            if enemy_coords[3] >= 400:  # Check if enemy hits the bottom
                self.game_over = True
                print("Game Over! Enemies reached the bottom!")
                break  # Exit the loop if game is over

        if not self.game_over:
            self.root.after(1000, self.move_enemies)  # Move enemies every second

    def update(self):
        if not self.game_over:
            self.move_enemies()  # Call to move enemies
            self.root.after(100, self.update)
        else:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = SpaceInvaders(root)
    root.mainloop()