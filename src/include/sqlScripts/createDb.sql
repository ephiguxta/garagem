create table if not exists funcionario (
	cpf varchar(18) not null,
	rg varchar(16) not null,
	nome varchar(45) not null,
	endereco varchar(45) not null,
	numero int not null,
	bairro varchar(45) not null,
	cep varchar(20) not null,
	telefone varchar(15) not null,
	email varchar(45) not null,
	cargo varchar(45) not null,
	salario float not null,

	primary key (cpf)
);

create table if not exists veiculo (
	modelo varchar(45) not null,
	marca varchar(45) not null,
	ano date not null,
	cor varchar(45) not null,
	preco float not null,
	placa varchar(9) not null,
	kmRodados int not null,

	primary key (placa)
);

create table if not exists cliente (
	cpf varchar(18) not null,
	rg varchar(16) not null,
	nome varchar(45) not null,
	endereco varchar(45) not null,
	numero int not null,
	bairro varchar(45) not null,
	cep varchar(20) not null,
	telefone varchar(15) not null,
	email varchar(45) not null,

	primary key (cpf)
);

create table if not exists venda (
    cpf_cliente varchar(14) not null,
    cpf_funcionario varchar(14) not null,
	data_venda date not null,
    placa_veiculo varchar(9) not null,
    id integer not null primary key autoincrement,

    foreign key (cpf_funcionario) references funcionario (cpf),
    foreign key (cpf_cliente) references cliente (cpf),
    foreign key (placa_veiculo) references veiculo (placa)
);
