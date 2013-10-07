#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase CLIENTE
#	Integrantes: Andreina Marcano 09-10478
#		     Luis Manuel Garcia 09-10963
#		     Vanessa Ballestes 08-10091
#		     Franco Nori 08-10801
#		     Bernardo Morales 08-10770
#	Tarea III
# 
 
import psycopg2
import unittest
import Producto
import Paquete
import conexiondb
import busquedasdb

class Cliente:

	def __init__(self, tipoID, ID, nombre, direccion, telefono):
		self._tipoID = tipoID
		self._ID = ID
		self._nombre = nombre
		self._direccion = direccion
		self._telefono = telefono
		self._listaProductos = None

	# Los siguentes metodos obtienen y modifican datos al Cliente. 
	def getTipoID(self):
		return self._tipoID
	
	def setTipoID(self, tipoID):
		self._tipoID = tipoID 
	
	def getID(self):
		return self._ID
	
	def setID(self, ID):
		self._ID = ID
		
	def getNombre(self):
		return self._nombre
	
	def setNombre(self, nombre):
		self._nombre= nombre
		
	def getTelefono(self):
		return self._telefono
		
	def setTelefono(self, telefono):
		self._telefono = telefono
		
	def getDireccion(self):
		return self._direccion
		
	def setDireccion(self, direccion):
		self._direccion = direccion

	def getListaProductos(self):
		return self._listaProductos

	def setListaProductos(self):
	      if(self._listaProductos is None):
			conex = conexiondb.ConexionMOCEL()
			query = "SELECT * FROM PRODUCTO P WHERE P.IDENTIFICADOR = '"+self.getID()+"';"
			conex.cur.execute(query)
			self._listaProductos = []
			for elem in conex.cur.fetchall():
				producto = Producto.Producto(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], str(elem[7]), elem[8], elem[9], str(elem[10]), elem[11], str(elem[12]))
				self._listaProductos.append(producto)
			conex.cerrarConexion()
	      else:
		 	return False
	      return True
	      
	# Imprime por pantalla la informacion de un cliente. 
	def imprimir(self):
	    print self.getTipoID()
	    print self.getID()
	    print self.getNombre()
	    print self.getDireccion()
	    print self.getTelefono()
	    if (self.getListaProductos() != None):
		for indice in range(len(self.getListaProductos())):
		    print "Producto:\n"
		    self._listaProductos[indice].imprimir()
	    else:
		print "El Cliente no tiene productos asociados"
			
	# Agrega un cliente en la tabla CLIENTE.
	def registrarCliente(self):
		busq = busquedasdb.busquedadb()
		clienteExistente = busq.buscarCliente(self.getID())
		if clienteExistente:
			print "El cliente ya ha sido registrado en el sistema"
		else:
			conex = conexiondb.ConexionMOCEL()
			query = "INSERT INTO CLIENTE(TIPO, IDENTIFICADOR, NOMBRE, DIRECCION, TELEFONO) VALUES (%s, %s, %s, %s, %s);"
			data = (self.getTipoID(), self.getID(), self.getNombre(), self.getDireccion(), self.getTelefono())	
			conex.cur.execute(query, data)
			conex.con.commit()
			conex.cerrarConexion()
			print "Se ha registrado correctamente al cliente en el sistema"
			
	      
	# Devuelve de la tabla CLIENTE a un cliente previamente buscado. 
	def consultarCliente(self):
		busq = busquedasdb.busquedadb()
		clienteValido = busq.buscarCliente(self.getID())
		if clienteValido:
			conex = conexiondb.ConexionMOCEL()
			query = "SELECT * FROM CLIENTE C WHERE (C.IDENTIFICADOR = '"+self.getID()+"');"	
			conex.cur.execute(query)
			self.imprimir()
			conex.cerrarConexion()
		else:
			print "El cliente no ha sido registrado en el sistema"
			

	
# Principal    
if __name__== "__main__":
	cliente = Cliente('CI', '19932833', 'Andreina Marcano', 'Montalbán II', '04142255770')
	cliente1 = Cliente('CI', '20410085', 'Vanessa', 'La victoria', '04265555555')
	cliente2 = Cliente('RIF', 'J20410085', 'LoQueSea', 'Miami', '1000020000')
	print "********************************************************************"
	if cliente.setListaProductos():
		cliente.consultarCliente()
	print "********************************************************************"
	cliente1.registrarCliente()
	cliente1.consultarCliente()
	print "********************************************************************"
	cliente2.consultarCliente()
	print "********************************************************************"

