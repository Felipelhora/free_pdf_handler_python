import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tktooltip  import ToolTip
from src.repository.water_mark import execute_mark_water, water_mark
from src.views.ModalsView import ModalsView
from src.views.Images import Icons
from PIL import Image, ImageTk

class WaterMarkView(ModalsView):
      
    def __init__(self):
        
        self.icons = Icons()
        #entrada do PDF
        self.entry_origin_path_pdf = None
        # Saida do PDF
        self.entry_output_path_pdf = None
        # Entrada da imagem
        self.entry_origin_path_image = None

    def get_input_pdf(self):
        pdf_origin_path_pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_origin_path_pdf:
            self.entry_origin_path_pdf.delete(0, tk.END)
            self.entry_origin_path_pdf.insert(0, pdf_origin_path_pdf)

    def find_save_location_and_execute(self):
        answer = self.check_inputs()
        if answer == False:
           return
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_path:
            self.entry_output_path_pdf.delete(0, tk.END)
            self.entry_output_path_pdf.insert(0, output_path)
            execute_mark_water(pdf_file_origin=self.entry_origin_path_pdf.get(), path_output_file=self.entry_output_path_pdf.get(), mark_water=self.entry_origin_path_image.get())
            self.clear_fields()

    def get_image(self):
        file_path = filedialog.askopenfilename(title="Selecione a Imagem", filetypes=(("Arquivos de Imagem", "*.png;*.jpg;*.jpeg"), ("Todos os Arquivos", "*.*")))
        self.entry_origin_path_image.delete(0, tk.END)  # Limpa o campo de entrada
        self.entry_origin_path_image.insert(0, file_path)  # Insere o caminho do arquivo selecionado no campo de entrada

    def check_inputs(self):
        if not self.entry_origin_path_pdf or self.entry_origin_path_pdf.get().strip() == '':
            self.message_error("Selecione algum arquivo PDF")
            return False
        if not self.entry_origin_path_image or self.entry_origin_path_image.get().strip() == '':
            self.message_error("É necessário uma foto ou um PDF para colocar como marca d'água")
            return False

    def clear_fields(self):
        self.entry_origin_path_pdf.delete(0, tk.END)       
        self.entry_origin_path_image.delete(0, tk.END)
        self.entry_output_path_pdf.delete(0, tk.END)

    def page_watermark(self, page):
        # CARREGAR PDF
        label_open_pdf = tk.Label(page, text="\n\n\n\nABRIR PDF")
        label_open_pdf.place(relx=0.2, rely=0.2, anchor=tk.CENTER)
        ico_open_folder = ImageTk.PhotoImage(self.icons.ico_open_folder)
        button_get_input_pdf = tk.Button(page, image=ico_open_folder, text='ABRIR', command=self.get_input_pdf, width=80, height=30, font=("Arial", 10), justify="center", anchor="center")
        button_get_input_pdf.image = ico_open_folder
        #button_get_input_pdf.grid(row=0, column=0, padx=5, pady=5, sticky='we',  anchor=tk.CENTER)
        button_get_input_pdf.place(relx=0.2, rely=0.2, anchor=tk.CENTER)
        ToolTip(button_get_input_pdf, "Abrir Arquivo PDF")

        self.entry_origin_path_pdf = tk.Entry(page, width=50)
        #self.entry_origin_path_pdf.grid(row=0, column=1, padx=5, pady=5)

        # MARCA D'AGUA
        label_imagem = tk.Label(page, text="\n\n\n\nMARCA D'ÁGUA")
        label_imagem.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
        ico_open_image = ImageTk.PhotoImage(self.icons.ico_open_image)
        botton_get_image = tk.Button(page, image=ico_open_image, command=self.get_image, width=80, height=30)
        botton_get_image.image = ico_open_image
        botton_get_image.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
        ToolTip(botton_get_image, "Abrir Imagem Marca d'água")


        self.entry_origin_path_image = tk.Entry(page, width=50)
        #self.entry_origin_path_image.grid(row=1, column=1, padx=5, pady=5, sticky='we')
 
        # CLEAR
        label_limpar = tk.Label(page, text="\n\n\n\nLIMPAR")
        label_limpar.place(relx=0.6, rely=0.2, anchor=tk.CENTER)
        ico_clear = ImageTk.PhotoImage(self.icons.ico_clear)
        button_clear_fields = tk.Button(page, image=ico_clear, command=self.clear_fields, width=70)
        button_clear_fields.image = ico_clear
        button_clear_fields.place(relx=0.6, rely=0.2, anchor=tk.CENTER)
        ToolTip(button_clear_fields, "Limpar")

        self.entry_output_path_pdf = tk.Entry(page, width=50)

        # SALVAR
        label_salvar = tk.Label(page, text="\n\n\n\nSALVAR")
        label_salvar.place(relx=0.8, rely=0.2, anchor=tk.CENTER)
        ico_save = ImageTk.PhotoImage(self.icons.ico_save)
        button_output_path_pdf = tk.Button(page, image=ico_save, command=self.find_save_location_and_execute,  width=70)
        button_output_path_pdf.image = ico_save
        button_output_path_pdf.place(relx=0.8, rely=0.2, anchor=tk.CENTER)
        ToolTip(button_output_path_pdf, "Salvar", follow=True, delay=0)


        




