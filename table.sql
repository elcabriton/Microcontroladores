CREATE TABLE password_access (
    senha VARCHAR(6) NOT NULL,
    ultimo_acesso DATE NOT NULL,
    fotos_tentativas BLOB,
    PRIMARY KEY (senha)
);