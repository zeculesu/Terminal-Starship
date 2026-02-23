import argparse
from engine import Engine
from scene import Scene
from screen import Screen

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="cruise")
    args = parser.parse_args()

    scene = Scene(mode=args.mode)
    screen = Screen()
    engine = Engine(scene, screen)
    engine.run()

if __name__ == "__main__":
    main()