import time
import sys
import signal
import shutil
import os

def check_screen_size(image: str):
    term = shutil.get_terminal_size((80, 24))
    term_w, term_h = term.columns, term.lines

    img_w, img_h = get_image_size(image)

    return term_w >= img_w and term_h >= img_h

def get_image_size(image: str):
    lines = image.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    return width, height

class Engine:
    def __init__(self, scene, screen, fps=1):
        self.scene = scene
        self.screen = screen
        self.fps = fps
        self.frame = 0
        self.running = True
        self.resize_error = False

        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGWINCH, self._resize_handler)

    def _signal_handler(self, signum, frame):
        self.running = False
    
    def _resize_handler(self, signum, frame):
        if not check_screen_size(self.scene.get_background()):
            self.running = False
            self.resize_error = True

    def increase_fps(self): self.fps += 10
    
    def decrease_fps(self): 
        if self.fps > 10:
            self.fps -= 10

    def print_resize_error(self):
        sys.stdout.write(
            "Терминал слишком маленький для отображения картинки\n"
            "Увеличьте размер окна и перезапустите программу.\n"
        )
        sys.stdout.flush()
        return

    def run(self):
        if not check_screen_size(self.scene.get_background()):
            self.print_resize_error()
            return

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

                for sprite in self.scene.sprites:
                    sprite.draw(self.screen, self.frame)
                sys.stdout.flush()

                self.frame += 1

                time.sleep(max(0, 1 / self.fps - (time.time() - start)))
        
        if self.resize_error:
            self.print_resize_error()