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

SELECT
    id_cliente PK, IDcliente as FK, nome_cliente, sexo_cliente, bairro, cidade
FROM
    cliente, endereco
WHERE
    id_cliente = IDcliente;

SELECT
    C.nome_cliente AS Nome, C.sexo_cliente AS Sexo, E.bairro AS Bairro, E.cidade AS Cidade
FROM
    cliente C, endereco E
WHERE
    C.id_cliente = E.IDcliente;

SELECT 
    C.nome_cliente, 
    C.email_cliente, 
    E.rua, 
    E.bairro, 
    T.numero_telefone, 
    T.tipo_telefone
FROM
    cliente C
INNER JOIN 
    endereco E
ON 
    C.id_cliente = E.idcliente
INNER JOIN
    telefone T
ON
    C.id_cliente = T.idcliente
WHERE
    T.tipo_telefone LIKE 'COM';