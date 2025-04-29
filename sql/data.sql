CREATE TABLE diretores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE generos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    diretor_id INT NOT NULL,
    genero_id INT NOT NULL,
    ano_lancamento INT NOT NULL,
    classificacao_indicativa VARCHAR(10),
    FOREIGN KEY (diretor_id) REFERENCES diretores(id),
    FOREIGN KEY (genero_id) REFERENCES generos(id)
);

-- Inserindo diretores
INSERT INTO diretores (nome) VALUES
('Christopher Nolan'),
('Bong Joon-ho'),
('Anthony e Joe Russo'),
('Jon Favreau'),
('Francis Ford Coppola'),
('Lana e Lilly Wachowski');

-- Inserindo gêneros
INSERT INTO generos (nome) VALUES
('Ficção Científica'),
('Drama'),
('Ação'),
('Animação'),
('Crime'),
('Aventura');

-- Inserindo filmes
INSERT INTO filmes (titulo, diretor_id, genero_id, ano_lancamento, classificacao_indicativa) VALUES
('Interstellar', 1, 1, 2014, '12'),
('Parasita', 2, 2, 2019, '16'),
('Vingadores: Ultimato', 3, 3, 2019, '12'),
('O Rei Leão', 4, 4, 2019, 'Livre'),
('O Poderoso Chefão', 5, 5, 1972, '18'),
('Matrix', 6, 1, 1999, '16');

