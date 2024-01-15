CREATE TABLE cliente (
    id_cliente INTEGER(4) PRIMARY KEY,
    idade_cliente INTEGER(2),
    cpf_cliente CHAR(14),
    email_cliente VARCHAR(35),
    nome_cliente VARCHAR(40),
    carro INTEGER(4)
);

CREATE TABLE carro (
    id_carro INTEGER(4) PRIMARY KEY,
    marca_carro VARCHAR(15),
    modelo_carro VARCHAR(10),
    motor_carro VARCHAR(20),
    cor_carro VARCHAR(15),
    acessorios_carro VARCHAR(30)
);
 
ALTER TABLE cliente ADD CONSTRAINT FK_cliente_2
    FOREIGN KEY (carro)
    REFERENCES carro (id_carro);