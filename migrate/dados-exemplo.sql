-- INSERT DE CATEGORIAS

INSERT INTO categorias(nome_categoria) VALUES ('Anel');
INSERT INTO categorias(nome_categoria) VALUES ('Pulseira');
INSERT INTO categorias(nome_categoria) VALUES ('Brinco');
INSERT INTO categorias(nome_categoria) VALUES ('Colar');
select * from categorias;
-- INSERT DE PRODUTOS


-- Anel
INSERT INTO produtos(produto, descr, preco, foto, id_categoria) 
VALUES ('Anel Tuileries','Um anel delicado com detalhes florais ou pequenas folhas esculpidas, inspirado nos jardins mais charmosos de Paris.',250.0,'https://images.pexels.com/photos/23440790/pexels-photo-23440790.jpeg',1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria) 
VALUES ('Anel Versailles','Uma peça suntuosa e detalhada, com uma pedra central imponente, inspirada no luxo e na arquitetura do famoso palácio.',250.0,'https://images.pexels.com/photos/19525067/pexels-photo-19525067.jpeg',1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria) 
VALUES ('Anel Bastille','Um aro robusto e texturizado, simbolizando força, atitude e a busca por liberdade. Famoso pelo bom gosto e charme.',250.0,'https://images.pexels.com/photos/19764335/pexels-photo-19764335.jpeg',1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria) 
VALUES ('Anel Louvre','Design geométrico e vanguardista, com linhas que remetem à famosa pirâmide de vidro do museu. Moderno e artístico.',250.0,'https://images.pexels.com/photos/19525064/pexels-photo-19525064.jpeg',1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria) 
VALUES ('Anel Marais','Um modelo statement (pesado e estiloso), com design urbano e assimétrico, inspirado no bairro mais descolado e artístico de Paris.', 250.0,'https://images.pexels.com/photos/2732096/pexels-photo-2732096.jpeg',1);


-- Colar
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Colar Notre-Dame', 'Uma medalha detalhada com arabescos ou estilo vitral, inspirada na grandiosidade da arte gótica francesa.', 250.0, 'https://images.pexels.com/photos/13292930/pexels-photo-13292930.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Colar Champagne', 'Uma gargantilha delicada com pequenas esferas de metal ou cristais pendurados que lembram o borbulhar da famosa bebida.', 250.0, 'https://images.pexels.com/photos/10356136/pexels-photo-10356136.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Colar Chamonix', 'Um colar longo com um pingente de cristal lapidado ou pedra bruta, remetendo ao gelo e à sofisticação dos Alpes Franceses.', 250.0, 'https://images.pexels.com/photos/20518711/pexels-photo-20518711.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Colar Arc', 'Uma gargantilha rígida estilo choker com design semicircular marcante, celebrando vitórias e a elegância urbana do Arco do Triunfo.', 250.0, 'https://images.pexels.com/photos/13292426/pexels-photo-13292426.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Colar Montmartre', 'Uma corrente longa com um pingente em formato de paleta de pintor ou medalha texturizada, homenageando o berço da boemia e dos artistas parisienses.', 250.0, 'https://images.pexels.com/photos/13292930/pexels-photo-13292930.jpeg', 1);


-- Pulseira
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Pulseira Riviera', 'Um bracelete clássico, sofisticado e inteiramente cravejado de brilhantes, que evoca o glamour da costa sul francesa.', 250.0, 'https://images.pexels.com/photos/34399114/pexels-photo-34399114.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Pulseira Provence', 'Uma peça romântica e maleável, idealmente com tons lilases ou texturas que lembram os campos de lavanda.', 250.0, 'https://images.pexels.com/photos/34399141/pexels-photo-34399141.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Pulseira Seine', 'Uma corrente fluida e de brilho contínuo, que imita o movimento suave das águas do rio Sena.', 250.0, 'https://images.pexels.com/photos/34399156/pexels-photo-34399156.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Pulseira Sorbonne', 'Um bracelete rígido, liso e polido. Passa uma imagem intelectual, minimalista e atemporal.', 250.0, 'https://images.pexels.com/photos/34399115/pexels-photo-34399115.jpeg', 1);



-- Brinco
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Brinco Eiffel', ' Brincos longos e estruturados que afinam na ponta, fazendo uma alusão elegante e sutil à silhueta da Torre Eiffel.', 250.0, 'https://images.pexels.com/photos/34372559/pexels-photo-34372559.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Brinco Mon Amour', 'Pequenos brincos de argola ou pino em formato de coração estilizado, trazendo o lado romântico e apaixonante de Paris.', 250.0, 'https://images.pexels.com/photos/34372554/pexels-photo-34372554.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Brinco Bordeaux', ' Brincos de gota com pedras em tom de vermelho-escuro profundo, celebrando a sofisticação dos vinhos franceses.', 250.0, 'https://images.pexels.com/photos/34372576/pexels-photo-34372576.jpeg', 1);
INSERT INTO produtos(produto, descr, preco, foto, id_categoria)
VALUES ('Brinco Lumière', ' Ear cuffs ou brincos que irradiam muito brilho, uma homenagem à "Cidade Luz" e ao cinema dos irmãos Lumière', 250.0, 'https://images.pexels.com/photos/34372575/pexels-photo-34372575.jpeg', 1);

select * from comentarios;

INSERT INTO usuarios (nome_completo, email, telefone, endereco, senha) VALUES ("Erica Santos", "erica123@gmail.com", "557836478","Avenida do sol 123", 3345);
INSERT INTO comentarios(codigo_usuario, comentario) VALUES (1,"Produto incrível! a qualidade é ótima e muito bem feito!");
SELECT usuarios.nome_completo, comentarios.comentario from comentarios
INNER JOIN usuarios on usuarios.nome_completo = usuarios.nome_completo;

SELECT produto, descr, preco, foto FROM produtos WHERE codigo = 1;