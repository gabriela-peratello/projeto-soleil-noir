CREATE DATABASE IF NOT EXISTS soleilnoir;
USE soleilnoir;

CREATE TABLE IF NOT EXISTS comentarios(
id_comentario INT NOT NULL PRIMARY KEY auto_increment,
codigo_usuario INT,
comentario VARCHAR(600),
FOREIGN KEY (codigo_usuario) REFERENCES usuarios(codigo_usuario)
);