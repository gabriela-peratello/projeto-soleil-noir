CREATE TABLE IF NOT EXISTS usuarios (
codigo_usuario INT NOT NULL PRIMARY KEY auto_increment,
nome_completo VARCHAR(200),
email VARCHAR(300) unique,
telefone CHAR(9),
endereço VARCHAR(100),
senha VARCHAR(200)
);