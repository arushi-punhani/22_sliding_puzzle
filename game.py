import time
from puzzle import Puzzle


class SlidingPuzzle:

    def __init__(self, size=None):
        self.size = size if size is not None else self.choose_size()
        self.moves = 0
        self.started = time.monotonic()
        self.is_completed = False
        self.puzzle = Puzzle(self.size)

    def choose_size(self):
        while True:
            print("\nChoose puzzle size:")
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

    def reset_board(self, new_size=None):
        """Recreates board while preserving session timer and move tracking."""
        if new_size is not None:
            self.size = new_size
        self.puzzle = Puzzle(self.size)
        self.is_completed = False

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

            # Detect solved state
            if self.puzzle.solved():
                self.is_completed = True
                print("\nSolved! Game complete.")
                print("Options: [Q]uit | [R]eset board")

                # Freeze lifecycle: commands cannot alter board state post-completion
                while True:
                    key = input("> ").strip().lower()
                    if key == "q":
                        return
                    elif key == "r":
                        self.reset_board()
                        break
                    else:
                        print("Puzzle is solved! Press Q to quit or R to reset.")
                continue

            key = input("> ").strip().lower()

            if key == "q":
                return

            if not key or key not in ("w", "a", "s", "d"):
                print("Use W/A/S/D.")
                continue

            # Task 4: Only increment move counter if tile actually moved
            if self.puzzle.move(key):
                self.moves += 1
            else:
                print("That move is not possible.")


