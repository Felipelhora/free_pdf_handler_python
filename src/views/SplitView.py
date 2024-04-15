import tkinter as tk
from tkinter import ttk
from src.views.subviews_split.SplitBlocksView import SplitBlocksView
from src.views.subviews_split.SplitOddEven import SplitOddEven
from src.views.subviews_split.SplitFreeChoises import SplitFreeChoises
from src.views.subviews_split.SplitRemovePages import SplitRemovePages



class SplitView:
    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(side=tk.LEFT, fill=tk.Y)
        self.split_blocks = SplitBlocksView()
        self.split_odd_even = SplitOddEven()
        self.split_free_choises = SplitFreeChoises()
        self.split_remove_pages = SplitRemovePages()
        # Criando as abas para cada ação
        len_space_title = 30
        self.option_1 = self.__get_spaces_string("SEPARAR POR BLOCOS", len_space_title)
        self.option_2 = self.__get_spaces_string("IMPARES E PARES", len_space_title)
        self.option_3 = self.__get_spaces_string("SEPARAR DE FOLHAS", len_space_title)
        self.option_4 = self.__get_spaces_string("REMOVER FOLHAS", len_space_title)
        actions = [self.option_1, self.option_2 , self.option_3, self.option_4]
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
            self.split_blocks.page_split_blocks(page)
        if action == self.option_2:
            self.split_odd_even.page_split_odd_even(page)
        if action == self.option_3:
            self.split_free_choises.page_split_free_choises(page)
        if action == self.option_4:
            self.split_remove_pages.page_split_remove_pages(page)