import time

class Engine:
    def __init__(self, scene, screen, fps=10):
        self.scene = scene
        self.screen = screen
        self.fps = fps
        self.frame = 0
        self.running = True

    def run(self):
        with self.screen:
            self.scene.draw()
            while self.running:
                start = time.time()

                for sprite in self.scene.sprites:
                    sprite.draw(self.screen, self.frame)
                self.frame += 1
                # self._handle_input()

                dt = time.time() - start
                time.sleep(max(0, 1 / self.fps - dt))
