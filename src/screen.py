import sys
import shutil

class Screen:
    ESC = "\033["

    def goto(self, y: int, x: int):
        sys.stdout.write(f"{self.ESC}{y};{x}H")

    def hide_cursor(self):
        sys.stdout.write(f"{self.ESC}?25l")
    
    def show_cursor(self):
        sys.stdout.write(f"{self.ESC}?25h")

    def clear(self):
        sys.stdout.write(f"{self.ESC}2J")

    def move_to_bottom(self):
        rows = shutil.get_terminal_size((80, 24)).lines
        self.goto(rows, 1)
    
    def move_to_input_line(self, offset: int = 1):
        rows = shutil.get_terminal_size((80, 24)).lines
        self.goto(rows - offset + 1, 1)

    def enter(self):
        sys.stdout.write(f"{self.ESC}?1049h")
        sys.stdout.write(f"{self.ESC}H")
        self.hide_cursor()
        self.clear()
        sys.stdout.flush()

    def exit(self):
        self.show_cursor()
        print(f"{self.ESC}?1049l", end="", flush=True)
        sys.stdout.flush()
    
    def __enter__(self):
        self.enter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.exit()