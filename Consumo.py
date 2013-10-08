#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase CONSUMO
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
import busquedasdb
import Producto
import Servicio

class Consumo():
		
	def __init__(self, codProd, codServicio, cantConsumida):
		self._codProd = codProd
		self._codServicio = codServicio
		self._cantConsumida = cantConsumida

	# Los siguientes metodos obtienen y modifican los datos del consumo.
	def getCodProducto(self):
		return self._codProd
	
	def setCodProducto(self, codProd):
		self._codProd = codProd 
		
	def getCodServicio(self):
		return self._codServicio
	
	def setCodServicio(self, codServicio):
		self._codServicio = codServicio
		
	def getCantConsumida(self):
		return self._cantConsumida
		
	def setCantConsumida(self, cantConsumida):
		self._cantConsumida = cantConsumida
		
	# Imprime por pantalla la informacion de un consumo
	def imprimir(self):
	    print self.getCodProducto()
	    print self.getCodServicio()
	    print self.getCantConsumida()    
	
	# Agrega el consumo de un servicio por un producto en la tabla CONSUME.
	def registrarConsumo(self):
		busq = busquedasdb.busquedadb()
		productoValido = busq.buscarProducto(self.getCodProducto())
		if productoValido:
			servicioValido = busq.buscarServicio(self.getCodServicio())
			if servicioValido:
				conex = conexiondb.ConexionMOCEL()
				consumoExistente = self.obtenerConsumoAnterior()
				if consumoExistente:
					consumoExistente = consumoExistente + self.getCantConsumida()
					query = "UPDATE CONSUME C SET CANT_CONSUMIDA = "+ str(consumoExistente) +" WHERE (C.CODIGO_PRODUCTO = '"+self.getCodProducto()+"' AND C.CODIGO_SERVICIO = '"+self.getCodServicio()+"');" 
					conex.cur.execute(query)
					conex.con.commit()
					conex.cerrarConexion()
					print "Se ha actualizado correctamente el consumo del servicio"
				else:
					ProductoAPaqueteAServicio = self.ProductoAPaqueteAServicio(self.getCodProducto(), self.getCodServicio())
					if ProductoAPaqueteAServicio:
						query = "INSERT INTO CONSUME(CODIGO_PRODUCTO, CODIGO_SERVICIO, CANT_CONSUMIDA) VALUES (%s, %s, %s);"
						data = (self.getCodProducto(), self.getCodServicio(), self.getCantConsumida())
						conex.cur.execute(query, data)
						conex.con.commit()
						conex.cerrarConexion()
						print "Se ha registrado correctamente el consumo del servicio"
					else:
						print "El producto no esta afiliado al servicio"
			else:
				print "El servicio no existe en el sistema"
		else:
			print "El producto no ha sido registrado en el sistema"

	# Actualiza a cero el consumo.
	def actualizarACero(self):
		conex = conexiondb.ConexionMOCEL()
		# Buzon de voz
		if self.getCodServicio() == '20005':
			query = "UPDATE CONSUME C SET CANT_CONSUMIDA = "+ str(1) +" WHERE (C.CODIGO_PRODUCTO = '"+self.getCodProducto()+"' AND C.CODIGO_SERVICIO = '"+self.getCodServicio()+"');" 
		# cualquier otro servicio
		else:
			query = "UPDATE CONSUME C SET CANT_CONSUMIDA = "+ str(0) +" WHERE (C.CODIGO_PRODUCTO = '"+self.getCodProducto()+"' AND C.CODIGO_SERVICIO = '"+self.getCodServicio()+"');" 
		conex.cur.execute(query)
		conex.con.commit()
		conex.cerrarConexion()
		print "Se ha actualizado correctamente el consumo del servicio"

	# Verifica que el producto a traves del paquete tiene acceso al servicio. 
	def ProductoAPaqueteAServicio(self):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT A.CODIGO_PAQUETE FROM ASOCIA A, INCLUYE I WHERE (A.CODIGO_PRODUCTO = '"+self.getCodProducto()+"' AND I.CODIGO_SERVICIO = '"+self.getCodServicio+"' AND A.CODIGO_PAQUETE = I.CODIGO_PAQUETE);"
		conex.cur.execute(query)
		for elem in conex.cur.fetchall():
			conex.cerrarConexion()
			return elem
		conex.cerrarConexion()
		return False

	# Devuelve de la tabla CONSUME el consumo existente de un servicio por un producto. 
	def obtenerConsumoAnterior(self):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT * FROM CONSUME C WHERE (C.CODIGO_PRODUCTO = '"+self.getCodProducto()+"' AND C.CODIGO_SERVICIO = '"+self.getCodServicio()+"');"	
		conex.cur.execute(query)
		for elem in conex.cur.fetchall():
			conex.cerrarConexion()
			return elem[2]
		conex.cerrarConexion()
		return False

	# Devuelve de la tabla CONSUME a un consumo previamente buscado. 
	def consultarConsumo(self):
		busq = busquedasdb.busquedadb()
		consumoValido = busq.buscarConsumo(self.getCodProducto(), self.getCodServicio())
		if consumoValido:
			conex = conexiondb.ConexionMOCEL()
			query = "SELECT * FROM CONSUME C WHERE (C.CODIGO_PRODUCTO = '"+self.getCodProducto()+"' AND C.CODIGO_SERVICIO = '"+self.getCodServicio()+"');"	
			conex.cur.execute(query)
			self.imprimir()
			conex.cerrarConexion()
		else:
			print "El consumo no ha sido registrado en el sistema"	


# Principal    
if __name__== "__main__":
	cons = Consumo('5004', '20004', 0)
	cons2 = Consumo('5002', '20003', 56)
	cons3 = Consumo('5000', '20004', 4)
	print "********************************************************************"
	cons.actualizarACero()
	print "********************************************************************"
	cons.consultarConsumo()
	print "********************************************************************"
	cons2.consultarConsumo()
	print "********************************************************************"
	print cons3.obtenerConsumoAnterior()
	cons3.registrarConsumo()
	print cons3.obtenerConsumoAnterior()
	print "********************************************************************"

