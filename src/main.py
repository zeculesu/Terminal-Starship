import argparse
import sys
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
    
    try:
        engine.run()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()