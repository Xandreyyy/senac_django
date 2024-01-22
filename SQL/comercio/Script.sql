CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(40) NOT NULL,
    idade_cliente INT(2) NOT NULL,
    sexo_cliente CHAR(1) NOT NULL,
    cpf_cliente CHAR(14) NOT NULL,
    email_cliente VARCHAR(40)
);

INSERT INTO cliente VALUES (
    NULL,
    "José",
    67,
    'M',
    "948.255.880-42",
    NULL
);

INSERT INTO CLIENTE VALUES (NULL,'João', 45, 'M','76567587887','JOAOA@IG.COM'),
                           (NULL,'Carlos', 38, 'M','5464553466','CARLOSA@IG.COM'),
                           (NULL,'Ana',31, 'F','456545678','ANA@IG.COM'),
                           (NULL,'Clara',60,'F','5687766856',NULL),
                           (NULL,'Jorge',28, 'M','8756547688','JORGE@IG.COM'),
                           (NULL,'Celia',57, 'M','5767876889','JCELIA@IG.COM');

-- -------------------------------------------------------------------------------

CREATE TABLE endereco (
    id_endereco INT(4) PRIMARY KEY AUTO_INCREMENT,
    rua VARCHAR(30) NOT NULL,
    bairro VARCHAR(20) NOT NULL,
    cidade VARCHAR(20) NOT NULL,
    estado CHAR(2) NOT NULL,
    IDcliente INT,
    FOREIGN KEY (IDcliente) REFERENCES cliente (id_cliente)
);

CREATE TABLE telefone (
    id_telefone INT PRIMARY KEY AUTO_INCREMENT,
    tipo_telefone ENUM("RES", "COM", "CEL"),
    numero_telefone VARCHAR(15) NOT NULL,
    IDcliente INT,
    FOREIGN KEY (IDcliente) REFERENCES cliente (id_cliente)
);

/* UTILIZANDO HAVING */aaa
SELECT
    departamento, COUNT(idFuncionario) as "Qtd. funcionarios"
FROM
    funcionarios
GROUP BY
    departamento
HAVING
    COUNT(idFuncionario) >= 2
ORDER BY
    COUNT(idFuncionario) DESC;

/* CONTAR QUANTOS REGISTROS TEM POR ESTADO*/
SELECT
    COUNT(id_endereco), estado
FROM
    endereco
GROUP BY
    estado
HAVING
    COUNT(id_endereco) > 1
ORDER BY
    COUNT(idCliente) DESC;

/* USANDO BETWEEN*/
SELECT
    C.nome_cliente AS Cliente, E.estado AS Estado
FROM
    cliente C
INNER JOIN
    endereco E
    ON
    C.id_cliente = E.IDcliente
WHERE
    E.estado BETWEEN "PR" AND "RS";

/* PROJETAR ID DOS CLIENTES ENTRE 10 E 15 */
SELECT
    id_cliente, nome_cliente, email_cliente
FROM
    cliente
WHERE
    id_cliente BETWEEN 10 AND 15;

-- ------------------------------------------
SELECT
    id_cliente AS ID, nome_cliente AS Nome, idade_cliente AS Idade
FROM
    cliente
WHERE
    id_cliente BETWEEN 1 AND 10
    AND
    idade_cliente IN (31, 38, 45);