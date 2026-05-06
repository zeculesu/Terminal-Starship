import time
import sys
import signal

class Engine:
    def __init__(self, scene, screen, fps=1):
        self.scene = scene
        self.screen = screen
        self.fps = fps
        self.frame = 0
        self.running = True
        
        signal.signal(signal.SIGINT, self._signal_handler)

    def _signal_handler(self, signum, frame):
        self.running = False

    def increase_fps(self): self.fps += 10
    
    def decrease_fps(self): self.fps -= 10

    def run(self):
        with self.screen:
            self.scene.draw_background(self.screen)
            while self.running:
                start = time.time()

                self.screen.goto(1, 1)

                # 1. input
                # key = self.input.get_key()
                # if key:
                #     self.scene.handle_input(key)

                # 2. update
                self.scene.update(self.frame)

                # 3. draw
                # self.scene.draw_background(self.screen)

                for sprite in self.scene.sprites:
                    sprite.draw(self.screen, self.frame)
                sys.stdout.flush()

                self.frame += 1

                time.sleep(max(0, 1 / self.fps - (time.time() - start)))
