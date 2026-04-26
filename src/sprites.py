class Sprite:
    def __init__(self, y, x, frames, enabled=True):
        self.y = y
        self.x = x
        self.frames = frames
        self.enabled = enabled

    def draw(self, screen, frame):
        if not self.enabled:
            return
        screen.goto(self.y, self.x)
        print(self.frames[frame % len(self.frames)], end="", flush=True)