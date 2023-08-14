create table if not exists garagem (
	cnpj varchar(18) not null,
	nome varchar(45) not null,
	endereco varchar(45) not null,
	bairro varchar(45) not null,
	numero int not null,
	cep varchar(20) not null,
	email varchar(45) not null,

	primary key (cnpj)
);

create table if not exists funcionario (
	cpf varchar(14) not null,
	rg varchar(16) not null,
	nome varchar(45) not null,
	cargo varchar(45) not null,
	salario float not null,
	endereco varchar(45) not null,
	bairro varchar(45) not null,
	numero int not null,
	cep varchar(45) not null,
	email varchar(45) not null,
	primary key (cpf)
);

create table if not exists veiculo (
	placa varchar(9) not null,
	marca varchar(45) not null,
	modelo varchar(45) not null,
	ano date not null,
	cor varchar(45) not null,
	kmRodados int not null,
	preco float not null,

	primary key (placa)
);

create table if not exists cliente (
	cpf varchar(18) not null,
	-- no script antigo aqui teria o seguinte campo:
	-- rg varchar(16) not null,
	nome varchar(45) not null,
	endereco varchar(45) not null,
	numero int not null,
	bairro varchar(45) not null,
	cep varchar(20) not null,
	telefone varchar(15) not null,
	email varchar(45) not null,

	primary key (cpf)
);


-- TODO: definir qual tabela seria inserido os dados
-- se for uma pessoa física ou jurídica

/*
create trable if not exists pessoaFisica (
	rg varchar(14) not null,
	dataNasc date not null,
	sexo varchar(1) not null,
	primary key
);
*/

create table if not exists compra (
	id integer not null,
	cnpjGaragem varchar(18) not null,

	cpfPessoa varchar not null,
	--cpfFuncionario varchar(14) not null,
	-- cpfPessoaFisica varchar(14),
	-- cnpjPessoaJuridica varchar(18),

	placaVeiculo varchar(9) not null,
	
	primary key (id),
	foreign key (cnpjGaragem) references garagem (cnpj),
	foreign key (cpfPessoa) references funcionario (cpf),

	foreign key (cpfPessoa) references cpf (pessoa),
	-- foreign key cpfPessoaFisica references pessoaFisica cpfPessoaFisica,
	-- foreign key cnpjPessoaJuridica references pessoaJuridica cnpjPessoaJuridica,

	foreign key (placaVeiculo) references placa (veiculo)
);
