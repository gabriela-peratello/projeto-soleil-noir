INSERT INTO usuarios (nome_completo, email, telefone, endereco, senha) VALUES ("Erica Santos", "erica123@gmail.com", "557836478","Avenida do sol 123", 3345);
INSERT INTO comentarios(codigo_usuario, comentario) VALUES (1,"Produto incrível! a qualidade é ótima e muito bem feito!");
SELECT usuarios.nome_completo, comentarios.comentario from comentarios
INNER JOIN usuarios on usuarios.nome_completo = usuarios.nome_completo;