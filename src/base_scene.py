import sys

class SceneBase:
    def __init__(self):
        self.sprites = []

    def update(self, frame: int):
        pass

    def draw_background(self, screen):
        bg = self.get_background()
        if bg:
            sys.stdout.write(bg)

    def get_background(self):
        return ""

    def handle_input(self, key):
        pass