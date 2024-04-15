import tkinter as tk
from PyPDF2 import errors
import math
from tkinter import messagebox, PhotoImage, filedialog
from PIL import Image, ImageDraw, ImageTk
from src.config import ICOS

class ModalsView:

    def __init__(self):
        self.loading_screen = None
        self.angle = 0
        self.animation = None

    def show_loading_circle(self):
        if self.loading_screen is None:
            self.loading_screen = tk.Toplevel()
            self.loading_screen.geometry("300x300")
            self.loading_screen.title("PROCESSANDO")
            self.loading_screen.resizable(False, False)
            self.loading_screen.iconbitmap(ICOS['pdf'])
            loading_label = tk.Label(self.loading_screen, text="PROCESSANDO...")
            loading_label.pack(pady=20)
            self.canvas = tk.Canvas(self.loading_screen, width=100, height=100)
            self.canvas.pack(pady=20)
            self.draw_circle()

    def draw_circle(self):
        try:
            if self.loading_screen:
                self.angle += 10
                self.angle %= 360
                image = Image.new("RGBA", (100, 100), (255, 255, 255, 0))
                draw = ImageDraw.Draw(image)
                draw.arc((10, 10, 90, 90), start=0, end=self.angle, fill="blue", width=10)
                self.animation = ImageTk.PhotoImage(image.rotate(-90))
                self.canvas.create_image(50, 50, image=self.animation)
                self.loading_screen.after(50, self.draw_circle)
        except:
            ...

    def close_loading_screen(self):
        try:
            if self.loading_screen:
                self.loading_screen.destroy()
                self.loading_screen = None
        except:
            ...

    def message_error(self, text:str) -> None:
        tk.messagebox.showerror("Erro", f"⚠️{text}⚠️")
    
    def message_success(self, text:str) -> None:
        tk.messagebox.showinfo("Sucesso", f"☑️{text}☑️")

    def exceptions_message(self, exception:str):
            if type(exception) == type(str):
                exception = exception
            else:
                exception = exception.__class__.__name__  
            if exception == 'FileNotDecryptedError':
                self.message_error(f'O arquivo está protegido por senha, não é possivel executar a operação')
            elif exception == 'ValueError':
                self.message_error(f'O arquivo não pode ser carregado, ou está corrompido ou não é um PDF, verifique melhor a lista de arquivos')    
            elif exception == 'PdfReadError':
                self.message_error(f'O arquivo não pode ser carregado, ou está corrompido ou não é um PDF, verifique melhor a lista de arquivos')
            elif exception == 'WrongParameter':
                self.message_error(f'Parametro Errado')
            else:
                self.message_error(f'Algo errado, refaça a operação, {exception}')
        
        
