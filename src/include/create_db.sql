-- TODO: primary key e foreign key.

create table garagem (
	cnpj varchar(16),
	nome varchar(64)
);

create table funcionario (
	cpf varchar(64),
	rg varchar(64),
	nome varchar(64),
	cargo varchar(64),
	salario float,
	endereco varchar(64),
	numero int,
	bairro varchar(64),
	cep varchar(64),
	telefone varchar(16),
	email varchar(64),
	dataNasc date,
	sexo char,
	cnpj varchar(14),
);

create table vendasFuncionario (
	id int, -- na imagem não possui essa variável
	cpfFuncionario varchar(16),
	cnpj varchar(16),
	placaVeiculo varchar(8)
);

create table pessoaFisica (
	cpf varchar(16),
	rg varchar(32),
	nome varchar(64),
	endereco varchar(64),
	numero int,
	bairro varchar(64),
	cep varchar(8),
	telefone varchar(64),
	email varchar(64),
	dataNasc date,
	sexo char
);

create table pessoaJuridica (
	cnpj varchar(16),
	nome varchar(64),
	endereco varchar(64),
	numero int,
	bairro varchar(64),
	cep varchar(8),
	telefone varchar(16),
	email varchar(64)
);

create table Veiculo (
	placa varchar(8),
	marca varchar(16),
	ano date,
	cor varchar(16),
	preco float,
	kmRodados int
	-- foreign key para cnpj da agencia
);

create table notaFiscal (
	-- apenas um esboço
	cpf varchar(16),
	cnpj varchar(16),
	placaVeiculo varchar(8),
	valor float
);
