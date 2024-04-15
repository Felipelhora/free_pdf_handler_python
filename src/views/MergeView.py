import tkinter as tk
from tkinter import filedialog
from src.repository.merge_pdf import merge_pdf, execute_merge
from tkinter import messagebox, PhotoImage
import os
from src.views.ModalsView import ModalsView
import tkinter.ttk as ttk
from src.views.Images import Icons
from tktooltip  import ToolTip
from PIL import Image, ImageTk
class MergeView(ModalsView):
      
    def __init__(self):

        # Saida do PDF
        self.entry_output_path_pdf = None
        # Labels
        self.label = None
        self.icons = Icons()
        # Variáveis de uso
        self.delete_file_button = None
        self.file_paths = [] # lista de arquivos salvos
        self.file_paths_listbox = None # função para lista
        self.selected_index = None # Variável para selecionar a ordem junto a lista

    # Método para excluir o arquivo selecionado da lista
    def delete_selected_file(self):
        selected_index = self.file_paths_listbox.curselection()
        if selected_index:
            del self.file_paths[selected_index[0]]
            self.update_file_paths_listbox()
            # Verifica se algum item está selecionado após a exclusão
   
    # Método para atualizar a lista de caminhos de arquivo
    def update_file_paths_listbox(self):
        # Limpa a lista antes de atualizá-la
        self.file_paths_listbox.delete(0, tk.END)
        # Adiciona os nomes dos arquivos à lista
        for idx, file_path in enumerate(self.file_paths, start=1):
            file_name = os.path.basename(file_path)
            self.file_paths_listbox.insert(tk.END, f"{idx}. {file_name}")

    # Método para carregar os arquivos
    def get_input_pdf(self):
        new_file_paths = filedialog.askopenfilenames(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if new_file_paths:
            self.file_paths.extend(new_file_paths)  # Adiciona novos caminhos à lista
            self.update_file_paths_listbox()

    # Método para localizar o local para salvar e capturar nome e endereço
    def find_save_location_and_execute(self):
        answer = self.check_inputs()
        if answer == False:
            return False
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.entry_output_path_pdf.delete(0, tk.END)
            self.entry_output_path_pdf.insert(0, file_path)
            execute_merge(files=self.file_paths, path_output_file=self.entry_output_path_pdf.get())
            self.clear_fields()
        
   # Método para mover um arquivo para cima na lista
    def move_up(self):
        selected_index = self.file_paths_listbox.curselection()
        if selected_index and selected_index[0] > 0:
            self.selected_index = selected_index[0] - 1
            self.file_paths.insert(self.selected_index, self.file_paths.pop(selected_index[0]))
            self.update_file_paths_listbox()
            self.file_paths_listbox.select_set(self.selected_index)

    # Método para mover um arquivo para baixo na lista
    def move_down(self):
        selected_index = self.file_paths_listbox.curselection()
        if selected_index and selected_index[0] < len(self.file_paths) - 1:
            self.selected_index = selected_index[0] + 1
            self.file_paths.insert(self.selected_index, self.file_paths.pop(selected_index[0]))
            self.update_file_paths_listbox()
            self.file_paths_listbox.select_set(self.selected_index)

    # Método para limpar a lista de arquivos e os dados de execução
    def clear_fields(self):
        self.file_paths = []
        self.file_paths_listbox.delete(0, tk.END)
        self.entry_output_path_pdf.delete(0, tk.END)


    # Método para executar a ação de merge
    def check_inputs(self) -> None:
        if len(self.file_paths) == 0:
            self.message_error('Por favor escolha os aquivos que deseja juntar')
            return False
        

    # Método para criar a página "JUNTAR" da interface
    def page_merge(self, page):
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
        label_limpar.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        ico_clear = ImageTk.PhotoImage(self.icons.ico_clear)
        button_clear_fields = tk.Button(page, image=ico_clear, command=self.clear_fields, width=70)
        button_clear_fields.image = ico_clear
        button_clear_fields.place(relx=0.5, rely=0.2, anchor=tk.CENTER)#.grid(row=0, column=2, padx=5, pady=5, sticky='we')
        ToolTip(button_clear_fields, "Limpar")
        self.entry_output_path_pdf = tk.Entry(page, width=50)

        # SALVAR
        label_salvar = tk.Label(page, text="\n\n\n\nSALVAR")
        label_salvar.place(relx=0.7, rely=0.2, anchor=tk.CENTER)
        ico_save = ImageTk.PhotoImage(self.icons.ico_save)
        button_output_path_pdf = tk.Button(page, image=ico_save, command=self.find_save_location_and_execute,  width=70)
        button_output_path_pdf.image = ico_save
        button_output_path_pdf.place(relx=0.7, rely=0.2, anchor=tk.CENTER)#grid(row=1, column=2, padx=5, pady=5, sticky='we')
        ToolTip(button_output_path_pdf, "Salvar", follow=True, delay=0)


        # BOTÃO PARA CIMA
        label_subir = tk.Label(page, text="\n\n\n\nSUBIR ITEM")
        label_subir.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
        ico_up = ImageTk.PhotoImage(self.icons.ico_up)
        button_up_list = tk.Button(page, image=ico_up,  width=70, command=self.move_up)
        button_up_list.image = ico_up
        button_up_list.place(relx=0.3, rely=0.4, anchor=tk.CENTER)#grid(row=1, column=2, padx=5, pady=5, sticky='we')
        ToolTip(button_up_list, "SUBIR ITEM DA LISTA", follow=True, delay=0)

        # BOTÃO PARA BAIXO
        label_subir = tk.Label(page, text="\n\n\n\nSUBIR ITEM")
        label_subir.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        ico_down = ImageTk.PhotoImage(self.icons.ico_down)
        button_down_list = tk.Button(page, image=ico_down,  width=70, command=self.move_down)
        button_down_list.image = ico_down
        button_down_list.place(relx=0.5, rely=0.4, anchor=tk.CENTER)#grid(row=1, column=2, padx=5, pady=5, sticky='we')
        ToolTip(button_down_list, "DESCER ITEM DA LISTA", follow=True, delay=0)

        # DELETAR DA LISTA
        label_subir = tk.Label(page, text="\n\n\n\nDELETAR ITEM")
        label_subir.place(relx=0.7, rely=0.4, anchor=tk.CENTER)
        ico_delete = ImageTk.PhotoImage(self.icons.ico_delete)
        button_delete_item_list = tk.Button(page, image=ico_delete,  width=70, command=self.delete_selected_file)
        button_delete_item_list.image = ico_delete
        button_delete_item_list.place(relx=0.7, rely=0.4, anchor=tk.CENTER)#grid(row=1, column=2, padx=5, pady=5, sticky='we')
        ToolTip(button_delete_item_list, "DELETAR ITEM DA LISTA", follow=True, delay=0)
        
        # Adicionando barra de rolagem à lista de caminhos de arquivos
        self.file_paths_listbox = tk.Listbox(page, width=50, height=10, selectmode=tk.SINGLE, font=("Arial", 12))
        self.file_paths_listbox.place(relx=0.47, rely=0.7, anchor=tk.CENTER)#pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(page, orient=tk.VERTICAL)
        scrollbar.place(relx=0.92, rely=0.7, anchor=tk.CENTER)
        self.file_paths_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.file_paths_listbox.yview)

      