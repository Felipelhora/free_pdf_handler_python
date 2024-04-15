import tkinter as tk
from tkinter import filedialog
from src.repository.protect_pdf import execute_protect
from PIL import Image, ImageTk
from src.views.ModalsView import ModalsView
import tkinter.ttk as ttk
from src.views.Images import Icons
from tktooltip  import ToolTip

class ProtegerView(ModalsView):
      
    def __init__(self):
        
        
        self.icons = Icons()
        #entrada do PDF
        self.entry_origin_path_pdf = None
        # Saida do PDF
        self.entry_output_path_pdf = None
        self.entry_password = None
        self.eye_icon_visible = False

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
            execute_protect(pdf_file_origin=self.entry_origin_path_pdf.get(),path_output_file=self.entry_output_path_pdf.get(), password=self.entry_password.get())
            self.clear_fields()


    def toggle_password_visibility(self, value:bool=None):
        if value == True:
           self.entry_password.config(show="*")
           self.eye_icon_visible = not self.eye_icon_visible
           return
        if self.eye_icon_visible:
            self.entry_password.config(show="*")
        else:
            self.entry_password.config(show="")
        self.eye_icon_visible = not self.eye_icon_visible

    def clear_fields(self):
        self.entry_origin_path_pdf.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_output_path_pdf.delete(0, tk.END)
        self.toggle_password_visibility(True)

    def check_inputs(self):
        if not self.entry_origin_path_pdf or self.entry_origin_path_pdf.get().strip() == '':
            self.message_error("Selecione algum arquivo PDF")
            return False
        if not self.entry_password or self.entry_password.get().strip() == '':
            self.message_error("É necessário digitar uma senha")
            return False

    def page_protect(self, page):
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

         # ver a senha
        label_to_see_pass = tk.Label(page, text="\n\n\n\nVER SENHA")
        label_to_see_pass.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
        ico_to_see_pass = ImageTk.PhotoImage(self.icons.ico_to_see)
        botton_make_grio = tk.Button(page, image=ico_to_see_pass, command=self.toggle_password_visibility, width=80, height=30)
        botton_make_grio.image = ico_to_see_pass
        botton_make_grio.place(relx=0.4, rely=0.2, anchor=tk.CENTER)
        ToolTip(botton_make_grio, "ver/esconder a senha")

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

        self.entry_password = tk.Entry(page, show="*", width=20)
        self.entry_password.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        label_info = tk.Label(page, text="SENHA", width=50, font=("Arial", 14))
        label_info.place(relx=0.5, rely=0.45, anchor=tk.CENTER)


        

        '''  def alternar_valor(self, value:bool=None):
        '''
            #-> value - Se estiver em True serve para deixar no padrão default
        '''
        if value == True:
           self.percentage = 100 
        else:
            self.percentage -= 10
            if self.percentage == 0:
                self.percentage = 100
        self.label_percentage.config(text=str(self.percentage))'''
        ''' label_file_path = tk.Label(page, text="Origem")
        label_file_path.grid(row=0, column=0, sticky="w")

        self.entry_origin_path_pdf = tk.Entry(page, width=50)
        self.entry_origin_path_pdf.grid(row=0, column=1, padx=5, pady=5)

        button_browse = tk.Button(page, text="Abrir", command=self.browse_folder_and_file)
        button_browse.grid(row=0, column=2, padx=5, pady=5)

        label_password = tk.Label(page, text="Senha:")
        label_password.grid(row=1, column=0, sticky="w")

        self.entry_password = tk.Entry(page, show="*", width=20)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        # Load the eye icon
        eye_icon = Image.open("eye_icon.png")
        eye_icon = eye_icon.resize((20, 20))
        eye_icon = ImageTk.PhotoImage(eye_icon)

        # Button to toggle password visibility
        toggle_visibility_button = tk.Button(page, image=eye_icon, command=self.toggle_password_visibility)
        toggle_visibility_button.image = eye_icon
        toggle_visibility_button.grid(row=1, column=2, padx=5, pady=5)

        label_save_path = tk.Label(page, text="Destino")
        label_save_path.grid(row=2, column=0, sticky="w")

        self.entry_output_path_pdf = tk.Entry(page, width=50)
        self.entry_output_path_pdf.grid(row=2, column=1, padx=5, pady=5)

        button_save_path = tk.Button(page, text="Escolher", command=self.browse_folder_for_save_path)
        button_save_path.grid(row=2, column=2, padx=5, pady=5)

        button_clear_fields = tk.Button(page, text="Limpar Campos", command=self.clear_fields)
        button_clear_fields.grid(row=3, column=0, columnspan=3, pady=5)

        button_protect = tk.Button(page, text="Executar", command=self.protect_pdf)
        button_protect.grid(row=4, column=0, columnspan=3, pady=10)

'''