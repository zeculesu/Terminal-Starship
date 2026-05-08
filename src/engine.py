import time
import sys
import signal
import tty
import termios
from utils import *

class Engine:
    def __init__(self, scene, screen, fps=1):
        self.scene = scene
        self.screen = screen
        self.fps = fps
        self.frame = 0
        self.running = True
        self.resize_error = False
        self.old_settings = None

        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGWINCH, self._resize_handler)

    def _signal_handler(self, signum, frame): self.running = False
    
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

    def get_key(self):
        ch = sys.stdin.read(1)
        
        if ch == '\x1b':
            next1 = sys.stdin.read(1)
            if next1 == '[':
                next2 = sys.stdin.read(1)
                if next2 == 'A':
                    return 'UP'
                elif next2 == 'B':
                    return 'DOWN'
            return None
        elif ch == 'Q' or ch == "q":
            return 'EXIT'
        return ch
    
    def enable_raw_mode(self):
        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    def disable_raw_mode(self):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def run(self):
        if not check_screen_size(self.scene.get_background()):
            self.print_resize_error()
            return

        with self.screen:
            self.enable_raw_mode()
            self.scene.draw_background(self.screen)
            while self.running:
                start = time.time()

                self.screen.goto(1, 1)

                import select
                if select.select([sys.stdin], [], [], 0.0)[0]:
                    key = self.get_key()
                    if key == 'EXIT': break
                    elif key == 'UP': self.increase_fps()
                    elif key == 'DOWN': self.decrease_fps()
                    elif key:
                        self.scene.handle_input(key)

                self.scene.update(self.frame)

                for sprite in self.scene.sprites:
                    sprite.draw(self.screen, self.frame)
                self.screen.move_to_input_line() 
                sys.stdout.flush()

                self.frame += 1

                time.sleep(max(0, 1 / self.fps - (time.time() - start)))
        
        self.disable_raw_mode()
        if self.resize_error:
            self.print_resize_error()