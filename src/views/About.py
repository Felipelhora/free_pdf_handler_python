import tkinter as tk
from tkinter import filedialog
from src.repository.compress_pdf import execute_compress
from PIL import Image, ImageTk
from src.views.ModalsView import ModalsView
import tkinter.ttk as ttk
from src.views.Images import Icons
from tktooltip  import ToolTip

class About(ModalsView):
      
    def __init__(self):
        self.icons = Icons()

        
    def page_about(self, page):

        label_info = tk.Label(page, text="Sistema de manipulação de PDF", width=50, font=("Arial", 20))
        label_info.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        label_info = tk.Label(page, text="Projeto de Conclusão de Curso Análise \ne desenvolvimento de Sistemas CEUB", width=50, font=("Arial", 10))
        label_info.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


        label_info = tk.Label(page, text="Alunos\nEmy Saiki Watanabe – RA: 72250476\nFelipe Lima da Hora – RA: 72200124\nFilipe Victal Vianna – RA: 72200652\nGabriel Henrique do Nascimento Neres – RA: 72200310\nThaissa Silva Rodrigues – RA: 72200773", width=50, font=("Arial", 10))
        label_info.place(relx=0.5, rely=0.6, anchor=tk.CENTER)