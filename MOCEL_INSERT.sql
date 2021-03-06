/*
 *	Ingenieria de software I 
 *	Base de Datos MOCEL
 *	Insercion de Datos
 *	Integrantes: Andreina Marcano 09-10478
 *		     Luis Manuel Garcia 09-10963
 *	Tarea II
 */ 


/* 15 CLIENTES */
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '20410084', 'Luis Garcia', 'Carrizal, Calle Las Americas', '04262192501');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '15914863', 'Elizabeth Garcia', 'Carrizal, Calle Las Americas', '04142819888');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '4680373', 'Aura Herrera', 'Carrizal, Calle Las Americas', '04242800020');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '27098110', 'Andrea Garcia', 'Carrizal, Calle Las Americas', '04144529448');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', 'E470782', 'Vicente Garcia', 'Carrizal, Calle Las Americas', '02123831561');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('RIF', 'J333333330', 'Videojumes.ca', 'Carrizal, Calle Las Americas', '00582123831562');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('RIF', 'J222222220', 'OPEN ENGLISH', 'Caracas, los Cortijos', '00582244445566');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '19932833', 'Andreina Marcano', 'Montalbán II', '04142255770');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '20132762', 'Enrique Marcano', 'Montalbán II', '04169376778');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '4888029', 'Martha Pacheco', 'Montalbán II', '02124421985');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '3688956', 'Enrique Marcano', 'Montalbán II', '02124421985');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '5564485', 'Beatriz Pacheco', 'El Marques', '04167250280');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('RIF', 'J777788888', 'AVAA', 'Caracas, Los Cortijos', '005821121122111');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('RIF', 'J999900000', 'AJE', 'Sartenejas, Universidad Simón Bolívar', '02129964894');
INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES ('CI', '11123456', 'Aura Garcia', 'Carrizal, Calle Las Americas', '04265555555');


/* 5 PAQUETES DE SERVICIOS, EL PAQUETE 0002 NO TIENE SUSCRIPTORES */
INSERT INTO PAQUETE(CODIGO_PAQUETE, NOMBRE_PAQUETE, DESCRIPCION, MONTO_PAQUETE) VALUES ('0001', 'MOCEL 2000', 'ZZZZZZ1', 49.00);
INSERT INTO PAQUETE(CODIGO_PAQUETE, NOMBRE_PAQUETE, DESCRIPCION, MONTO_PAQUETE) VALUES ('1101', 'MIXTO PLUS', 'ZZZZZZ2', 211.00);
INSERT INTO PAQUETE(CODIGO_PAQUETE, NOMBRE_PAQUETE, DESCRIPCION, MONTO_PAQUETE) VALUES ('1102', 'Pegadito con otros 1500', 'ZZZZZZ3', 16.00);	
INSERT INTO PAQUETE(CODIGO_PAQUETE, NOMBRE_PAQUETE, DESCRIPCION, MONTO_PAQUETE) VALUES ('0002', 'Pegadito con otros 30', 'ZZZZZZ4', 19.00);
INSERT INTO PAQUETE(CODIGO_PAQUETE, NOMBRE_PAQUETE, DESCRIPCION, MONTO_PAQUETE) VALUES ('2201', 'Mensajes 800', 'ZZZZZZ5', 38.00);	


/* 6 TIPOS DE SERVICIOS */
INSERT INTO SERVICIO(CODIGO_SERVICIO, NOMBRE_SERVICIO, DESCRIPCION, TARIFA_BASICA) VALUES ('20001', 'Seg MOCEL-MOCEL', 'AAAAA', 0.01150);
INSERT INTO SERVICIO(CODIGO_SERVICIO, NOMBRE_SERVICIO, DESCRIPCION, TARIFA_BASICA) VALUES ('20002', 'Seg Otros moviles', 'BBBBB', 0.01250);
INSERT INTO SERVICIO(CODIGO_SERVICIO, NOMBRE_SERVICIO, DESCRIPCION, TARIFA_BASICA) VALUES ('20003', 'Seg Fijos', 'CCCCC', 0.01150);
INSERT INTO SERVICIO(CODIGO_SERVICIO, NOMBRE_SERVICIO, DESCRIPCION, TARIFA_BASICA) VALUES ('20004', 'Mensajes', 'DDDDD', 0.500);		/* MONTO IRREAL */
INSERT INTO SERVICIO(CODIGO_SERVICIO, NOMBRE_SERVICIO, DESCRIPCION, TARIFA_BASICA) VALUES ('20005', 'Buzon de msjs', 'EEEEE', 20.00);		/* MONTO IRREAL */


/* 12 INCLUSIONES DE SERVICIOS EN PAQUETES */
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('0001', '20001', 1000);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('1101', '20001', 39000);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('0001', '20002', 1000);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('1101', '20002', 2600);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('1101', '20003', 5000);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('0001', '20004', 200);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('1101', '20004', 200);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('0001', '20005', 1);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('1101', '20005', 1);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('1102', '20002', 1500);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('0002', '20002', 1800);
INSERT INTO INCLUYE(CODIGO_PAQUETE, CODIGO_SERVICIO, CANT_SERVICIO) VALUES ('2201', '20004', 800);


/* 2 TIPOS DE PLANES, UNO PREPAGO Y OTRO POSTPAGO */
INSERT INTO PLAN(CODIGO_PLAN, NOMBRE_PLAN, DESCRIPCION, RENTA_BASICA, CODIGO_PAQUETE) VALUES ('001', 'MOCEL 2000', 'XXXXX1', 49.00, '0001');
INSERT INTO PLAN(CODIGO_PLAN, NOMBRE_PLAN, DESCRIPCION, RENTA_BASICA, CODIGO_PAQUETE) VALUES ('101', 'MIXTO PLUS', 'YYYYY1', 211.00, '1101');

INSERT INTO PLAN_PREPAGO(CODIGO_PLAN) VALUES ('001');

INSERT INTO PLAN_POSTPAGO(CODIGO_PLAN) VALUES ('101');


/* 19 PRODUCTOS VENDIDOS, (4 CLIENTES TIENEN 2 PRODUCTOS, UNO PREPAGO Y OTRO POSTPAGO (PRIMEROS 8 PRODUCTOS), EL RESTO SOLO TIENE UN PRODUCTO) */
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5000', '20410084', '001', 'BB310', 'AABBCC', 'd', '5050505084848484', '11-08-2018', 'Mercantil', '11', '11-08-2012', 'E', 200.00);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5001', '20410084', '101', 'Letus', 'DDEEFF', 'd', '5050505084848484', '11-08-2118', 'Mercantil', '11', '11-08-2012', 'O', 0.00);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5002', '19932833', '001', 'BB310', 'AABBCC', 'c', '5050505066668888', '19-12-2016', 'Mercantil', '19', '19-12-2011', 'E', 14.50);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5003', '19932833', '101', 'Letus', 'DDEEFF', 'c', '5050505066668888', '19-12-2116', 'Mercantil', '19', '19-12-2011', 'O', 0.00);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5004', 'J777788888', '001', 'Zenzei', 'GGHHII', 'C', '5555000055550000', '15-05-2015', 'Banesco', '06', '06-06-2012', 'E', 308.00);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5005', 'J777788888', '101', 'Letus', 'DDEEFF', 'C', '5555000055550000', '15-05-2015', 'Banesco', '22', '06-06-2012', 'O', 0.00);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5006', 'J999900000', '001', 'Zenzei', 'GGHHII', 'D', '1515151515151515', '30-10-2017', 'Bancaribe', '01', '01-12-2006', 'E', 3.30);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5007', 'J999900000', '101', 'Letus', 'DDEEFF', 'D', '1515151515151515', '30-10-2017', 'Bancaribe', '01', '01-12-2006', 'O', 0.00);

INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5008', '4680373', '001', 'BB310', 'AABBCC', 'D', '1212121289898989', '05-05-2015', 'Banesco', '02', '02-06-2012', 'E', 34.34);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5009', 'E470782', '001', 'Letus', 'DDEEFF', 'D', '1212121234343434', '05-05-2015', 'Banesco', '03', '03-06-2012', 'E', 8.8);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5010', '4888029', '001', 'BB310', 'AABBCC', 'D', '1212121278787878', '14-10-2017', 'Banco de Venezuela', '26', '26-12-2011', 'E', 0.15);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5011', '3688956', '001', 'Letus', 'DDEEFF', 'D', '1212121245454545', '14-10-2017', 'Banco de Venezuela', '27', '27-12-2011', 'E', 90.56);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5012', '27098110', '001', 'Zenzei', 'GGHHII', 'D', '1212121221212121', '01-01-2014', 'Mercantil', '27', '27-12-2012', 'E', 4.80);

INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5013', '15914863', '101', 'BB310', 'AABBCC', 'C', '7777888899990000', '05-09-2015', 'Bicentenario', '02', '02-06-2012', 'O', 0.00);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5014', '11123456', '101', 'Zenzei', 'GGHHII', 'C', '1111222233334444', '05-09-2015', 'Banesco', '03', '03-01-2013', 'O', 0.00);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5015', '20132762', '101', 'BB310', 'AABBCC', 'C', '5555666677778888', '14-02-2017', 'Bicentenario', '09', '09-02-2013', 'O', 0.00);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5016', '5564485', '101', 'Zenzei', 'GGHHII', 'C', '9999000011112222', '14-02-2017', 'Mercantil', '09', '09-12-2012', 'O', 0.00);

INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5017', 'J333333330', '001', 'BB310', 'AABBCC', 'c', '4455445544554455', '14-09-2018', 'Banco de Venezuela', '04', '04-02-2013', 'E', 100.00);
INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES ('5018', 'J222222220', '101', 'Zenzei', 'GGHHII', 'C', '6677667766776677', '16-06-2018', 'Mercantil', '04', '04-11-2012', 'O', 0.00);


/* MUCHOS CONSUMOS, CADA PRODUCTO AFILIADO AL PLAN PREPAGO CONSUME 4 SERVICIOS, CADA PRODUCTO AFILIADO AL PLAN POSTPAGO CONSUME 5 SERVICIOS */
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5000', '20001', 500);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5000', '20002', 1000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5000', '20004', 150);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5000', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5001', '20001', 500);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5001', '20002', 1000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5001', '20003', 4999);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5001', '20004', 150);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5001', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5002', '20001', 1003);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5002', '20002', 1003);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5002', '20004', 203);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5002', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5003', '20001', 40000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5003', '20002', 3000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5003', '20003', 5500);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5003', '20004', 250);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5003', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5004', '20001', 200);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5004', '20002', 1999);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5004', '20004', 150);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5004', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5005', '20001', 500);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5005', '20002', 3000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5005', '20003', 4999);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5005', '20004', 150);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5005', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5006', '20001', 167);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5006', '20002', 888);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5006', '20004', 200);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5006', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5007', '20001', 34000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5007', '20002', 2500);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5007', '20003', 5000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5007', '20004', 144);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5007', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5008', '20001', 300);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5008', '20002', 1010);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5008', '20004', 1004);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5008', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5009', '20001', 1100);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5009', '20002', 888);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5009', '20004', 13);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5009', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5010', '20001', 300);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5010', '20002', 1010);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5010', '20004', 500);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5010', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5011', '20001', 1100);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5011', '20002', 888);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5011', '20004', 13);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5011', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5012', '20001', 300);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5012', '20002', 3000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5012', '20004', 300);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5012', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5013', '20001', 40000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5013', '20002', 43);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5013', '20003', 5000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5013', '20004', 1004);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5013', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5014', '20001', 30000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5014', '20002', 43);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5014', '20003', 5000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5014', '20004', 100);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5014', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5015', '20001', 444);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5015', '20002', 4000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5015', '20003', 5000);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5015', '20004', 500);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5015', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5016', '20001', 4444);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5016', '20002', 300);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5016', '20003', 4999);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5016', '20004', 100);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5016', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5017', '20001', 1001);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5017', '20002', 1001);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5017', '20004', 201);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5017', '20005', 1);

INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5018', '20001', 39001);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5018', '20002', 2601);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5018', '20003', 5001);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5018', '20004', 201);
INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES ('5018', '20005', 1);


/* 24 ASOCIACIONES DE PRODUCTOS CON PAQUETES, UNA POR PRODUCTO MAS 5 ADICIONALES */
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5000', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5001', '1101');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5002', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5003', '1101');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5004', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5005', '1101');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5006', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5007', '1101');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5008', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5009', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5010', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5011', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5012', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5013', '1101');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5014', '1101');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5015', '1101');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5016', '1101');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5017', '0001');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5018', '1101');

INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5005', '1102');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5008', '2201');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5010', '2201');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5013', '2201');
INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES ('5015', '2201');


		


