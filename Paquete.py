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
import Servicio


class Paquete:

	def __init__(self,codPaquete, nombre, descripcion, monto):
		self._codPaquete = codPaquete
		self._nombre = nombre
		self._descripcion = descripcion 
		self._monto = monto
		self._listaServiciosConInclusiones = []
		
	# Los siguientes metodos obtienen y modifican los datos del paquete.
	def getCodPaquete(self):
		return self._codPaquete
	
	def setCodPaquete(self, codPaquete):
		self._codPaquete = codPaquete
		
	def getNombre(self):
		return self._nombre
	
	def setNombre(self, nombre):
		self._nombre = nombre

	def getDescripcion(self):
		return self._descripcion
	
	def setDescripcion(self, descripcion):
		self._descricpion = descripcion
		
	def getMonto(self):
		return self._monto
		
	def setMonto(self, monto):
		self._monto = monto
		
	def getListaServiciosConInclusiones(self):
		return self._listaServiciosConInclusiones

	def setListaServiciosConInclusiones(self):
       		conex = conexiondb.ConexionMOCEL()
		query = "SELECT S.* , I.CANT_SERVICIO FROM SERVICIO S, INCLUYE I WHERE I.CODIGO_PAQUETE = '"+ self.getCodPaquete()+"' AND I.CODIGO_SERVICIO = S.CODIGO_SERVICIO;"
		conex.cur.execute(query)
		self._listaServiciosConInclusiones = []
		for elem in conex.cur.fetchall():
			servicio = (Servicio.Servicio(elem[0],elem[1],elem[2],elem[3]),elem[4])
			self._listaServiciosConInclusiones.append(servicio)
		conex.cerrarConexion()
		if len(self._listaServiciosConInclusiones) == 0:
			return False
		else:
			return True
	
	# Imprime por pantalla la informacion de un paquete.
	def imprimir(self):
	    print self.getCodPaquete()
	    print self.getNombre()
	    print self.getDescripcion()
	    print str(self.getMonto())
		
	    if (self.getListaServiciosConInclusiones() != None):
		for indice in range(len(self.getListaServiciosConInclusiones())):
			print "Servicio y Cant incluida:\n"
			self._listaServiciosConInclusiones[indice][0].imprimir()
			print str(self._listaServiciosConInclusiones[indice][1])
			print "\n"
	    else:
		print "El Paquete no tiene servicios asociados"

	# Devuelve de la tabla PAQUETE a un paquete previamente buscado. 
	def consultarPaquete(self):
		busq = busquedasdb.busquedadb()
		paqueteValido = busq.buscarPaquete(self.getCodPaquete())
		if paqueteValido:
			conex = conexiondb.ConexionMOCEL()
			query = "SELECT * FROM PAQUETE P WHERE (P.CODIGO_PAQUETE = '"+self.getCodPaquete()+"');"	
			conex.cur.execute(query)
			self.imprimir()
			conex.cerrarConexion()
		else:
			print "El paquete no existe en el sistema"


# Principal    
if __name__== "__main__":
	pack = Paquete('1101', 'MIXTO PLUS', 'ZZZZZZ2', 211.00)
	pack1 = Paquete('2201', 'Mensajes 800', 'ZZZZZZ5', 38.00)
	print "********************************************************************"
	if pack.setListaServiciosConInclusiones():
		pack.consultarPaquete()
	print "********************************************************************"
	if pack1.setListaServiciosConInclusiones():
		pack1.consultarPaquete()
	print "********************************************************************"

	
