import sys

class Sprite:
    def __init__(self, y, x, frames):
        self.y = y
        self.x = x
        self.frames = frames
        self.current = 0

    def update(self, frame):
        self.current = frame % len(self.frames)

    def draw(self, screen, frame):
        screen.goto(self.y, self.x)
        sys.stdout.write(self.frames[self.current])
