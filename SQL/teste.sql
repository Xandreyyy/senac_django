CREATE TABLE cliente (
  id BIGINT, 
  idade BIGINT, 
  sexo CHAR,
  dependentes BIGINT, 
  escolaridade VARCHAR(80), 
  tipo_cartao VARCHAR(80), 
  limite_credito FLOAT, 
  valor_transacoes_12m FLOAT, 
  qtd_transacoes_12m BIGINT
);

-- SHOW TABLES; -- mostrar tabelas
-- DESC cliente; -- descrever a tabela

-- INSERT -> insere dados na última linha da tabela
-- antes inseria dados desta maneira:
INSERT INTO cliente (
	id,
  idade, 
  sexo,
  dependentes, 
  escolaridade, 
  tipo_cartao, 
  limite_credito, 
  valor_transacoes_12m, 
  qtd_transacoes_12m
) VALUES (
  111111111,
  45,
  'M',
  3,
  'ensino medio',
  'blue',
  12691.51,
  1144.90,
  42
);

-- atualmente se insere desta forma:
INSERT INTO cliente VALUES (222222222, 49, 'M', 3, 'ensino medio', 'blue', 12691.51, 1144.90, 42);

-- inserir mais de um registro em uma query
INSERT INTO cliente VALUES (333333333, 40, 'F', 5, 'ensino fundamental', 'blue', 15691.51, 1024.90, 37),
                           (444444444, 49, 'F', 5, 'mestrado', 'red', 8256.96, 1291.45, 33),
                           (555555555, 51, 'M', 3, 'mestrado', 'blue', 3418.56, 1887.72, 20);

-- SELECT -> consultará a tabela

SELECT * FROM cliente;

SELECT id, escolaridade, sexo FROM cliente;

SELECT * from cliente LIMIT 1;

SELECT * FROM cliente WHERE sexo = 'F' AND tipo_cartao = "blue";

SELECT AVG(idade) AS media_linda from cliente;

SELECT
	id AS codigo,
  dependentes as filhos,
  valor_transacoes_12m as gastos
FROM
	cliente
WHERE
	sexo = 'F';

/*como usar order by*/

-- ===========================================================

CREATE TABLE transacao (
    id_transacao INT,
    id_cliente INT, 
    data_compra DATE,
    valor FLOAT
);

ALTER TABLE transacao ADD id_loja varchar(20);
ALTER TABLE transacao MODIFY COLUMN valor DOUBLE;
ALTER TABLE transacao DROP COLUMN id_loja;

INSERT INTO transacao VALUES (1, 768805383, "2021-06-10", 50.74,"magalu"),
                  			  (2, 768805399, "2021-06-13", 30.90,"giraffas"),
                			  (3, 818770008, "2021-06-05", 110.00,"postoshell"); 
SELECT * from transacao;

DESC transacao;

DELETE FROM transacao;

DELETE FROM transacao WHERE valor = 110;

UPDATE transacao SET id_loja = "postoshell" WHERE id_transacao = 3;