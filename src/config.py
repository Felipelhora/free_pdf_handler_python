import os
import platform



def bar():
    if platform.system() == 'Windows':
        bar = '/'

    elif platform.system() == 'linux':
        bar = '\\'
    return bar


CONFIG = {
            "local_path" : os.getcwd(),
           
            "type_enconde_text" : 'latin-1',
            "images_path" : f'{os.getcwd()}{bar()}src{bar()}images',
            "system":  platform.system(),
            "bar_system": bar(),
            "extensions_images_suporte": ['png', 'jpg', 'jpeg', 'bitmap'],

}

ICOS = {
            "open": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}open.png',
            "save": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}save.png',
            "add": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}add.png',
            "delete": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}delete.png',
            "clear": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}clear.png',
            "clockwise": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}clockwise.png',
            "up": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}up.png',
            "down": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}down.png',
            "open_image": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}open_image.png',
            "to_see": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}to_see.png',
            "percentage": f'{os.getcwd()}{bar()}images{bar()}icos{bar()}percentage.png',
            "pdf" :f'{os.getcwd()}{bar()}images{bar()}icos{bar()}pdf.ico',
        }