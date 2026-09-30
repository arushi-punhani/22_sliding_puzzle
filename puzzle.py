import random


class Puzzle:

    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        tiles = list(range(1, self.size * self.size)) + [0]

        # Build initial solved grid
        board = [
            tiles[r * self.size : (r + 1) * self.size] for r in range(self.size)
        ]

        # Temporarily assign board so self.blank_pos() and self.move() work
        self.board = board

        # Scramble using only legal blank moves
        for _ in range(self.size * self.size * 10):
            direction = random.choice(["w", "a", "s", "d"])
            self.move(direction)

        # Avoid starting in the solved state
        while self.solved():
            for _ in range(self.size * self.size * 10):
                direction = random.choice(["w", "a", "s", "d"])
                self.move(direction)

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