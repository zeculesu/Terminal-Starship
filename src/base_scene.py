class SceneBase:
    def __init__(self):
        self.sprites = []

    def update(self, frame: int):
        """обновление логики сцены"""
        pass

    def draw_background(self, screen):
        """рисование фона (ASCII корабль и т.д.)"""
        pass

    def handle_input(self, key):
        """реакция сцены на input"""
        pass