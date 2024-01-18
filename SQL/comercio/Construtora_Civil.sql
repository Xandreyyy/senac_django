/*CREATES TABLE*/

create table construtora (
    cod_const VARCHAR (10) not null,
    cnpj VARCHAR (20) unique not null,
    nome_const VARCHAR (30) not null,
    primary key (cod_const)
);

create table engenheiro(
    crea varchar (8) not null,
    cpf cha varchar r(11) unique not null,
    nome_eng varchar (30) not null,
    area_atuacao varchar (20) not null,
    primary key (crea)
);

create table obra (
    cod_obra integer not null,
    nome_obra varchar(30) not null,
    localizacao varchar(50) not null,
    tipo varchar (15) not null,
    cod_const varchar (10) not null,
    cod_eng_resp varchar (8) not null,
    primary key (cod_obra),
    foreign key (cod_const) references construtora(cod_const),
    foreign key (cod_eng_resp) references engenheiro(crea)
);

create table operario(
    cart_trab varchar(15) not null,
    nomeop varchar(30) not null,
    endereco varchar(50) not null,
    telefone varchar(20),
    primary key (cart_trab)
);

create table obra_operario(
    cod_obra integer not null,
    cart_trab varchar(15) not null,
    data_local date not null,
    atividades varchar(200),
    primary key (cod_obra, cart_trab),
    foreign key (cod_obra) references obra(cod_obra),
    foreign key (cart_trab) references operario (cart_trab)
);

create table operario_construtora (
    cart_trab varchar(15) not null,
    cod_const varchar(10) not null,
    primary key (cart_trab, cod_const),
    foreign key (cart_trab) references operario (cart_trab),
    foreign key (cod_const) references construtora(cod_const)
);

/*INSERTS*/

-- CONSTRUTORA
insert into construtora values ('c1', '12365423512489','Encol'),
                               ('c2','78874529890133','Goldzstein'),
                               ('c3', '89083484166739','A3'),
                               ('c4', '87294592979871','Metaplan');

-- ENGENHEIRO
insert into engenheiro values ('e1','5637279211','Luis Silva','Edificacao'),
                              ('e2','73941939815','Carlos Alvarez','Pontes/Viadutos'),
                              ('e3','89058348193','Maria Souza','Pontes/Viadutos'),
                              ('e4','83489347851','Jose Silva','Edificacao');

-- OBRA
insert into obra values (01,'Boqueirao','BR 116, Km 25','Viaduto','c4','e2'),
                        (02,'Solar Firenze', 'Rua Mariland, 512 - Porto Alegre', 'Edificio', 'c1', 'e1'),
                        (03,'Serraria','Rua Sarandi, 600 - Porto Alegre','Ponte','c4','e3'),
                        (04,'Venezia','Av. Carlos Soares, 890 - Canoas','Edificio','c3','e4'),
                        (05,'Guaiba','Av. Praia de Belas, 1200 - Porto Alegre', 'Edificio', 'c2', 'e1'),
                        (06,'particular','Rua Ipanema, 310 - Porto Alegre','Casa','c3','e3');

-- OPERARIO
insert into operario values ('op030','Joao Souza','Rua Lima, 89 - Porto Alegre','249-9087'),
                            ('op010','Paulo Castro','Av. Protasio Alves, 23/101 - Porto Alegre',NULL),
                            ('op876','Luis Padilha','Av. Salgado Filho, 345 - Canoas','472-9083'),
                            ('op452','Marcos Freitas','Travessa do Canto, 67/304 - Porto Alegre','331-7838');

--OBRA_OPERARIO
insert into obra_operario values (03,'op010', '1997-06-15', 'preparacao da base'),
                                 (01,'op030', '1997-06-18', 'preparacao e colocacao de ferros'),
                                 (01,'op010', '1997-08-02', NULL),
                                 (02,'op876', '1997-08-20', 'pintura aberturas do 2o. andar'),
                                 (02,'op030', '1997-08-12', 'colocacao aberturas 20. andar'),
                                 (04,'op010', '1997-03-03', 'colocacao telhado');

-- OPERARIO_CONSTRUTORA
insert into operario_construtora values ('op010','c4'),
                                        ('op030','c4'),
                                        ('op030','c1'),
                                        ('op010','c3'),
                                        ('op876','c1');