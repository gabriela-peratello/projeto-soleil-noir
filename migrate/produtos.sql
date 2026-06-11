CREATE TABLE IF NOT EXISTS produtos (
codigo INT NOT NULL PRIMARY KEY auto_increment,
produto VARCHAR(200),
descr VARCHAR(400),
preco FLOAT,
foto VARCHAR (500),
id_categoria INT,
FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);