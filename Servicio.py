#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase PAQUETE
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

class Servicio():
  
	def __init__(self,codServicio, nombre, descripcion, tarifaBasica):
		self._codServicio = codServicio
		self._nombre = nombre
		self._descripcion = descripcion
		self._tarifaBasica = tarifaBasica

	# Los siguientes metodos obtienen y modifican los datos del servicio		
	def getCodServicio(self):
		return self._codServicio
	
	def setCodServicio(self, codServicio):
		self._codServicio = codServicio 
		
	def getNombre(self):
		return self._nombre
	
	def setNombre(self, nombre):
		self._nombre = nombre

	def getDescripcion(self):
		return self._descripcion
	
	def setDescripcion(self, descripcion):
		self._descripcion = descripcion
		
	def getTarifaBasica(self):
		return self._tarifaBasica
		
	def setTarifaBasica(self, tarifaBasica):
		self._tarifaBasica = tarifaBasica

	# Imprime por pantalla la informacion de un servicio		
	def imprimir(self):
	    print self.getCodServicio()
	    print self.getNombre()
	    print self.getDescripcion()
	    print self.getTarifaBasica()

	# Devuelve de la tabla SERVICIO a un servicio previamente buscado. 
	def consultarServicio(self):
		busq = busquedasdb.busquedadb()
		servicioValido = busq.buscarServicio(self.getCodServicio())
		if servicioValido:
			conex = conexiondb.ConexionMOCEL()
			query = "SELECT * FROM SERVICIO S WHERE (S.CODIGO_SERVICIO = '"+self.getCodServicio()+"');"	
			conex.cur.execute(query)
			self.imprimir()
			conex.cerrarConexion()
		else:
			print "El servicio no existe en el sistema"		
	

# Principal    
if __name__== "__main__":
	serv = Servicio('20002', 'Seg Otros moviles', 'BBBBB', 0.01250)
	serv1 = Servicio('20004', 'Mensajes', 'DDDDD', 0.500)
	print "********************************************************************"
	serv.consultarServicio()
	print "********************************************************************"
	serv1.consultarServicio()
	print "********************************************************************"
	
	
