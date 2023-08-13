from tkinter import *
# serve para "setar" o caminho das imagens dinamicamente
from sys import path
import customtkinter

import sqlite3

janela = customtkinter.CTk()

# Tela principal
class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.telaOpcoes()
        janela.mainloop()

    # Define o tema
    def tema(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    # Ajusta a tela
    def tela(self):
        janela.title("Gerenciador de Garagem")
        # Dimensão da janela
        altura = 600
        largura = 700

        # Dimensão do nosso sistema
        alturaTela = janela.winfo_screenheight()
        larguraTela = janela.winfo_screenwidth()

        # Posição da janela
        posx = (larguraTela / 2) - (largura / 2)
        posy = (alturaTela / 2) - (altura / 2)

        # Definindo geometry centralizado
        janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        janela.resizable(False, False)

    # Método com as requisitos funcionais
    def telaOpcoes(self):

        # definindo a logo da primeira tela
        caminhoDaImagem = path[0] + '/img/logoPrincipal.png'
        # TODO:
        # realizar a leitura da imagem sem warnings
        img = PhotoImage(file = caminhoDaImagem)

        label_img = customtkinter.CTkLabel(master=janela, image=img)
        label_img.place(x=-25, y=30)

        # Frame Opções
        frame = customtkinter.CTkFrame(janela, width=350, height=396)
        frame.pack(side=RIGHT)

        # Frame widget
        font = customtkinter.CTkFont(family="Roboto", size=16)

        # Variáveis que serão armazenadas no registro do funcionário
        nome = customtkinter.StringVar(janela)
        enderecoSave = customtkinter.StringVar(janela)
        numeroSave = customtkinter.StringVar(janela)
        bairroSave = customtkinter.StringVar(janela)
        cepSave = customtkinter.StringVar(janela)
        telefoneSave = customtkinter.StringVar(janela)
        emailSave = customtkinter.StringVar(janela)
        cargoSave = customtkinter.StringVar(janela)
        salarioSave = customtkinter.StringVar(janela)

        # Variáveis que serão armazenadas no registro de clientes
        cpfClienteSave = customtkinter.StringVar(janela)
        nomeClienteSave = customtkinter.StringVar(janela)
        enderecoClienteSave = customtkinter.StringVar(janela)
        numeroClienteSave = customtkinter.StringVar(janela)
        bairroClienteSave = customtkinter.StringVar(janela)
        cepClienteSave = customtkinter.StringVar(janela)
        telefoneClienteSave = customtkinter.StringVar(janela)
        emailClienteSave = customtkinter.StringVar(janela)
        nomeEmpresaClienteSave = customtkinter.StringVar(janela)
        cnpjClienteSave = customtkinter.StringVar(janela)

        # Variáveis que serão armazenadas no registro de clientes
        modeloVeiculoSave = customtkinter.StringVar(janela)
        marcaVeiculoSave = customtkinter.StringVar(janela)
        anoVeiculoSave = customtkinter.StringVar(janela)
        corVeiculoSave = customtkinter.StringVar(janela)
        precoVeiculoSave = customtkinter.StringVar(janela)
        placaVeiculoSave = customtkinter.StringVar(janela)
        kmRodadoSave = customtkinter.StringVar(janela)

        # Váriavel para pesquisar funcionário
        nomeFuncPesquisarSave = customtkinter.StringVar(janela)

        # Variável para pesquisar cliente
        nomePesquisarClienteSave = customtkinter.StringVar(janela)

        # Variável para pesquisar veículo 
        modeloVeiculoPesquisarSave = customtkinter.StringVar(janela)

        def printnome():
            print("Inisira a função no command=")

        # Tela para cadastrar Funcionario
        def telaCadastrarFuncionario():
            frame.pack_forget()

            # Frame com os dados do funcionario
            frameFuncionario = customtkinter.CTkFrame(janela, width=350, height=600)
            frameFuncionario.pack(side=RIGHT)

            # Frame com os títulos
            frameLabelFuncionario = customtkinter.CTkFrame(janela, width=350, height=600)
            frameLabelFuncionario.pack(side=LEFT)

            label = customtkinter.CTkLabel(master=frameFuncionario,
                                           text="Cadastrar Funcionario",
                                           ).place(x=25, y=5)

            # Títulos
            labelNomeFuncionario = customtkinter.CTkLabel(master=frameLabelFuncionario,
                                           text="Nome: ",
                                           ).place(x=280, y=40)

            labelEnderecoFuncionario = customtkinter.CTkLabel(master=frameLabelFuncionario,
                                           text="Endereço: ",
                                           ).place(x=280, y=80)

            labelNumeroFuncionario = customtkinter.CTkLabel(master=frameLabelFuncionario,
                                           text="Número: ",
                                           ).place(x=280, y=120)

            labelBairroFuncionario = customtkinter.CTkLabel(master=frameLabelFuncionario,
                                           text="Bairro: ",
                                           ).place(x=280, y=160)

            labelCepFuncionario = customtkinter.CTkLabel(master=frameLabelFuncionario,
                                           text="Cep: ",
                                           ).place(x=280, y=200)

            labelTelefoneFuncionario = customtkinter.CTkLabel(master=frameLabelFuncionario,
                                           text="Telefone: ",
                                           ).place(x=280, y=240)

            labelEmailFuncionario = customtkinter.CTkLabel(master=frameLabelFuncionario,
                                           text="Email: ",
                                           ).place(x=280, y=280)

            labelCargoFuncionario = customtkinter.CTkLabel(master=frameLabelFuncionario,
                                           text="Cargo: ",
                                           ).place(x=280, y=320)

            labelSalarioFuncionario = customtkinter.CTkLabel(master=frameLabelFuncionario,
                                           text="Salário: ",
                                           ).place(x=280, y=360)

            # Entrada de dados
            nomeEntry = customtkinter.CTkEntry(master=frameFuncionario,
                                                      width=300,
                                                      textvariable=nome
                                                      ).place(x=25, y=40)

            enderecoEntry = customtkinter.CTkEntry(master=frameFuncionario,
                                                      textvariable=enderecoSave,
                                                      width=300
                                                      ).place(x=25, y=80)

            numeroEntry = customtkinter.CTkEntry(master=frameFuncionario,
                                                      textvariable=numeroSave,
                                                      width=300
                                                      ).place(x=25, y=120)

            bairroEntry = customtkinter.CTkEntry(master=frameFuncionario,
                                                      textvariable=bairroSave,
                                                      width=300
                                                      ).place(x=25, y=160)

            cepEntry = customtkinter.CTkEntry(master=frameFuncionario,
                                                      textvariable=cepSave,
                                                      width=300
                                                      ).place(x=25, y=200)

            telefoneEntry = customtkinter.CTkEntry(master=frameFuncionario,
                                                      textvariable=telefoneSave,
                                                      width=300
                                                      ).place(x=25, y=240)

            emailEntry = customtkinter.CTkEntry(master=frameFuncionario,
                                                      textvariable=emailSave,
                                                      width=300
                                                      ).place(x=25, y=280)

            cargoEntry = customtkinter.CTkEntry(master=frameFuncionario,
                                                      textvariable=cargoSave,
                                                      width=300
                                                      ).place(x=25, y=320)

            salarioEntry = customtkinter.CTkEntry(master=frameFuncionario,
                                                      textvariable=salarioSave,
                                                      width=300
                                                      ).place(x=25, y=360)

            saveFuncionario = customtkinter.CTkButton(master=frameFuncionario, 
                                         text="Cadastrar Funcionário", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="green",
                                         hover_color="#014B05",
                                         command=printnome
                                         ).place(x=25, y=480)

            # Volta para tela inicial
            def back():
                frameFuncionario.pack_forget()
                frameLabelFuncionario.pack_forget()
                frame.pack(side=RIGHT)

            voltar = customtkinter.CTkButton(master=frameFuncionario, 
                                         text="Voltar", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="gray",
                                         hover_color="#090909",
                                         command=back
                                         ).place(x=25, y=520)

        def telaCadastrarCliente():
            frame.pack_forget()

            # Frame com os dados do cliente
            frameCliente = customtkinter.CTkFrame(janela, width=350, height=600)
            frameCliente.pack(side=RIGHT)

            # Frame com os títulos
            frameLabelCliente = customtkinter.CTkFrame(janela, width=350, height=600)
            frameLabelCliente.pack(side=LEFT)

            label = customtkinter.CTkLabel(master=frameCliente,
                                           text="Cadastrar Cliente",
                                           ).place(x=25, y=5)

            # Títulos
            labelCpfCliente = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="CPF: ",
                                           ).place(x=280, y=40)

            labelNomeCliente = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="Nome: ",
                                           ).place(x=280, y=80)

            labelEnderecoCliente = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="Endereço: ",
                                           ).place(x=280, y=120)

            labelNumeroCliente = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="Número: ",
                                           ).place(x=280, y=160)

            labelBairroCliente = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="Bairro: ",
                                           ).place(x=280, y=200)

            labelCepCliente = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="Cep: ",
                                           ).place(x=280, y=240)

            labelTelefoneCliente = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="Telefone: ",
                                           ).place(x=280, y=280)

            labelEmailCliente = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="Email: ",
                                           ).place(x=280, y=320)

            labelNomeEmpresa = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="Empresa: ",
                                           ).place(x=280, y=360)

            labelCnpfCliente = customtkinter.CTkLabel(master=frameLabelCliente,
                                           text="CNPJ: ",
                                           ).place(x=280, y=400)


            # Entrada de dados
            cpfCliente = customtkinter.CTkEntry(master=frameCliente,
                                                      width=300,
                                                      textvariable=cpfClienteSave
                                                      ).place(x=25, y=40)

            nomeCliente = customtkinter.CTkEntry(master=frameCliente,
                                                      textvariable=nomeClienteSave,
                                                      width=300
                                                      ).place(x=25, y=80)

            enderecoCliente = customtkinter.CTkEntry(master=frameCliente,
                                                      textvariable=enderecoClienteSave,
                                                      width=300
                                                      ).place(x=25, y=120)

            numeroCliente = customtkinter.CTkEntry(master=frameCliente,
                                                      textvariable=numeroClienteSave,
                                                      width=300
                                                      ).place(x=25, y=160)

            bairroCliente = customtkinter.CTkEntry(master=frameCliente,
                                                      textvariable=bairroClienteSave,
                                                      width=300
                                                      ).place(x=25, y=200)

            cepCliente = customtkinter.CTkEntry(master=frameCliente,
                                                      textvariable=cepClienteSave,
                                                      width=300
                                                      ).place(x=25, y=240)

            telefoneCliente = customtkinter.CTkEntry(master=frameCliente,
                                                      textvariable=telefoneClienteSave,
                                                      width=300
                                                      ).place(x=25, y=280)

            emailCliente = customtkinter.CTkEntry(master=frameCliente,
                                                      textvariable=emailClienteSave,
                                                      width=300
                                                      ).place(x=25, y=320)

            nomeEmpresa = customtkinter.CTkEntry(master=frameCliente,
                                                      textvariable=nomeEmpresaClienteSave,
                                                      width=300
                                                      ).place(x=25, y=360)

            cnpjCliente = customtkinter.CTkEntry(master=frameCliente,
                                                      textvariable=cnpjClienteSave,
                                                      width=300
                                                      ).place(x=25, y=400)

            saveFuncionario = customtkinter.CTkButton(master=frameCliente, 
                                         text="Cadastrar Funcionário", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="green",
                                         hover_color="#014B05",
                                         command=printnome
                                         ).place(x=25, y=480)

            # Volta para tela inicial
            def back():
                frameCliente.pack_forget()
                frameLabelCliente.pack_forget()
                frame.pack(side=RIGHT)

            voltar = customtkinter.CTkButton(master=frameCliente, 
                                         text="Voltar", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="gray",
                                         hover_color="#090909",
                                         command=back
                                         ).place(x=25, y=520)

        # Tela para cadastrar Veiculo
        def telaCadastrarVeiculo():
            frame.pack_forget()

            # Frame com os dados do veiculo
            frameVeiculo = customtkinter.CTkFrame(janela, width=350, height=600)
            frameVeiculo.pack(side=RIGHT)

            # Frame com os títulos
            frameLabelVeiculo = customtkinter.CTkFrame(janela, width=350, height=600)
            frameLabelVeiculo.pack(side=LEFT)

            label = customtkinter.CTkLabel(master=frameVeiculo,
                                           text="Cadastrar Veiculo",
                                           ).place(x=25, y=5)

            # Título
            labelModelo = customtkinter.CTkLabel(master=frameLabelVeiculo,
                                           text="Modelo: ",
                                           ).place(x=280, y=40)

            labelMarca = customtkinter.CTkLabel(master=frameLabelVeiculo,
                                           text="Marca: ",
                                           ).place(x=280, y=80)

            labelAno = customtkinter.CTkLabel(master=frameLabelVeiculo,
                                           text="Ano: ",
                                           ).place(x=280, y=120)

            labelCor = customtkinter.CTkLabel(master=frameLabelVeiculo,
                                           text="Cor: ",
                                           ).place(x=280, y=160)

            labelPreco = customtkinter.CTkLabel(master=frameLabelVeiculo,
                                           text="Preço: ",
                                           ).place(x=280, y=200)

            labelPlaca = customtkinter.CTkLabel(master=frameLabelVeiculo,
                                           text="Placa: ",
                                           ).place(x=280, y=240)

            labelKmRodado = customtkinter.CTkLabel(master=frameLabelVeiculo,
                                           text="Km rodado: ",
                                           ).place(x=280, y=280)

            # Entrada de dados
            modeloVeiculo = customtkinter.CTkEntry(master=frameVeiculo,
                                                      width=300,
                                                      textvariable=modeloVeiculoSave,
                                                      ).place(x=25, y=40)

            marcaVeiculo = customtkinter.CTkEntry(master=frameVeiculo,
                                                      width=300,
                                                      textvariable=marcaVeiculoSave,
                                                      ).place(x=25, y=80)

            anoVeiculo = customtkinter.CTkEntry(master=frameVeiculo,
                                                      textvariable=anoVeiculoSave,
                                                      width=300).place(x=25, y=120)

            corVeiculo = customtkinter.CTkEntry(master=frameVeiculo,
                                                      textvariable=corVeiculoSave,
                                                      width=300).place(x=25, y=160)

            precoVeiculo = customtkinter.CTkEntry(master=frameVeiculo,
                                                      textvariable=precoVeiculoSave,
                                                      width=300).place(x=25, y=200)

            placaVeiculo = customtkinter.CTkEntry(master=frameVeiculo,
                                                    textvariable=placaVeiculoSave,
                                                      width=300).place(x=25, y=240)

            kmRodadoVeiculo = customtkinter.CTkEntry(master=frameVeiculo,
                                                      textvariable=kmRodadoSave,
                                                      width=300).place(x=25, y=280)

            # Botão save
            saveVeiculo = customtkinter.CTkButton(master=frameVeiculo, 
                                         text="Cadastrar Veículo", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="green",
                                         hover_color="#014B05",
                                         command=printnome
                                         ).place(x=25, y=480)

            # Volta para tela inicial
            def back():
                frameVeiculo.pack_forget()
                frameLabelVeiculo.pack_forget()
                frame.pack(side=RIGHT)

            voltar = customtkinter.CTkButton(master=frameVeiculo, 
                                         text="Voltar", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="gray",
                                         hover_color="#090909",
                                         command=back
                                         ).place(x=25, y=520)

        # Tela para Pesquisar Funcionário
        def telaPesquisarFuncionario():
            frame.pack_forget()

            # Frame com os dados do funcionario
            framePesquisarFuncionario = customtkinter.CTkFrame(janela, width=350, height=600)
            framePesquisarFuncionario.pack(side=RIGHT)

            # Frame com os títulos
            frameLabelPesquisarFuncionario = customtkinter.CTkFrame(janela, width=350, height=600)
            frameLabelPesquisarFuncionario.pack(side=LEFT)

            label = customtkinter.CTkLabel(framePesquisarFuncionario,
                                           text="Pesquisar Funcionário",
                                           ).place(x=25, y=5)

            # Titulo
            labelNomeFunc = customtkinter.CTkLabel(frameLabelPesquisarFuncionario,
                                           text="Nome: ",
                                           ).place(x=280, y=40)

            # Entrada de dados
            nomeFuncPesquisar = customtkinter.CTkEntry(framePesquisarFuncionario,
                                                      width=300,
                                                      textvariable = nomeFuncPesquisarSave,
                                                      ).place(x=25, y=40)

            scrollableFuncionarioFrame = customtkinter.CTkScrollableFrame(framePesquisarFuncionario, width=280, height=350)
            scrollableFuncionarioFrame.place(x=25, y=90)

            # TODO: passar esse método para a classe do banco de dados
            def pesquisarFuncionario():

                # Exclui os dados da pesquisa anterior
                for widget in scrollableFuncionarioFrame.winfo_children():
                    widget.destroy() 

                searchTerm = nomeFuncPesquisarSave.get().strip() 

                # Verifica se a pesquisa está vazia
                if searchTerm:
                    # Conexão temporária com o banco de dados
                    conn = sqlite3.connect("bdGaragemJython.db")
                    cursor = conn.cursor()

                    # Atributos da pesquisa
                    query = f"SELECT nome, cpfFuncionario FROM funcionario WHERE nome LIKE '%{nomeFuncPesquisarSave.get()}%'"
                    cursor.execute(query)

                    # Array de resultados
                    results = cursor.fetchall()
                    conn.close()

                    # Verifica se existe algum resultado
                    if  len(results) < 1:
                            customtkinter.CTkLabel(scrollableFuncionarioFrame, text="Não foi possível encontar.").pack(side="top")

                    # Tratamento e disposição na tela
                    colors = ["#303030", "#343638"] 
                    for i, result in enumerate(results):
                        colorIndex = i % len(colors)
                        color = colors[colorIndex]

                        customtkinter.CTkLabel(scrollableFuncionarioFrame, 
                                            text="Nome: " + result[0] + "\nCpf: " + result[1],
                                            font=("Helvetica", 14),
                                            height=50,
                                            width=300,
                                            anchor=W,
                                            padx=20,
                                            bg_color=color).pack(side="top")

            # Botão save
            savePesFuncionario = customtkinter.CTkButton(master=framePesquisarFuncionario, 
                                         text="Pesquisar Funcionário", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="green",
                                         hover_color="#014B05",
                                         command=pesquisarFuncionario
                                         ).place(x=25, y=480)

            # Volta para tela inicial
            def back():
                framePesquisarFuncionario.pack_forget()
                frameLabelPesquisarFuncionario.pack_forget()
                frame.pack(side=RIGHT)

            voltar = customtkinter.CTkButton(master=framePesquisarFuncionario, 
                                         text="Voltar", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="gray",
                                         hover_color="#090909",
                                         command=back
                                         ).place(x=25, y=520)

        # Tela pesquisar cliente
        def telaPesquisarCliente():
            frame.pack_forget()

            # Frame com os dados do cliente
            framePesquisarCliente = customtkinter.CTkFrame(janela, width=350, height=600)
            framePesquisarCliente.pack(side=RIGHT)

            # Frame com os títulos
            frameLabelPesquisarCliente = customtkinter.CTkFrame(janela, width=350, height=600)
            frameLabelPesquisarCliente.pack(side=LEFT)

            label = customtkinter.CTkLabel(master=framePesquisarCliente,
                                           text="Pesquisar Cliente",
                                           ).place(x=25, y=5)

            # Título
            labelNomeClientePesquisar = customtkinter.CTkLabel(master=frameLabelPesquisarCliente,
                                           text="Nome: ",
                                           ).place(x=280, y=40)

            # Entrada de dados
            nomeClientePesquisar = customtkinter.CTkEntry(master=framePesquisarCliente,
                                                      width=300,
                                                      textvariable=nomePesquisarClienteSave,
                                                      ).place(x=25, y=40)

            scrollableClienteFrame = customtkinter.CTkScrollableFrame(framePesquisarCliente, width=280, height=350)
            scrollableClienteFrame.place(x=25, y=90)

            def pesquisarCliente():

                # Exclui os dados da pesquisa anterior
                for widget in scrollableClienteFrame.winfo_children():
                    widget.destroy() 

                searchTerm = nomePesquisarClienteSave.get().strip() 

                # Verifica se a pesquisa está vazia
                if searchTerm:

                    # Conexão temporária com o banco de dados
                    conn = sqlite3.connect("bdGaragemJython.db")
                    cursor = conn.cursor()

                    # Atributos da pesquisa
                    query = f"SELECT nome, cpfPessoaFisica, email FROM PessoaFisica WHERE nome LIKE '%{nomePesquisarClienteSave.get()}%'"
                    cursor.execute(query)

                    # Array de resultados
                    results = cursor.fetchall()
                    conn.close()

                    # Verifica se esxiste resultado
                    if  len(results) < 1:
                            customtkinter.CTkLabel(scrollableClienteFrame, text="Não foi possível encontar.").pack(side="top")

                    # Tratamento e disposição na tela
                    colors = ["#303030", "#343638"] 
                    for i, result in enumerate(results):
                        color_index = i % len(colors)
                        color = colors[color_index]

                        customtkinter.CTkLabel(scrollableClienteFrame, 
                                            text="Nome: " + result[0] + "\nCpf: " + result[1]+ "\n Email: " + result[2],
                                            font=("Helvetica", 14),
                                            height=80,
                                            width=300,
                                            anchor=W,
                                            padx=20,
                                            bg_color=color).pack(side="top")

            # Botão save
            savePesFuncionario = customtkinter.CTkButton(master=framePesquisarCliente, 
                                         text="Pesquisar Cliente", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="green",
                                         hover_color="#014B05",
                                         command=pesquisarCliente
                                         ).place(x=25, y=480)

            # Volta para tela inicial
            def back():
                framePesquisarCliente.pack_forget()
                frameLabelPesquisarCliente.pack_forget()
                frame.pack(side=RIGHT)

            voltar = customtkinter.CTkButton(master=framePesquisarCliente, 
                                         text="Voltar", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="gray",
                                         hover_color="#090909",
                                         command=back
                                         ).place(x=25, y=520)

        # Tela pesquisar veículo
        def telaPesquisarVeiculo():
            frame.pack_forget()

            # Frame com os dados do veiculo
            framePesquisarVeiculo = customtkinter.CTkFrame(janela, width=350, height=600)
            framePesquisarVeiculo.pack(side=RIGHT)

            # Frame com os títulos
            frameLabelPesquisarVeiculo = customtkinter.CTkFrame(janela, width=350, height=600)
            frameLabelPesquisarVeiculo.pack(side=LEFT)

            label = customtkinter.CTkLabel(master=framePesquisarVeiculo,
                                           text="Pesquisar Veículo",
                                           ).place(x=25, y=5)

            # Título
            labelModeloVeiculo = customtkinter.CTkLabel(master=frameLabelPesquisarVeiculo,
                                           text="Nome: ",
                                           ).place(x=280, y=40)

            # Entrada de dados
            modeloPesquisar = customtkinter.CTkEntry(master=framePesquisarVeiculo,
                                                      width=300,
                                                      textvariable=modeloVeiculoPesquisarSave,
                                                      ).place(x=25, y=40)

            ########################################
            ###       Insira o código aqui       ###
            ########################################

            # Botão save
            savePesFuncionario = customtkinter.CTkButton(master=framePesquisarVeiculo,
                                         text="Pesquisar Veículo",
                                         width=300, height=30,
                                         font=("Roboto", 16),
                                         fg_color="green",
                                         hover_color="#014B05",
                                         command=printnome
                                         ).place(x=25, y=480)

            # Volta para tela inicial
            def back():
                framePesquisarVeiculo.pack_forget()
                frameLabelPesquisarVeiculo.pack_forget()
                frame.pack(side=RIGHT)

            voltar = customtkinter.CTkButton(master=framePesquisarVeiculo, 
                                         text="Voltar", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="gray",
                                         hover_color="#090909",
                                         command=back
                                         ).place(x=25, y=520)

        # Tela pesquisar veículo
        def telaHistoricoVendas():
            frame.pack_forget()

            # Frame com os dados do histórico
            frameHistoricoVendas = customtkinter.CTkFrame(janela, width=700, height=600)
            frameHistoricoVendas.pack(side=RIGHT)

            label = customtkinter.CTkLabel(master=frameHistoricoVendas,
                                           text="Histórico de vendas",
                                           ).place(x=25, y=5)

            ########################################
            ###       Insira o código aqui       ###
            ########################################

            # Botão save
            exibirHistorico = customtkinter.CTkButton(master=frameHistoricoVendas, 
                                         text="Exibir Histórico", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="green",
                                         hover_color="#014B05",
                                         command=printnome
                                         ).place(x=25, y=480)

            # Volta para tela inicial
            def back():
                frameHistoricoVendas.pack_forget()
                frame.pack(side=RIGHT)

            voltar = customtkinter.CTkButton(master=frameHistoricoVendas, 
                                         text="Voltar", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="gray",
                                         hover_color="#090909",
                                         command=back
                                         ).place(x=25, y=520)

        # Tela realizar venda
        def telaRealizarVenda():
            frame.pack_forget()

            # Frame com os dados da venda
            frameRealizarVenda = customtkinter.CTkFrame(janela, width=350, height=600)
            frameRealizarVenda.pack(side=RIGHT)

            # Frame com os títulos
            frameLabelRealizarVenda = customtkinter.CTkFrame(janela, width=350, height=600)
            frameLabelRealizarVenda.pack(side=LEFT)

            label = customtkinter.CTkLabel(master=frameRealizarVenda,
                                           text="Realizar Venda",
                                           ).place(x=25, y=5)

            # Titulo######################
            # Similar ao cadastrar veículo

            # Entrada de dados############
            # Similar ao cadastrar veículo

            # Botão save
            saveFuncionario = customtkinter.CTkButton(master=frameRealizarVenda, 
                                         text="Realizar Venda", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="green",
                                         hover_color="#014B05",
                                         command=printnome
                                         ).place(x=25, y=480)

            # Volta para tela inicial
            def back():
                frameRealizarVenda.pack_forget()
                frameLabelRealizarVenda.pack_forget()
                frame.pack(side=RIGHT)

            voltar = customtkinter.CTkButton(master=frameRealizarVenda, 
                                         text="Voltar", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         fg_color="gray",
                                         hover_color="#090909",
                                         command=back
                                         ).place(x=25, y=520)

        # Opções do menu
        botao1 = customtkinter.CTkButton(master=frame, 
                                         text="Cadastrar Funcionário", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         command=telaCadastrarFuncionario
                                         ).place(x=25, y=60)

        botao2 = customtkinter.CTkButton(master=frame, 
                                         text="Pesquisar Funcionário", 
                                         width=300, 
                                         height=30,  
                                         font=("Roboto", 16),
                                         command=telaPesquisarFuncionario
                                         ).place(x=25, y=100)

        botao3 = customtkinter.CTkButton(master=frame, 
                                         text="Cadastrar Cliente", 
                                         width=300, height=30,  
                                         font=("Roboto", 16),
                                         command=telaCadastrarCliente
                                         ).place(x=25, y=140)

        botao4 = customtkinter.CTkButton(master=frame, 
                                        text="Pesquisar Cliente", 
                                        width=300, 
                                        height=30,  
                                        font=("Roboto", 16),
                                        command=telaPesquisarCliente
                                        ).place(x=25, y=180)

        botao5 = customtkinter.CTkButton(master=frame, 
                                        text="Cadastrar Veículo", 
                                        width=300, 
                                        height=30,  
                                        font=("Roboto", 16),
                                        command=telaCadastrarVeiculo
                                        ).place(x=25, y=220)

        botao6 = customtkinter.CTkButton(master=frame, 
                                        text="Pesquisar Veículo", 
                                        width=300, 
                                        height=30,  
                                        font=("Roboto", 16),
                                        command=telaPesquisarVeiculo
                                        ).place(x=25, y=260)

        botao7 = customtkinter.CTkButton(master=frame, 
                                        text="Histórico de Vendas", 
                                        width=300, 
                                        height=30,  
                                        font=("Roboto", 16),
                                        command=telaHistoricoVendas
                                        ).place(x=25, y=300)

        botao8 = customtkinter.CTkButton(master=frame, 
                                        text="Realizar Venda", 
                                        width=300, 
                                        height=30,  
                                        font=("Roboto", 16),
                                        command=telaRealizarVenda
                                        ).place(x=25, y=340)

Aplicacao()
