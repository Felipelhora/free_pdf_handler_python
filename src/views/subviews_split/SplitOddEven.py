import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from src.views.ModalsView import ModalsView
from src.repository.split_pdf import split_odd_even_async
import tkinter.ttk as ttk
from src.views.Images import Icons
from tktooltip  import ToolTip
class SplitOddEven(ModalsView):
    ...
    def __init__(self):


        self.icons = Icons()
        #entrada do PDF
        self.entry_origin_path_pdf = None
        # Saida do PDF
        self.entry_output_path_pdf = None
        self.var_par = True
        self.var_impar = True

    def get_input_pdf(self):
        file_path = filedialog.askopenfilename() #defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]
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
            split_odd_even_async(pdf_file_origin=self.entry_origin_path_pdf.get(), path_output_file=self.entry_output_path_pdf.get(), paramters=[self.var_par.get(), self.var_impar.get()])

    def clear_fields(self):
        self.entry_origin_path_pdf.delete(0, tk.END)
        self.entry_output_path_pdf.delete(0, tk.END)
        self.var_par.set(True)
        self.var_impar.set(True)
        
    def check_inputs(self):
        if not self.entry_origin_path_pdf or self.entry_origin_path_pdf.get().strip() == '':
            self.message_error("Selecione algum arquivo PDF")
            return False
        if self.var_par.get() == False and self.var_impar.get() == False:
            self.message_error("Pelo menos um dos campos PAR/IMPAR deve ser escolhido")
            return False
        
    def page_split_odd_even(self, page):
        self.check_var = tk.BooleanVar()
        # CARREGAR PDF
        label_open_pdf = tk.Label(page, text="\n\n\n\nABRIR PDF")
        label_open_pdf.place(relx=0.3, rely=0.2, anchor=tk.CENTER)
        ico_open_folder = ImageTk.PhotoImage(self.icons.ico_open_folder)
        button_get_input_pdf = tk.Button(page, image=ico_open_folder, text='ABRIR', command=self.get_input_pdf, width=80, height=30, font=("Arial", 10), justify="center", anchor="center")
        button_get_input_pdf.image = ico_open_folder
        button_get_input_pdf.place(relx=0.3, rely=0.2, anchor=tk.CENTER)
        ToolTip(button_get_input_pdf, "Abrir Arquivo PDF")

        self.entry_origin_path_pdf = tk.Entry(page, width=50)

        # CLEAR
        label_limpar = tk.Label(page, text="\n\n\n\nLIMPAR")
        label_limpar.place(relx=0.51, rely=0.2, anchor=tk.CENTER)
        ico_clear = ImageTk.PhotoImage(self.icons.ico_clear)
        button_clear_fields = tk.Button(page, image=ico_clear, command=self.clear_fields, width=70)
        button_clear_fields.image = ico_clear
        button_clear_fields.place(relx=0.51, rely=0.2, anchor=tk.CENTER)
        ToolTip(button_clear_fields, "Limpar")
        self.entry_output_path_pdf = tk.Entry(page, width=50)

        # SALVAR
        label_salvar = tk.Label(page, text="\n\n\n\nSALVAR")
        label_salvar.place(relx=0.7, rely=0.2, anchor=tk.CENTER)
        ico_save = ImageTk.PhotoImage(self.icons.ico_save)
        button_output_path_pdf = tk.Button(page, image=ico_save, command=self.find_save_location_and_execute,  width=70)
        button_output_path_pdf.image = ico_save
        button_output_path_pdf.place(relx=0.7, rely=0.2, anchor=tk.CENTER)
        ToolTip(button_output_path_pdf, "Salvar", follow=True, delay=0)


        self.var_par = tk.BooleanVar(value=True)
        self.var_impar = tk.BooleanVar(value=True)

        self.check_par = tk.Checkbutton(page, text="Páginas Pares", variable=self.var_par)
        self.check_par.place(relx=0.35, rely=0.4, anchor=tk.CENTER)

        self.check_impar = tk.Checkbutton(page, text="Páginas Ímpares", variable=self.var_impar)
        self.check_impar.place(relx=0.65, rely=0.4, anchor=tk.CENTER)