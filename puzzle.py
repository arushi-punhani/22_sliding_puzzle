import random


class Puzzle:

    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        tiles = list(range(1, self.size * self.size)) + [0]
        self.board = [
            tiles[r * self.size : (r + 1) * self.size] for r in range(self.size)
        ]

        # Scramble using legal blank moves
        moves_count = self.size * self.size * 20
        for _ in range(moves_count):
            r, c = self.blank_pos()
            valid_dirs = []
            if r > 0:
                valid_dirs.append("w")
            if r < self.size - 1:
                valid_dirs.append("s")
            if c > 0:
                valid_dirs.append("a")
            if c < self.size - 1:
                valid_dirs.append("d")

            self.move(random.choice(valid_dirs))

        # Ensure board isn't already solved
        while self.solved():
            r, c = self.blank_pos()
            valid_dirs = []
            if r > 0:
                valid_dirs.append("w")
            if r < self.size - 1:
                valid_dirs.append("s")
            if c > 0:
                valid_dirs.append("a")
            if c < self.size - 1:
                valid_dirs.append("d")

            self.move(random.choice(valid_dirs))

        return self.board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        r, c = self.blank_pos()
        dr, dc = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}[
            direction
        ]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False
        self.board[r][c], self.board[nr][nc] = (
            self.board[nr][nc],
            self.board[r][c],
        )
        return True

    def solved(self):
        return (
            sum(self.board, []) == list(range(1, self.size * self.size)) + [0]
        )