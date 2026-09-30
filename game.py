import time
from puzzle import Puzzle


class SlidingPuzzle:

    def __init__(self, size=None):
        # Allow choosing size at startup, falling back to 4x4
        self.size = size if size is not None else self.choose_size()
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()

    def choose_size(self):
        while True:
            print("Choose puzzle size:")
            print("1. 3x3")
            print("2. 4x4")
            print("3. 5x5")

            choice = input("> ").strip()

            if choice == "1":
                return 3
            elif choice == "2":
                return 4
            elif choice == "3":
                return 5
            else:
                print("Please choose 1, 2, or 3.")

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))
        print(
            "Moves:",
            self.moves,
            " Time:",
            int(time.monotonic() - self.started),
            "s",
        )

    def run(self):
        print(
            "Sliding Puzzle — W/A/S/D moves the tile into the blank. Q quits."
        )
        while True:
            self.display()
            if self.puzzle.solved():
                print("Solved!")
                return
            key = input("> ").strip().lower()
            if key == "q":
                return
            if not key or key not in ("w", "a", "s", "d"):
                print("Use W/A/S/D.")
                continue
            if self.puzzle.move(key):
                self.moves += 1
            else:
                print("That move is not possible.")


if __name__ == "__main__":
    game = SlidingPuzzle()
    game.run()