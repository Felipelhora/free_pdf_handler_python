import tkinter as tk
from tkinter import ttk
from src.views.subviews_convert.ConvertImages import ConvertImages
from src.views.subviews_convert.ConvertDocuments import ConvertDocuments


class ConvertToPdf:
    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(side=tk.LEFT, fill=tk.Y)

        # Criando as abas para cada ação
        len_space_title = 76
        self.option_1 = self.__get_spaces_string("CONVERTER IMAGENS", len_space_title)
        self.option_2 = self.__get_spaces_string("CONVERTER DOCUMENTOS", len_space_title)
        actions = [self.option_1, self.option_2]
        for action in actions:
            page = tk.Frame(self.notebook)
            self.notebook.add(page, text=action)
            self.create_action_widgets(page, action)


    def __get_spaces_string(self, text:str, len_tittle:int) -> list:
        number_text = len(text)
        value_string = len_tittle
        len_space = (value_string - number_text) // 2
        extra_space = (value_string - number_text) % 2
        return f"{' '* len_space}{text}{' '* (len_space + extra_space)}"

    def create_action_widgets(self, page, action):
        if action == self.option_1:
            ConvertImages().page_convert_images(page)
        if action == self.option_2:
           ConvertDocuments().page_convert_documents(page)