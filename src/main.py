from tkinter import *
import tkinter.messagebox
from sys import path
from PIL import Image
import customtkinter
from bancoDeDados import BancoDeDados

from funcionario import Funcionario
from cliente import Cliente
from veiculos import Veiculo
from venda import Venda


class Aplicacao:
    def __init__(self):
        self.banco = BancoDeDados("test.db")
        self.janela = customtkinter.CTk()
        self.frame = customtkinter.CTkFrame(self.janela)

        self.setTema()
        self.configurarTela()
        self.criarTelaOpcoes()

        self.janela.mainloop()

    def setTema(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    def configurarTela(self):
        self.janela.title("Gerenciador de Garagem")
        largura = 700
        altura = 600
        larguraTela = self.janela.winfo_screenwidth()
        alturaTela = self.janela.winfo_screenheight()
        posx = (larguraTela / 2) - (largura / 2)
        posy = (alturaTela / 2) - (altura / 2)

        self.janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.janela.resizable(False, False)

    def criarTelaOpcoes(self):
        self.frame.pack_forget()

        caminhoDaImagem = path[0] + "/img/logoPrincipal.png"
        imgData = Image.open(caminhoDaImagem)
        img = customtkinter.CTkImage(
            dark_image=imgData, light_image=imgData, size=(350, 350)
        )

        self.frame = customtkinter.CTkFrame(self.janela)
        self.frame.pack(fill=BOTH, expand=True)

        labelImg = customtkinter.CTkLabel(self.frame, image=img, text="")
        labelImg.pack(side=LEFT)

        self.frameBotoes = customtkinter.CTkFrame(self.frame, width=350, height=396)
        self.frameBotoes.pack(side=RIGHT)

        self.criarBotoes(self.frameBotoes)

    def criarBotoes(self, frame):
        dadosBotao = [
            ("Cadastrar Funcionário", self.telaCadastrarFuncionario),
            ("Pesquisar Funcionário", self.telaPesquisarFuncionario),
            ("Cadastrar Cliente", self.telaCadastrarCliente),
            ("Pesquisar Cliente", self.telaPesquisarCliente),
            ("Cadastrar Veículo", self.telaCadastrarVeiculo),
            ("Pesquisar Veículo", self.telaPesquisarVeiculo),
            ("Histórico de Vendas", self.telaHistoricoVendas),
            ("Realizar Venda", self.telaRealizarVenda),
        ]

        y = 60
        for text, command in dadosBotao:
            customtkinter.CTkButton(
                frame,
                text=text,
                width=300,
                height=30,
                font=("Roboto", 16),
                command=command,
            ).place(x=25, y=y)
            y += 40

    def cadastrar(self, tabela, entryObject):
        atributos = vars(entryObject)
        valores = []

        for valor in atributos.values():
            valores.append(valor.get())

        # Inserção no BD
        self.banco.inserirDados(tabela, valores)

        # Limpar os valores das entradas após o cadastro
        for valor in atributos.values():
            valor.set("")

        tkinter.messagebox.showinfo("Sucesso", "O cadastro foi realizado com sucesso!")

    # TODO
    # 1. Validar os dados antes da inserção no banco
    # 2. Verificar bancoDeDados.py

    def telaCadastrarFuncionario(self):
        self.frame.pack_forget()

        self.frame = customtkinter.CTkFrame(self.janela)
        self.frame.pack(fill=BOTH, expand=True)

        frameFuncionario = customtkinter.CTkFrame(self.frame, width=350, height=600)
        frameFuncionario.pack(side=RIGHT)

        frameLabelFuncionario = customtkinter.CTkFrame(
            self.frame, width=350, height=600
        )
        frameLabelFuncionario.pack(side=LEFT)

        customtkinter.CTkLabel(
            frameFuncionario,
            text="Cadastrar Funcionário",
        ).place(x=25, y=5)

        novoFuncionario = Funcionario()

        y = 40

        campos = [
            ("CPF", novoFuncionario.cpf),
            ("RG", novoFuncionario.rg),
            ("Nome", novoFuncionario.nome),
            ("Endereço", novoFuncionario.endereco),
            ("Número", novoFuncionario.numero),
            ("Bairro", novoFuncionario.bairro),
            ("CEP", novoFuncionario.cep),
            ("Email", novoFuncionario.email),
            ("Telefone", novoFuncionario.telefone),
            ("Cargo", novoFuncionario.cargo),
            ("Salário", novoFuncionario.salario),
        ]

        for label, var in campos:
            customtkinter.CTkLabel(
                frameLabelFuncionario,
                text=f"{label}: ",
            ).place(x=280, y=y)

            customtkinter.CTkEntry(
                frameFuncionario,
                width=300,
                textvariable=var,
            ).place(x=25, y=y)
            y += 40

        customtkinter.CTkButton(
            frameFuncionario,
            text="Cadastrar Funcionário",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="green",
            hover_color="#014B05",
            command=lambda: self.cadastrar("funcionario", novoFuncionario),
        ).place(x=25, y=480)

        customtkinter.CTkButton(
            frameFuncionario,
            text="Voltar",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="gray",
            hover_color="#090909",
            command=self.voltar,
        ).place(x=25, y=520)

    def telaPesquisarFuncionario(self):
        self.frame.pack_forget()

        self.frame = customtkinter.CTkFrame(self.janela)
        self.frame.pack(fill=BOTH, expand=True)

        # Frame com os dados do funcionario
        framePesquisarFuncionario = customtkinter.CTkFrame(
            self.frame, width=350, height=600
        )
        framePesquisarFuncionario.pack(side=RIGHT)

        # Frame com os títulos
        frameLabelPesquisarFuncionario = customtkinter.CTkFrame(
            self.frame, width=350, height=600
        )
        frameLabelPesquisarFuncionario.pack(side=LEFT)

        customtkinter.CTkLabel(
            framePesquisarFuncionario,
            text="Pesquisar Funcionário",
        ).place(x=25, y=5)

        customtkinter.CTkLabel(
            frameLabelPesquisarFuncionario,
            text="Nome: ",
        ).place(x=280, y=40)

        nomeFuncPesquisarSave = customtkinter.StringVar()

        customtkinter.CTkEntry(
            framePesquisarFuncionario,
            width=300,
            textvariable=nomeFuncPesquisarSave,
        ).place(x=25, y=40)

        scrollableFuncionarioFrame = customtkinter.CTkScrollableFrame(
            framePesquisarFuncionario, width=280, height=350
        )
        scrollableFuncionarioFrame.place(x=25, y=90)

        def pesquisarFuncionario():
            # Exclui os dados da pesquisa anterior
            for widget in scrollableFuncionarioFrame.winfo_children():
                widget.destroy()

            searchTerm = nomeFuncPesquisarSave.get().strip()

            # Verifica se a pesquisa está vazia
            if searchTerm:
                results = self.banco.pesquisar("funcionario", searchTerm)

                # Verifica se existe algum resultado
                if len(results) < 1:
                    customtkinter.CTkLabel(
                        scrollableFuncionarioFrame, text="Não foi possível encontar."
                    ).pack(side="top")

                # Tratamento e disposição na tela
                colors = ["#303030", "#343638"]
                for i, result in enumerate(results):
                    colorIndex = i % len(colors)
                    color = colors[colorIndex]

                    labelFrame = customtkinter.CTkFrame(scrollableFuncionarioFrame)
                    labelFrame.pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Cpf: " + result[0],
                        font=("Helvetica", 12),
                        height=40,
                        width=300,
                        anchor=SW,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Rg: " + result[1],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Nome: " + result[2],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Endereço: " + result[3] + ", " + str(result[4]),
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Bairro: " + result[5],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="CEP: " + result[6],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Telefone: " + result[7],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Email: " + result[8],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Cargo: " + result[9],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Salário: R$ " + str(result[10]),
                        font=("Helvetica", 12),
                        height=40,
                        width=300,
                        anchor=NW,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

        customtkinter.CTkButton(
            framePesquisarFuncionario,
            text="Pesquisar Funcionário",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="green",
            hover_color="#014B05",
            command=pesquisarFuncionario,
        ).place(x=25, y=480)

        customtkinter.CTkButton(
            framePesquisarFuncionario,
            text="Voltar",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="gray",
            hover_color="#090909",
            command=self.voltar,
        ).place(x=25, y=520)

    def telaCadastrarCliente(self):
        self.frame.pack_forget()

        self.frame = customtkinter.CTkFrame(self.janela)
        self.frame.pack(fill=BOTH, expand=True)

        frameCliente = customtkinter.CTkFrame(self.frame, width=350, height=600)
        frameCliente.pack(side=RIGHT)

        frameLabelCliente = customtkinter.CTkFrame(self.frame, width=350, height=600)
        frameLabelCliente.pack(side=LEFT)

        customtkinter.CTkLabel(
            frameCliente,
            text="Cadastrar Cliente",
        ).place(x=25, y=5)

        novoCliente = Cliente()

        y = 40
        campos = [
            ("CPF", novoCliente.cpf),
            ("RG", novoCliente.rg),
            ("Nome", novoCliente.nome),
            ("Endereço", novoCliente.endereco),
            ("Número", novoCliente.numero),
            ("Bairro", novoCliente.bairro),
            ("CEP", novoCliente.cep),
            ("Telefone", novoCliente.telefone),
            ("Email", novoCliente.email),
        ]

        for label, var in campos:
            customtkinter.CTkLabel(
                frameLabelCliente,
                text=f"{label}: ",
            ).place(x=280, y=y)

            customtkinter.CTkEntry(
                frameCliente,
                width=300,
                textvariable=var,
            ).place(x=25, y=y)
            y += 40

        customtkinter.CTkButton(
            frameCliente,
            text="Cadastrar Cliente",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="green",
            hover_color="#014B05",
            command=lambda: self.cadastrar("cliente", novoCliente),
        ).place(x=25, y=480)

        customtkinter.CTkButton(
            frameCliente,
            text="Voltar",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="gray",
            hover_color="#090909",
            command=self.voltar,
        ).place(x=25, y=520)

    def telaPesquisarCliente(self):
        self.frame.pack_forget()

        self.frame = customtkinter.CTkFrame(self.janela)
        self.frame.pack(fill=BOTH, expand=True)

        # Frame com os dados do cliente
        framePesquisarCliente = customtkinter.CTkFrame(
            self.frame, width=350, height=600
        )
        framePesquisarCliente.pack(side=RIGHT)

        # Frame com os títulos
        frameLabelPesquisarCliente = customtkinter.CTkFrame(
            self.frame, width=350, height=600
        )
        frameLabelPesquisarCliente.pack(side=LEFT)

        customtkinter.CTkLabel(
            framePesquisarCliente,
            text="Pesquisar Cliente",
        ).place(x=25, y=5)

        customtkinter.CTkLabel(
            frameLabelPesquisarCliente,
            text="Nome: ",
        ).place(x=280, y=40)

        nomePesquisarClienteSave = customtkinter.StringVar()

        customtkinter.CTkEntry(
            framePesquisarCliente,
            width=300,
            textvariable=nomePesquisarClienteSave,
        ).place(x=25, y=40)

        scrollableClienteFrame = customtkinter.CTkScrollableFrame(
            framePesquisarCliente, width=280, height=350
        )
        scrollableClienteFrame.place(x=25, y=90)

        def pesquisarCliente():
            # Exclui os dados da pesquisa anterior
            for widget in scrollableClienteFrame.winfo_children():
                widget.destroy()

            searchTerm = nomePesquisarClienteSave.get().strip()

            # Verifica se a pesquisa está vazia
            if searchTerm:
                nome = nomePesquisarClienteSave.get()
                results = self.banco.pesquisar("cliente", nome)

                # Verifica se esxiste resultado
                if len(results) < 1:
                    customtkinter.CTkLabel(
                        scrollableClienteFrame, text="Não foi possível encontar."
                    ).pack(side="top")

                # Tratamento e disposição na tela
                colors = ["#303030", "#343638"]
                for i, result in enumerate(results):
                    color_index = i % len(colors)
                    color = colors[color_index]

                    labelFrame = customtkinter.CTkFrame(scrollableClienteFrame)
                    labelFrame.pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="CPF: " + result[0],
                        font=("Helvetica", 12),
                        height=40,
                        width=300,
                        anchor=SW,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="RG: " + result[1],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=SW,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Nome: " + result[2],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Endereço: " + result[3] + ", " + str(result[4]),
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Bairro: " + result[5],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="CEP: " + result[6],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Telefone: " + result[7],
                        font=("Helvetica", 12),
                        height=20,
                        width=300,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Email: " + result[8],
                        font=("Helvetica", 12),
                        height=40,
                        width=300,
                        anchor=NW,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

        customtkinter.CTkButton(
            framePesquisarCliente,
            text="Pesquisar Cliente",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="green",
            hover_color="#014B05",
            command=pesquisarCliente,
        ).place(x=25, y=480)

        customtkinter.CTkButton(
            framePesquisarCliente,
            text="Voltar",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="gray",
            hover_color="#090909",
            command=self.voltar,
        ).place(x=25, y=520)

    def telaCadastrarVeiculo(self):
        self.frame.pack_forget()

        self.frame = customtkinter.CTkFrame(self.janela)
        self.frame.pack(fill=BOTH, expand=True)

        frameVeiculo = customtkinter.CTkFrame(self.frame, width=350, height=600)
        frameVeiculo.pack(side=RIGHT)

        frameLabelVeiculo = customtkinter.CTkFrame(self.frame, width=350, height=600)
        frameLabelVeiculo.pack(side=LEFT)

        customtkinter.CTkLabel(
            frameVeiculo, text="Cadastrar Veículo", font=("Roboto", 16)
        ).place(x=25, y=5)

        novoVeiculo = Veiculo()

        campos = [
            ("Modelo", novoVeiculo.modelo),
            ("Marca", novoVeiculo.marca),
            ("Ano", novoVeiculo.ano),
            ("Cor", novoVeiculo.cor),
            ("Preço", novoVeiculo.preco),
            ("Placa", novoVeiculo.placa),
            ("Km Rodado", novoVeiculo.kmRodados),
        ]

        y = 40
        for label, var in campos:
            customtkinter.CTkLabel(
                frameLabelVeiculo,
                text=f"{label}: ",
            ).place(x=280, y=y)

            customtkinter.CTkEntry(
                frameVeiculo,
                width=300,
                textvariable=var,
            ).place(x=25, y=y)
            y += 40

        customtkinter.CTkButton(
            frameVeiculo,
            text="Cadastrar Veículo",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="green",
            hover_color="#014B05",
            command=lambda: self.cadastrar("veiculo", novoVeiculo),
        ).place(x=25, y=480)

        customtkinter.CTkButton(
            frameVeiculo,
            text="Voltar",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="gray",
            hover_color="#090909",
            command=self.voltar,
        ).place(x=25, y=520)

    def telaPesquisarVeiculo(self):
        self.frame.pack_forget()

        self.frame = customtkinter.CTkFrame(self.janela)
        self.frame.pack(fill=BOTH, expand=True)

        # Frame com os dados do veiculo
        framePesquisarVeiculo = customtkinter.CTkFrame(
            self.frame, width=350, height=600
        )
        framePesquisarVeiculo.pack(side=RIGHT)

        # Frame com os títulos
        frameLabelPesquisarVeiculo = customtkinter.CTkFrame(
            self.frame, width=350, height=600
        )
        frameLabelPesquisarVeiculo.pack(side=LEFT)

        customtkinter.CTkLabel(
            framePesquisarVeiculo,
            text="Pesquisar Veículo",
        ).place(x=25, y=5)

        customtkinter.CTkLabel(
            frameLabelPesquisarVeiculo,
            text="Modelo: ",
        ).place(x=280, y=40)

        modeloVeiculoPesquisarSave = customtkinter.StringVar()

        customtkinter.CTkEntry(
            framePesquisarVeiculo,
            width=300,
            textvariable=modeloVeiculoPesquisarSave,
        ).place(x=25, y=40)

        scrollableCarFrame = customtkinter.CTkScrollableFrame(
            framePesquisarVeiculo, width=280, height=350
        )
        scrollableCarFrame.place(x=25, y=90)

        def pesquisarVeiculo():
            # Exclui os dados da pesquisa anterior
            for widget in scrollableCarFrame.winfo_children():
                widget.destroy()

            searchTerm = modeloVeiculoPesquisarSave.get().strip()

            # Verifica se a pesquisa está vazia
            if searchTerm:
                results = self.banco.pesquisar("veiculo", searchTerm, "modelo")

                # Verifica se esxiste resultado
                if len(results) < 1:
                    customtkinter.CTkLabel(
                        scrollableCarFrame, text="Não foi possível encontar."
                    ).pack(side="top")

                # Tratamento e disposição na tela
                colors = ["#303030", "#343638"]
                for i, result in enumerate(results):
                    colorIndex = i % len(colors)
                    color = colors[colorIndex]

                    labelFrame = customtkinter.CTkFrame(scrollableCarFrame)
                    labelFrame.pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Modelo: "
                        + result[0]
                        + "  "
                        + result[3]
                        + "  "
                        + (str(result[2]).split("-"))[0],
                        font=("Helvetica", 12),
                        height=40,
                        width=625,
                        anchor=SW,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Marca: " + result[1] + " - Placa: " + result[5],
                        font=("Helvetica", 12),
                        height=20,
                        width=625,
                        anchor=W,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

                    customtkinter.CTkLabel(
                        labelFrame,
                        text="Kilometragem: "
                        + str(result[6])
                        + " - Preço: R$ "
                        + str(result[4]),
                        font=("Helvetica", 12),
                        height=40,
                        width=625,
                        anchor=NW,
                        padx=20,
                        bg_color=color,
                    ).pack(side="top")

        customtkinter.CTkButton(
            framePesquisarVeiculo,
            text="Pesquisar Veículo",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="green",
            hover_color="#014B05",
            command=pesquisarVeiculo,
        ).place(x=25, y=480)

        customtkinter.CTkButton(
            framePesquisarVeiculo,
            text="Voltar",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="gray",
            hover_color="#090909",
            command=self.voltar,
        ).place(x=25, y=520)

    def telaHistoricoVendas(self):
        self.frame.pack_forget()

        self.frame = customtkinter.CTkFrame(self.janela)
        self.frame.pack(fill=BOTH, expand=True)

        # Frame com os dados do histórico
        frameHistoricoVendas = customtkinter.CTkFrame(self.frame, width=700, height=600)
        frameHistoricoVendas.pack(side=RIGHT)

        customtkinter.CTkLabel(
            master=frameHistoricoVendas,
            text="Histórico de vendas",
        ).place(x=25, y=5)

        scrollableHistoricoFrame = customtkinter.CTkScrollableFrame(
            frameHistoricoVendas, width=625, height=400
        )
        scrollableHistoricoFrame.place(x=25, y=40)

        def pesquisarHistorico():
            # Exclui os dados da pesquisa anterior
            for widget in scrollableHistoricoFrame.winfo_children():
                widget.destroy()

            results = self.banco.pesquisar("venda")

            # Verifica se esxiste resultado
            if len(results) < 1:
                customtkinter.CTkLabel(
                    scrollableHistoricoFrame,
                    text="Ainda não existem vendas registradas.",
                ).pack(side="top")

            # Tratamento e disposição na tela
            colors = ["#303030", "#343638"]
            for i, result in enumerate(results):
                colorIndex = i % len(colors)
                color = colors[colorIndex]

                labelFrame = customtkinter.CTkFrame(scrollableHistoricoFrame)
                labelFrame.pack(side="top")

                customtkinter.CTkLabel(
                    labelFrame,
                    text="CPF Cliente: " + result[0],
                    font=("Helvetica", 12),
                    height=40,
                    width=625,
                    anchor=SW,
                    padx=20,
                    bg_color=color,
                ).pack(side="top")

                customtkinter.CTkLabel(
                    labelFrame,
                    text="CPF Funcionario: " + result[1],
                    font=("Helvetica", 12),
                    height=20,
                    width=625,
                    anchor=W,
                    padx=20,
                    bg_color=color,
                ).pack(side="top")

                customtkinter.CTkLabel(
                    labelFrame,
                    text="Data da venda: " + result[2],
                    font=("Helvetica", 12),
                    height=20,
                    width=625,
                    anchor=W,
                    padx=20,
                    bg_color=color,
                ).pack(side="top")

                customtkinter.CTkLabel(
                    labelFrame,
                    text="Placa do carro comprado: " + result[3],
                    font=("Helvetica", 12),
                    height=20,
                    width=625,
                    anchor=W,
                    padx=20,
                    bg_color=color,
                ).pack(side="top")

                customtkinter.CTkLabel(
                    labelFrame,
                    text="Id: " + str(result[4]),
                    font=("Helvetica", 12),
                    height=40,
                    width=625,
                    anchor=NW,
                    padx=20,
                    bg_color=color,
                ).pack(side="top")

        customtkinter.CTkButton(
            master=frameHistoricoVendas,
            text="Exibir Histórico",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="green",
            hover_color="#014B05",
            command=pesquisarHistorico,
        ).place(x=25, y=480)

        customtkinter.CTkButton(
            master=frameHistoricoVendas,
            text="Voltar",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="gray",
            hover_color="#090909",
            command=self.voltar,
        ).place(x=25, y=520)

    def telaRealizarVenda(self):
        self.frame.pack_forget()

        self.frame = customtkinter.CTkFrame(self.janela)
        self.frame.pack(fill=BOTH, expand=True)

        frameVenda = customtkinter.CTkFrame(self.frame, width=350, height=600)
        frameVenda.pack(side=RIGHT)

        frameLabelVenda = customtkinter.CTkFrame(self.frame, width=350, height=600)
        frameLabelVenda.pack(side=LEFT)

        customtkinter.CTkLabel(
            frameVenda,
            text="Realizar Venda",
        ).place(x=25, y=5)

        novaVenda = Venda()

        y = 40
        campos = [
            ("CPF Cliente", novaVenda.cpfCliente),
            ("CPF Funcionário", novaVenda.cpfFuncionario),
            ("Placa Veículo", novaVenda.placaVeiculo),
        ]

        for label, var in campos:
            customtkinter.CTkLabel(
                frameLabelVenda,
                text=f"{label}: ",
            ).place(x=240, y=y)

            customtkinter.CTkEntry(
                frameVenda,
                width=300,
                textvariable=var,
            ).place(x=25, y=y)
            y += 40

        customtkinter.CTkButton(
            master=frameVenda,
            text="Realizar Venda",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="green",
            hover_color="#014B05",
            command=lambda: (
                novaVenda.dataVenda.set(self.getTimestamp()),
                self.cadastrar("venda", novaVenda),
            ),
        ).place(x=25, y=480)

        customtkinter.CTkButton(
            master=frameVenda,
            text="Voltar",
            width=300,
            height=30,
            font=("Roboto", 16),
            fg_color="gray",
            hover_color="#090909",
            command=self.voltar,
        ).place(x=25, y=520)

    def voltar(self):
        self.frame.pack_forget()
        self.criarTelaOpcoes()

    def getTimestamp(self):
        from datetime import datetime

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


app = Aplicacao()
