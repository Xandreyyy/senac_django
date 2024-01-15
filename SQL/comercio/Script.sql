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
    "Jose",
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