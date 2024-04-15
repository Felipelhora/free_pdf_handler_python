import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from src.views.ModalsView import ModalsView
from src.views.Images import Icons
from tktooltip  import ToolTip
from src.repository.checker_parameters import decode_input_with_str_to_list_int, get_pages_inside_range
from src.repository.pdf_info import pdf_info
from src.repository.rotate_pdf import rotate_pdf

from PIL import Image, ImageTk

class RotatePdf(ModalsView):
    
    def __init__(self):
        self.icons = Icons()
        #entrada do PDF
        self.entry_origin_path_pdf = None
        # Saida do PDF
        self.entry_output_path_pdf = None
        # Entrada da imagem
        self.check_var = True
        self.grau = 0
        self.label_grau = None
        self.entry_graus = None

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
            if self.check_var.get() == True:
                answer_pdf_info = pdf_info(file_path=self.entry_origin_path_pdf.get())
                if answer_pdf_info[1] != False:
                    total_paginas = answer_pdf_info[0]['total_pages']
                    list_pages = get_pages_inside_range([1,total_paginas])
                    rotate_pdf(pdf_file_origin=self.entry_origin_path_pdf.get(), path_output_file=self.entry_output_path_pdf.get(), grau=self.grau, list_pages=list_pages)
                    return 
            else:
                list_pages = decode_input_with_str_to_list_int(self.entry_graus.get())
                rotate_pdf(pdf_file_origin=self.entry_origin_path_pdf.get(), path_output_file=self.entry_output_path_pdf.get(), grau=self.grau, list_pages=list_pages)

    def clear_fields(self):
        self.entry_origin_path_pdf.delete(0, tk.END)
        self.entry_output_path_pdf.delete(0, tk.END)
        self.alternar_valor(True)
        if self.entry_graus['state'] == 'normal':
           self.entry_graus.delete(0, tk.END)

    def check_inputs(self):
        if not self.entry_origin_path_pdf or self.entry_origin_path_pdf.get().strip() == '':
            self.message_error("Selecione algum arquivo PDF")
            return False
        if self.check_var.get() == False and self.entry_graus.get() == None or self.check_var.get() == False and self.entry_graus.get().strip() == '': # and self.entry_graus == None or self.check_var.get() == False and len(self.entry_graus) == '' or self.check_var.get() == False and self.entry_graus == ' '
            self.message_error("É necessário indicar as páginas que serão rotacionadas se o campo 'Todas Páginas' não estiver selecionado")
            return False
        if self.grau == 0:
            self.message_error("O valor de rotação não poderá ser 0")
            return False

    def toggle_entry_state(self):
        if self.check_var.get():
          self.entry_graus['state'] = 'disabled'
          self.entry_graus.delete(0, tk.END)
        else:
           self.entry_graus['state'] = 'normal'
           self.entry_graus.delete(0, tk.END)

    def page_rotate(self, page):

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

         # SENTIDO DO GIRO
        label_sentido_giro = tk.Label(page, text="\n\n\n\nºGRAU")
        label_sentido_giro.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
        ico_sentido_giro = ImageTk.PhotoImage(self.icons.ico_clockwise)
        botton_make_grio = tk.Button(page, image=ico_sentido_giro, command=self.alternar_valor, width=80, height=30)
        botton_make_grio.image = ico_sentido_giro
        botton_make_grio.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
        ToolTip(botton_make_grio, "Rotacionar sentido horário")

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
        button_output_path_pdf.place(relx=0.8, rely=0.2, anchor=tk.CENTER)#grid(row=1, column=2, padx=5, pady=5, sticky='we')
        ToolTip(button_output_path_pdf, "Salvar", follow=True, delay=0)

        self.label_grau = tk.Label(page, text=0, width=50, font=('Arial Black', 14))
        self.label_grau.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        self.check_var = tk.BooleanVar()
        self.check_var.set(True)  # Inicia com o Entry desabilitado
        self.check_button = tk.Checkbutton(page, text="Todas Páginas", variable=self.check_var, command=self.toggle_entry_state)
        self.check_button.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.entry_graus = tk.Entry(page, width=50)
        self.entry_graus.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.entry_graus.config(state="disabled")

        label_info = tk.Label(page, text="Digite números de página separados por vírgulas( ',' ) \ne/ou intervalos de páginas com traço ( '-' ) Ex. 1,3-5 ", width=50)
        label_info.place(relx=0.5, rely=0.66, anchor=tk.CENTER)

    def alternar_valor(self, value:bool=None):
        '''
            -> value - Se estiver em True serve para zerar o contador
        '''
        if value == True:
           self.grau = 0 
        else:
            self.grau += 90
            if self.grau > 270:
                self.grau = 0
        self.label_grau.config(text=str(self.grau))
