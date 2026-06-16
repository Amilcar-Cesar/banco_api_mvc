-- Active: 1781618138773@@localhost@3306@bank_database
CREATE TABLE IF NOT EXISTS `pessoa_fisica` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    renda_mensal DECIMAL(12, 2),
    idade INT,
    nome_completo VARCHAR(255),
    celular VARCHAR(50),
    email VARCHAR(255),
    categoria VARCHAR(50),
    saldo DECIMAL(12, 2)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS `pessoa_juridica` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    renda_mensal DECIMAL(12, 2),
    idade INT,
    nome_completo VARCHAR(255),
    celular VARCHAR(50),
    email VARCHAR(255),
    categoria VARCHAR(50),
    saldo DECIMAL(12, 2)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;