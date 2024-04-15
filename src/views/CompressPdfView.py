import tkinter as tk
from tkinter import filedialog
from src.repository.compress_pdf import execute_compress
from PIL import Image, ImageTk
from src.views.ModalsView import ModalsView
import tkinter.ttk as ttk
from src.views.Images import Icons
from tktooltip  import ToolTip

class CompressPdfView(ModalsView):
      
    def __init__(self):
        self.icons = Icons()
        #entrada do PDF
        self.entry_origin_path_pdf = None
        # Saida do PDF
        self.entry_output_path_pdf = None
        # Entrada da imagem
        self.check_var = True
        self.label_percentage = None
        self.percentage = 100

    def get_input_pdf(self):
        file_path = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.entry_origin_path_pdf.delete(0, tk.END)
            self.entry_origin_path_pdf.insert(0, file_path)


    def find_save_location_and_execute(self):
        answer = self.check_inputs()
        if answer == False:
            return False
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if save_path:
            self.entry_output_path_pdf.delete(0, tk.END)
            self.entry_output_path_pdf.insert(0, save_path)
            execute_compress(pdf_file_origin=self.entry_origin_path_pdf.get(), path_output_file=self.entry_output_path_pdf.get(), quality_dpi=self.percentage) 
            self.clear_fields()

    def clear_fields(self):
        self.entry_origin_path_pdf.delete(0, tk.END)
        self.entry_output_path_pdf.delete(0, tk.END)
        self.alternar_valor(value=True)

    def check_inputs(self):
        if not self.entry_origin_path_pdf or self.entry_origin_path_pdf.get().strip() == '':
            self.message_error("Selecione algum arquivo PDF")
            return False
        if self.percentage == 100:
            self.message_error("É necessário uma informar um valor de redução da qualidade")
            return False
        
    def page_compress(self, page):

        self.check_var = tk.BooleanVar()
        # CARREGAR PDF
        label_open_pdf = tk.Label(page, text="\n\n\n\nABRIR PDF")
        label_open_pdf.place(relx=0.2, rely=0.2, anchor=tk.CENTER)
        ico_open_folder = ImageTk.PhotoImage(self.icons.ico_open_folder)
        button_get_input_pdf = tk.Button(page, image=ico_open_folder, text='ABRIR', command=self.get_input_pdf, width=80, height=30, font=("Arial", 10), justify="center", anchor="center")
        button_get_input_pdf.image = ico_open_folder
        button_get_input_pdf.place(relx=0.2, rely=0.2, anchor=tk.CENTER)
        ToolTip(button_get_input_pdf, "Abrir Arquivo PDF")

        self.entry_origin_path_pdf = tk.Entry(page, width=50)

         # PORCENTAGEM DE SAIDA
        label_percetage_output = tk.Label(page, text="\n\n\n\n% SAIDA")
        label_percetage_output.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
        ico_percetage_output = ImageTk.PhotoImage(self.icons.ico_percentage)
        botton_make_grio = tk.Button(page, image=ico_percetage_output, command=self.alternar_valor, width=80, height=30)
        botton_make_grio.image = ico_percetage_output
        botton_make_grio.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
        ToolTip(botton_make_grio, "% referente ao arquivo original")

        # CLEAR
        label_limpar = tk.Label(page, text="\n\n\n\nLIMPAR")
        label_limpar.place(relx=0.6, rely=0.2, anchor=tk.CENTER)
        ico_clear = ImageTk.PhotoImage(self.icons.ico_clear)
        button_clear_fields = tk.Button(page, image=ico_clear, command=self.clear_fields, width=70)
        button_clear_fields.image = ico_clear
        button_clear_fields.place(relx=0.6, rely=0.2, anchor=tk.CENTER)#.grid(row=0, column=2, padx=5, pady=5, sticky='we')
        ToolTip(button_clear_fields, "Limpar")
        self.entry_output_path_pdf = tk.Entry(page, width=50)

        # SALVAR
        label_salvar = tk.Label(page, text="\n\n\n\nSALVAR")
        label_salvar.place(relx=0.8, rely=0.2, anchor=tk.CENTER)
        ico_save = ImageTk.PhotoImage(self.icons.ico_save)
        button_output_path_pdf = tk.Button(page, image=ico_save, command=self.find_save_location_and_execute,  width=70)
        button_output_path_pdf.image = ico_save
        button_output_path_pdf.place(relx=0.8, rely=0.2, anchor=tk.CENTER)#grid(row=1, column=2, padx=5, pady=5, sticky='we')
        ToolTip(button_output_path_pdf, "Salvar", follow=True, delay=0)


        self.label_percentage = tk.Label(page, text=0, width=50, font=('Arial Black', 14))
        self.label_percentage.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        label_info = tk.Label(page, text="% do arquivo original", width=50)
        label_info.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    def alternar_valor(self, value:bool=None):
        '''
            -> value - Se estiver em True serve para deixar no padrão default
        '''
        if value == True:
           self.percentage = 100 
        else:
            self.percentage -= 10
            if self.percentage == 0:
                self.percentage = 100
        self.label_percentage.config(text=str(self.percentage))