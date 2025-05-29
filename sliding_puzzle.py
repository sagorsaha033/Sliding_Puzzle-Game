import tkinter as tk
import random
from tkinter import messagebox


class SlidingPuzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("15 Puzzle Game")

        self.size = 4  # 4x4 puzzle
        self.tiles = list(range(1, self.size * self.size)) + [""]
        self.buttons = []

        self.create_widgets()
        self.shuffle_tiles()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        for row in range(self.size):
            row_buttons = []
            for col in range(self.size):
                btn = tk.Button(self.frame, text="", font=("Arial", 18), width=4, height=2,
                                command=lambda r=row, c=col: self.move_tile(r, c))
                btn.grid(row=row, column=col, padx=2, pady=2)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        self.reset_button = tk.Button(self.root, text="Shuffle", command=self.shuffle_tiles)
        self.reset_button.pack(pady=10)

    def shuffle_tiles(self):
        while True:
            random.shuffle(self.tiles)
            if self.is_solvable(self.tiles):
                break
        self.update_buttons()

    def update_buttons(self):
        for i in range(self.size):
            for j in range(self.size):
                val = self.tiles[i * self.size + j]
                btn = self.buttons[i][j]
                btn["text"] = val
                btn["state"] = "normal" if val != "" else "disabled"

    def move_tile(self, r, c):
        idx = r * self.size + c
        empty_idx = self.tiles.index("")
        empty_r, empty_c = divmod(empty_idx, self.size)

        # Check if clicked tile is next to the empty one
        if abs(empty_r - r) + abs(empty_c - c) == 1:
            self.tiles[empty_idx], self.tiles[idx] = self.tiles[idx], self.tiles[empty_idx]
            self.update_buttons()
            if self.is_solved():
                messagebox.showinfo("Congratulations!", "🎉 You solved the puzzle!")

    def is_solved(self):
        return self.tiles == list(range(1, self.size * self.size)) + [""]

    def is_solvable(self, tile_list):
        inv_count = 0
        flat = [t for t in tile_list if t != ""]
        for i in range(len(flat)):
            for j in range(i + 1, len(flat)):
                if flat[i] > flat[j]:
                    inv_count += 1

        empty_row = tile_list.index("") // self.size
        if self.size % 2 == 1:
            return inv_count % 2 == 0
        else:
            return (inv_count + self.size - empty_row) % 2 == 0


if __name__ == "__main__":
    root = tk.Tk()
    game = SlidingPuzzle(root)
    root.mainloop()
