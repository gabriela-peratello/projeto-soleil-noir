-- PRODUTOS

INSERT INTO usuarios (nome_completo, email, telefone, endereco, senha) VALUES ("Erica Santos", "erica123@gmail.com", "557836478","Avenida do sol 123", 3345);
INSERT INTO comentarios(codigo_usuario, comentario) VALUES (1,"Produto incrível! a qualidade é ótima e muito bem feito!");
SELECT usuarios.nome_completo, comentarios.comentario from comentarios
INNER JOIN usuarios on usuarios.nome_completo = usuarios.nome_completo;

-- INSERT DE CATEGORIAS

INSERT INTO categorias(nome_categoria) VALUES ('Anel');
INSERT INTO categorias(nome_categoria) VALUES ('Pulseira');
INSERT INTO categorias(nome_categoria) VALUES ('Brinco');
INSERT INTO categorias(nome_categoria) VALUES ('Colar');

-- INSERT DE PRODUTOS

INSERT INTO produtos(produto, descr, preco, foto, id_categoria) 
VALUES ('Anel Tuileries','Um anel delicado com detalhes florais ou pequenas folhas esculpidas, inspirado nos jardins mais charmosos de Paris.',250.0,'https://images.pexels.com/photos/23440790/pexels-photo-23440790.jpeg',1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria) 
VALUES ('Anel Versailles','Uma peça suntuosa e detalhada, com uma pedra central imponente, inspirada no luxo e na arquitetura do famoso palácio.',250.0,'https://images.pexels.com/photos/23440790/pexels-photo-23440790.jpeg',1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria) 
VALUES ('Anel Bastille','Um aro robusto e texturizado, simbolizando força, atitude e a busca por liberdade.',250.0,'https://images.pexels.com/photos/23440790/pexels-photo-23440790.jpeg',1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria) 
VALUES ('Anel Louvre','Design geométrico e vanguardista, com linhas que remetem à famosa pirâmide de vidro do museu. Moderno e artístico.',250.0,'https://images.pexels.com/photos/23440790/pexels-photo-23440790.jpeg',1);

-- 