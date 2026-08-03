CREATE DATABASE CR7GOAT;
USE CR7GOAT;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    tipo VARCHAR(20) NOT NULL
);

SELECT * FROM usuario
;

INSERT INTO usuario (email, senha, tipo)
VALUES
('murilorohohmann@gmail.com', 'hohmann', 'admin');


USE CR7GOAT;


CREATE TABLE IF NOT EXISTS estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    quantidade INT DEFAULT 0
);


INSERT INTO estoque (produto, categoria, quantidade) VALUES 
('Luva de Proteção', 'EPI', 15),
('Chave de Fenda', 'Ferramentas', 8),
('Capacete Industrial', 'EPI', 5);
