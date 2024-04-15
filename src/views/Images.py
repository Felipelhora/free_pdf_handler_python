from PIL import Image, ImageTk
from src.config import ICOS





class Icons:



    def __init__(self):
        self.ico_open_folder = self.open_folder()
        self.ico_save = self.save()
        self.ico_add = self.add()
        self.ico_clear = self.clear()
        self.ico_clockwise = self.clockwise()
        self.ico_delete = self.delete()
        self.ico_down = self.down()
        self.ico_up = self.up()
        self.ico_percentage = self.percentage()
        self.ico_open_image = self.open_image()
        self.ico_to_see = self.to_see()

    def __operate_image_lower(self, image_path):
        ico = Image.open(image_path)
        ico = ico.resize((30, 30))
        return ico

    def __operate_image(self, image_path):
        ico = Image.open(image_path)
        ico = ico.resize((30, 30))
        return ico

    def open_folder(self):
        return self.__operate_image(ICOS['open'])

    def save(self):
        return self.__operate_image(ICOS['save'])

    def add(self):
        return self.__operate_image(ICOS['add'])
    
    def clear(self):
        return self.__operate_image(ICOS['clear'])

    def clockwise(self):
        return self.__operate_image(ICOS['clockwise'])
    
    def delete(self):
        return self.__operate_image(ICOS['delete'])

    def down(self):
        return self.__operate_image_lower(ICOS['down'])
    
    def up(self):
        return self.__operate_image_lower(ICOS['up'])
    
    def open_image(self):
        return self.__operate_image(ICOS['open_image'])
    
    def percentage(self):
        return self.__operate_image(ICOS['percentage'])
    
    def to_see(self):
        return self.__operate_image(ICOS['to_see'])