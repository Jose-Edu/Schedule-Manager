"""
    Arquivo principal do projeto.
    Cria e roda a janela principal.
    Execute este arquivo para iniciar o App.
    (WIP)
"""


# Importa o tkinter para trabalhar a interface gráfica
import tkinter as tk
# Importa o tkcalendar para utilizar o calendário
import tkcalendar as Calendar


# Classe principal do projeto. Define a janela base do programa 
class main:


    def __init__(self) -> None:
        self.app = tk.Tk()
        self.app.title('Schedule Manager')
        self.app.geometry('800x600')
        self.main_frame = tk.Frame(self.app, background='lightgray').pack(expand='True', fill='both')

        # Criando o calendário
        self.calendar = Calendar.Calendar(self.main_frame, selectmode="day", date_pattern="dd/MM/yyyy")
        self.calendar.pack(side= "top", expand="true",fill="both", padx=20, pady=20)
        

    def clean_window(self) -> None:
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.app, background='lightgray').pack(expand='True', fill='both')

    
# Atribui a classe main à root. Executa o mainloop do programa
if __name__ == '__main__':

    root = main()
    root.app.mainloop()

