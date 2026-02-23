import sys


class Screen:
    ESC = "\033["

    def goto(self, y: int, x: int):
        print(f"{self.ESC}{y};{x}H", end="", flush=True)

    def hide_cursor(self):
        print(f"{self.ESC}?25l", end="", flush=True)

    def show_cursor(self):
        print(f"{self.ESC}?25h", end="", flush=True)

    def clear(self):
        print(f"{self.ESC}2J", end="", flush=True)

    def enter(self):
        print(f"{self.ESC}?1049h", end="", flush=True)
        self.hide_cursor()
        self.clear()

    def exit(self):
        self.show_cursor()
        print(f"{self.ESC}?1049l", end="", flush=True)
        sys.stdout.flush()
    
    def __enter__(self):
        self.enter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.exit()