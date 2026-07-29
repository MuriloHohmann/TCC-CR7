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