import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from src.views.ModalsView import ModalsView
from src.repository.split_pdf import execute_split_async
import tkinter.ttk as ttk
from src.views.Images import Icons
from tktooltip  import ToolTip
from src.repository.checker_parameters import decode_input_with_str_to_list_blocks
from src.repository.pdf_info import pdf_info

class SplitFreeChoises(ModalsView):
            
    def __init__(self):
        self.icons = Icons()
        #entrada do PDF
        self.entry_origin_path_pdf = None
        # Saida do PDF
        self.entry_output_path_pdf = None
        self.entry_bloco_divisao = None
    

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
            answer_pdf_info = pdf_info(self.entry_origin_path_pdf.get())
            if answer_pdf_info[1] != False:
                total_pages = answer_pdf_info[0]['total_pages']
                list_pages = decode_input_with_str_to_list_blocks(input_str=self.entry_bloco_divisao.get(), len_pages=total_pages)
                if list_pages != False:
                    execute_split_async(
                                            pdf_file_origin=self.entry_origin_path_pdf.get(),
                                            path_output_file=self.entry_output_path_pdf.get(),  
                                            arrays_blocks=list_pages)
                    self.clear_fields()
                else:
                    return False
            else:
                return False
            
    def clear_fields(self):
        self.entry_origin_path_pdf.delete(0, tk.END)
        self.entry_output_path_pdf.delete(0, tk.END)
        self.entry_bloco_divisao.delete(0, tk.END)

    def check_inputs(self):
        if not self.entry_origin_path_pdf or self.entry_origin_path_pdf.get().strip() == '':
           self.message_error("Selecione algum arquivo PDF")
           return False
        if self.entry_bloco_divisao.get() == None or self.entry_bloco_divisao.get().strip() == '':
           self.message_error("É necessário indicar as páginas que serão retiradas")
           return False

      
    def page_split_free_choises(self, page):
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

        self.entry_bloco_divisao = tk.Entry(page, width=50)
        self.entry_bloco_divisao.place(relx=0.51, rely=0.4, anchor=tk.CENTER)

        label_info = tk.Label(page, text="Digite números de página retiradas usando vírgulas( ',' ) \ne/ou intervalos de páginas com traço ( '-' ) Ex. 1,3-5 ", width=50)
        label_info.place(relx=0.51, rely=0.5, anchor=tk.CENTER)


        label_info_2 = tk.Label(page, text="Cria um arquivo separado para cada\n página ou range de páginas indicado", width=50, font=("Arial", 7, "italic"))
        label_info_2.place(relx=0.51, rely=0.7, anchor=tk.CENTER)