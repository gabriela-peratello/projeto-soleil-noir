CREATE DATABASE IF NOT EXISTS soleilnoir;
USE soleilnoir;

CREATE TABLE IF NOT EXISTS categorias(
id_categoria INT PRIMARY KEY auto_increment,
nome_categoria VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
codigo INT NOT NULL PRIMARY KEY auto_increment,
produto VARCHAR(200),
descr VARCHAR(400),
preco FLOAT,
foto VARCHAR (500),
id_categoria INT,
FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

CREATE TABLE IF NOT EXISTS usuarios (
codigo_usuario INT NOT NULL PRIMARY KEY auto_increment,
nome_completo VARCHAR(200),
email VARCHAR(300) unique,
telefone VARCHAR(20),
endereco VARCHAR(100),
senha VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS comentarios(
id_comentario INT NOT NULL PRIMARY KEY auto_increment,
codigo_usuario INT,
comentario VARCHAR(600),
FOREIGN KEY (codigo_usuario) REFERENCES usuarios(codigo_usuario)
);