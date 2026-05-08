import shutil



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