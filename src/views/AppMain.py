import tkinter as tk
from tkinter import ttk
from src.config import ICOS
from src.views.MergeView import MergeView
from src.views.SplitView import SplitView
from src.views.ProtegerView import ProtegerView
from src.views.WaterMarkView import WaterMarkView
from src.views.RotatePdf import RotatePdf
from src.views.ConvertToPdf import ConvertToPdf
from src.views.CompressPdfView import CompressPdfView
from src.views.About import About



class AppMain:
   def __init__(self, root):
      self.root = root
      self.root.iconbitmap(ICOS['pdf'])
      self.root.title("MaXterPDF")
      self.root.geometry("650x500")
      self.file_paths = []
      self.merge_view = MergeView()
      self.protect_view = ProtegerView()
      self.water_mark_view = WaterMarkView()
      self.rotate_pdf = RotatePdf()
      self.compress_pdf = CompressPdfView()
      self.about = About()
      self.notebook = ttk.Notebook(root)
      self.notebook.pack(side=tk.LEFT, fill=tk.Y)
      self.root.resizable(False, False) 
      len_space_title = 12
      self.option_1 = self.__get_spaces_string("JUNTAR", len_space_title)
      self.option_2 = self.__get_spaces_string("SEPARAR", len_space_title)
      self.option_3 = self.__get_spaces_string("ROTACIONAR", len_space_title)
      self.option_4 = self.__get_spaces_string("CONVERTER", len_space_title)
      self.option_5 = self.__get_spaces_string("MARCA D'ÁGUA", len_space_title)
      self.option_6 = self.__get_spaces_string("COMPRIMIR", len_space_title)
      self.option_7 = self.__get_spaces_string("PROTEGER", len_space_title)
      self.option_8 = self.__get_spaces_string("SOBRE", len_space_title)
      actions = [self.option_1, self.option_2 , self.option_3, self.option_4, self.option_5, self.option_6, self.option_7, self.option_8]
      for action in actions:
         page = tk.Frame(self.notebook)
         self.notebook.add(page, text=action)
         self.create_action_widgets(page, action)

   # Para deixar um espaçamento entre as abas igual
   def __get_spaces_string(self, text:str, len_tittle:int) -> list:
        number_text = len(text)
        value_string = len_tittle
        len_space = (value_string - number_text) // 2
        extra_space = (value_string - number_text) % 2
        return f"{' '* len_space}{text}{' '* (len_space + extra_space)}"

   def create_action_widgets(self, page, action):
         if action == self.option_1:
            self.merge_view.page_merge(page)
         elif action == self.option_2:
           self.split_view = SplitView(root=page)
         elif action == self.option_3:
            self.rotate_pdf.page_rotate(page)
         elif action == self.option_4:
            self.split_view = ConvertToPdf(page)
         elif action == self.option_5:
            self.water_mark_view.page_watermark(page)
         elif action == self.option_6:
            self.compress_pdf.page_compress(page)
         elif action == self.option_7:
            self.protect_view.page_protect(page)
         elif action == self.option_8:
            self.about.page_about(page)

            
           
           

