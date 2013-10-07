#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase BUSQUEDA DATA BASES
#	Integrantes: Andreina Marcano 09-10478
#		     Luis Manuel Garcia 09-10963
#		     Vanessa Ballestes 08-10091
#		     Franco Nori 08-10801
#		     Bernardo Morales 08-10770
#	Tarea III
# 
 
import psycopg2
import unittest
import conexiondb

# Realiza las busquedas necesarias para hacer validaciones
class busquedadb():

	def __init__(self):
		pass

	# Busca en la tabla CLIENTE a un cliente.
	@staticmethod
	def buscarCliente(ID):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT C.IDENTIFICADOR FROM CLIENTE C WHERE (C.IDENTIFICADOR = '"+ID+"');"	
		conex.cur.execute(query)
		for elem in conex.cur.fetchall():
			conex.cerrarConexion()
			return True
		conex.cerrarConexion()
		return False	

	# Busca en la tabla PRODUCTO a un producto. 
	@staticmethod
	def buscarProducto(codProducto):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT P.CODIGO_PRODUCTO FROM PRODUCTO P WHERE (P.CODIGO_PRODUCTO = '"+str(codProducto)+"');"
		conex.cur.execute(query)
		for elem in conex.cur.fetchall():
			conex.cerrarConexion()
			return True
		conex.cerrarConexion()
		return False

	# Busca en la tabla PLAN a un plan
	@staticmethod
	def buscarPlan(codPlan):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT P.CODIGO_PLAN FROM PLAN P WHERE (P.CODIGO_PLAN = '"+codPlan+"');"	
		conex.cur.execute(query)
		for elem in conex.cur.fetchall():
			conex.cerrarConexion()
			return True
		conex.cerrarConexion()
		return False	

	# Busca en la tabla PAQUETE a un paquete.	
	@staticmethod
	def buscarPaquete(codPaquete):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT P.CODIGO_PAQUETE FROM PAQUETE P WHERE (P.CODIGO_PAQUETE = '"+codPaquete+"');"
		conex.cur.execute(query)
		for elem in conex.cur.fetchall():
			conex.cerrarConexion()
			return True
		conex.cerrarConexion()
		return False

	# Busca en la tabla Servicio a un servicio.	
	@staticmethod
	def buscarServicio(codServicio):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT S.CODIGO_SERVICIO FROM SERVICIO S WHERE (S.CODIGO_SERVICIO = '"+codServicio+"');"
		conex.cur.execute(query)
		for elem in conex.cur.fetchall():
			conex.cerrarConexion()
			return True
		conex.cerrarConexion()
		return False

	# Busca en la tabla ASOCIA a una afiliacion. 
	@staticmethod
	def buscarAfiliacion(codProducto, codPaquete):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT * FROM ASOCIA A WHERE (A.CODIGO_PRODUCTO = '"+codProducto+"' AND A.CODIGO_PAQUETE = '"+codPaquete+"');"
		conex.cur.execute(query)
		for elem in conex.cur.fetchall():
			conex.cerrarConexion()
			return True
		conex.cerrarConexion()
		return False

	# Busca en la tabla CONSUME a un consumo. 
	@staticmethod
	def buscarConsumo(codProducto, codServicio):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT * FROM CONSUME C WHERE (C.CODIGO_PRODUCTO = '"+codProducto+"' AND C.CODIGO_SERVICIO = '"+codServicio+"');"
		conex.cur.execute(query)
		for elem in conex.cur.fetchall():
			conex.cerrarConexion()
			return True
		conex.cerrarConexion()
		return False



