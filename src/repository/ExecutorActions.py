import threading
from src.views.ModalsView import ModalsView



# Classe para executar de forma paralela as ações com o modal loadgin e destravar a tela

class ExecutorActions:

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.thread = None
        self.modals_view = ModalsView()

    def _execute_function(self):
        self.result = self.func(*self.args, **self.kwargs)

    def execute_with_loading(self):
        self.thread = threading.Thread(target=self._execute_with_loading)
        self.thread.start()

    def _execute_with_loading(self):
        self.modals_view.show_loading_circle()
        self._execute_function()
        try:
            self.modals_view.close_loading_screen()
        except:
            ...
        

    def wait_until_finish(self):
        if self.thread:
            self.thread.join()

    def get_result(self):
        self.wait_until_finish()
        return self.result