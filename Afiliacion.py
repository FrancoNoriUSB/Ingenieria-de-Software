#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase AFILIACION
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
import Paquete

class Afiliacion():
	def __init__(self, codProducto, codPaquete):
		self._codProducto = codProducto
		self._codPaquete = codPaquete

	# Los siguientes metodos obtienen y modifican los datos de la asociacion		
	def getCodProducto(self):
		return self._codProducto
	
	def setCodProducto(self, codProducto):
		self._codProducto = codProducto 
		
	def getCodPaquete(self):
		return self._codPaquete
	
	def setCodPaquete(self, codPaquete):
		self._codPaquete = codPaquete

	# Imprime por pantalla la informacion de un servicio		
	def imprimir(self):
	    print self.getCodProducto()
	    print self.getCodPaquete()

	# Agrega la afiliacion de un producto a un paquete en la tabla ASOCIA.
	def afiliarProductoAPaquete(self):
		busq = busquedasdb.busquedadb()
		productoValido = busq.buscarProducto(self.getCodProducto())
		if productoValido:
			paqueteValido = busq.buscarPaquete(self.getCodPaquete())
			if paqueteValido:
				afiliacionExistente = busq.buscarAfiliacion(self.getCodProducto(), self.getCodPaquete())
				if afiliacionExistente:
					print "La afiliacion ya ha sido registrada en el sistema"
				else:
					conex = conexiondb.ConexionMOCEL()
					query = "INSERT INTO ASOCIA(CODIGO_PRODUCTO, CODIGO_PAQUETE) VALUES (%s, %s);"
					data = (self.getCodProducto(), self.getCodPaquete())	
					conex.cur.execute(query, data)
					conex.con.commit()
					conex.cerrarConexion()
					print "Se ha afiliado correctamente al producto con el paquete"
			else:
				print "El paquete no existe en el sistema"
		else:
			print "El producto no ha sido registrado en el sistema"

	# Elimina la afiliacion de un producto a un paquete en la tabla ASOCIA.
	def desafiliarProductoAPaquete(self):
		busq = busquedasdb.busquedadb()
		afiliacionExistente = busq.buscarAfiliacion(self.getCodProducto(), self.getCodPaquete())
		if not afiliacionExistente:
			print "La afiliacion entre el producto y el paquete no existe en el sistema"
		else:
			conex = conexiondb.ConexionMOCEL()
			query = "DELETE FROM ASOCIA A WHERE (A.CODIGO_PRODUCTO = '"+self.getCodProducto()+"' AND A.CODIGO_PAQUETE = '"+self.getCodPaquete()+"')"
			conex.cur.execute(query)
			conex.con.commit()
			conex.cerrarConexion()
			print "Se ha desafiliado correctamente al producto del paquete"
	

	# Devuelve de la tabla ASOCIA a una afiliacion previamente buscada. 
	def consultarAfiliacion(self):
		busq = busquedasdb.busquedadb()
		afiliacionValida = busq.buscarAfiliacion(self.getCodProducto(), self.getCodPaquete())
		if afiliacionValida:
			conex = conexiondb.ConexionMOCEL()
			query = "SELECT * FROM ASOCIA A WHERE (A.CODIGO_PRODUCTO = '"+self.getCodProducto()+"' AND A.CODIGO_PAQUETE = '"+self.getCodPaquete()+"');"	
			conex.cur.execute(query)
			self.imprimir()
			conex.cerrarConexion()
		else:
			print "La afiliacion no ha sido registrada en el sistema"	

	
# Principal    
if __name__== "__main__":
	afil = Afiliacion('5019', '0001')
	afil2 = Afiliacion('5013', '2201')
	afil3 = Afiliacion('5013', '1101')
	print "********************************************************************"
	afil.afiliarProductoAPaquete()
	print "********************************************************************"
	afil.desafiliarProductoAPaquete()
	print "********************************************************************"
	afil2.consultarAfiliacion()
	print "********************************************************************"
	afil3.consultarAfiliacion()
	print "********************************************************************"


