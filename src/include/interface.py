import customtkinter
from tkinter import *

janela = customtkinter.CTk()

#Classe tela principal
class Application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.telaOpcoes()
        janela.mainloop()

    #Define o tema
    def tema(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    #Ajusta a tela
    def tela(self):
        janela.title("Gerenciador de Garagem")
        #Dimensão da janela
        altura = 400
        largura = 700

        #Dimensão do nosso sistema
        altura_screen = janela.winfo_screenheight()
        largura_screen = janela.winfo_screenwidth()

        #Posição da janela
        posx = (largura_screen / 2) - (largura / 2)
        posy = (altura_screen / 2) - (altura / 2)

        #Definindo geometry centralizado
        janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        janela.resizable(False, False)

    #Método com as requisitos funcionais
    def telaOpcoes(self):
        #Trabalhando com a logo
        img = PhotoImage(file="logo1.png")
        label_img = customtkinter.CTkLabel(master=janela, image=img)
        label_img.place(x=-25, y=30)

        #Frame Opções
        frame = customtkinter.CTkFrame(janela, width=350, height=396)
        frame.pack(side=RIGHT)

        #Frame widget
        font = customtkinter.CTkFont(family="Roboto", size=16)
        botao1 = customtkinter.CTkButton(master=frame, text="Cadastrar usuário", width=300, height=30,  font=("Roboto", 16)).place(x=25, y=60)

        botao2 = customtkinter.CTkButton(master=frame, text="Pesquisar usuário", width=300, height=30,  font=("Roboto", 16)).place(x=25, y=100)

        botao3 = customtkinter.CTkButton(master=frame, text="Cadastrar veículo", width=300, height=30,  font=("Roboto", 16)).place(x=25, y=140)

        botao4 = customtkinter.CTkButton(master=frame, text="Pesquisar veículo", width=300, height=30,  font=("Roboto", 16)).place(x=25, y=180)

        botao5 = customtkinter.CTkButton(master=frame, text="Histórico de vendas", width=300, height=30,  font=("Roboto", 16)).place(x=25, y=220)

        botao6 = customtkinter.CTkButton(master=frame, text="Realizar venda", width=300, height=30,  font=("Roboto", 16)).place(x=25, y=260)

Application()
