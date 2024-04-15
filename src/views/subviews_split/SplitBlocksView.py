import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from src.views.ModalsView import ModalsView
from src.repository.split_pdf import make_list_blocks, execute_split_async
import tkinter.ttk as ttk
from src.views.Images import Icons
from tktooltip  import ToolTip
class SplitBlocksView(ModalsView):
    ...
    def __init__(self):
        self.icons = Icons()
        #entrada do PDF
        self.entry_origin_path_pdf = None
        # Saida do PDF
        self.entry_output_path_pdf = None
        self.entry_bloco_divisao = None

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
            list_blocks = make_list_blocks(pdf_file_origin=self.entry_origin_path_pdf.get(),value=int(self.entry_bloco_divisao.get()))
            if list_blocks != False:
                execute_split_async(pdf_file_origin=self.entry_origin_path_pdf.get(), path_output_file=self.entry_output_path_pdf.get(),arrays_blocks=list_blocks)
                self.clear_fields()

    def clear_fields(self):
        self.entry_origin_path_pdf.delete(0, tk.END)
        self.entry_bloco_divisao.delete(0, tk.END)
        self.entry_output_path_pdf.delete(0, tk.END)

    def check_inputs(self):
        if not self.entry_origin_path_pdf or self.entry_origin_path_pdf.get().strip() == '':
            self.message_error("Selecione algum arquivo PDF")
            return False
        if not self.entry_bloco_divisao or self.entry_bloco_divisao.get().strip() == '':
            self.message_error("É necessário indicar o valor do bloco")
            return False
        try:
            int(self.entry_bloco_divisao.get())
            return True
        except:
            self.message_error("O valor do bloco deve ser um número")
            return False
        
    def page_split_blocks(self, page):

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

        self.entry_bloco_divisao = tk.Entry(page, width=40)
        self.entry_bloco_divisao.place(relx=0.51, rely=0.4, anchor=tk.CENTER)

        label_info = tk.Label(page, text="Indique o tamanho do bloco de páginas \nque o arquivo será divido", width=50, font=("Arial", 10))
        label_info.place(relx=0.51, rely=0.5, anchor=tk.CENTER)

        label_info = tk.Label(page, text="Separa o arquivo em blocos de páginas com o valor escolhido", width=50, font=("Arial", 7, "italic"))
        label_info.place(relx=0.51, rely=0.7, anchor=tk.CENTER)