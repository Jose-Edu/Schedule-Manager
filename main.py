"""
    Arquivo principal do projeto.
    Cria e roda a janela principal.
    Execute este arquivo para iniciar o App.
    (WIP)
"""


# Importa o tkinter para trabalhar a interface gráfica
import tkinter as tk


# Classe principal do projeto. Define a janela base do programa 
class main:


    def __init__(self) -> None:
        self.app = tk.Tk()
        self.app.title('Schedule Manager')
        self.app.geometry('800x600')
        self.main_frame = tk.Frame(self.app, background='lightgray').pack(expand='True', fill='both')
        

# Atribui a classe main à root, executa o mainloop do programa
if __name__ == '__main__':

    root = main()
    root.app.mainloop()
