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