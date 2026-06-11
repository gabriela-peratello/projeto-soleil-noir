CREATE TABLE IF NOT EXISTS usuarios (
codigo_usuario INT NOT NULL PRIMARY KEY auto_increment,
nome_completo VARCHAR(200),
email VARCHAR(300) unique,
telefone VARCHAR(20),
endereco VARCHAR(100),
senha VARCHAR(200)
);