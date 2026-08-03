CREATE DATABASE CR7GOAT;
USE CR7GOAT;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    tipo VARCHAR(20) NOT NULL
);

SELECT * FROM estoque
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


USE CR7GOAT;

CREATE TABLE IF NOT EXISTS historico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100) NOT NULL,
    acao VARCHAR(50) NOT NULL,
    produto VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
);