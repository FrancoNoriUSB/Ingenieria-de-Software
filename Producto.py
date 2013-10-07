#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase PRODUCTO
#	Integrantes: Andreina Marcano 09-10478
#		     Luis Manuel Garcia 09-10963
#		     Vanessa Ballestes 08-10091
#		     Franco Nori 08-10801
#		     Bernardo Morales 08-10770
#	Tarea III
# 
 
import psycopg2
import unittest
import Paquete
import Consumo
import conexiondb
import busquedasdb
import Cliente
import Plan

class Producto:

	def __init__(self, codProducto, ID, codPlan, nombre, descripcion, tipoTarjeta, numeroTarjeta, fechaVencTarjeta, bancoTarjeta, diaFacturacion, fechaAfil, tipoPlan, montoDisp):
		self._codProducto = codProducto
		self._ID = ID
		self._codPlan = codPlan
		self._nombre = nombre
		self._descripcion = descripcion
		self._tipoTarjeta = tipoTarjeta
		self._numeroTarjeta = numeroTarjeta
		self._fechaVencTarjeta = fechaVencTarjeta
		self._bancoTarjeta = bancoTarjeta
		self._diaFacturacion = diaFacturacion
		self._fechaAfil = fechaAfil
		self._tipoPlan = tipoPlan
		self._montoDisp = montoDisp
		self._listaPaquetes = None
		self._listaConsumos = None
	
	# Los siguientes metodos obtienen y modifican los datos del producto.
	def getCodProducto(self):
		return self._codProducto
	
	def setCodProducto(self, codProducto):
		self._codProducto = codProducto

	def getID(self):
		return self._ID
	
	def setID(self, ID):
		self._ID = ID

	def getCodPlan(self):
		return self._codPlan
	
	def setCodPlan(self, codPlan):
		self._codPlan = codPlan
		
	def getNombre(self):
		return self._nombre
	
	def setNombre(self, nombre):
		self._nombre= nombre

	def getDescripcion(self):
		return self._descripcion
	
	def setDescripcion(self, descripcion):
		self._descripcion = descripcion

	def getTipoTarjeta(self):
		return self._tipoTarjeta
	
	def setTipoTarejta(self, tipoTarjeta):
		self._tipoTarjeta = tipoTarjeta

	def getNumeroTarjeta(self):
		return self._numeroTarjeta
	
	def setNumeroTarjeta(self, numeroTarjeta):
		self._numeroTarjeta = numeroTarjeta
		
	def getFechaVencTarjeta(self):
		return self._fechaVencTarjeta
	
	def setFechaVencTarjeta(self, fechaVencTarjeta):
		self._fechaVencTarjeta= fechaVencTarjeta

	def getBancoTarjeta(self):
		return self._bancoTarjeta
	
	def setBancoTarjeta(self, bancoTarjeta):
		self._bancoTarjeta = bancoTarjeta

	def getDiaFacturacion(self):
		return self._diaFacturacion
		
	def setDiaFacturacion(self, diaFacturacion):
		self._diaFacturacion = diaFacturacion

	def getFechaAfil(self):
		return self._fechaAfil
		
	def setFechaAfil(self, fechaAfil):
		self._fechaAfil = fechaAfil

	def getTipoPlan(self):
		return self._tipoPlan
		
	def setTipoPlan(self, tipoPlan):
		self._tipoPlan = tipoPlan
	
	def getMontoDisp(self):
		return self._montoDisp
		
	def setMontoDisp(self, montoDisp):
		print montoDisp
		conex = conexiondb.ConexionMOCEL()
		query = "UPDATE PRODUCTO P SET MD_O_PU = "+ str(montoDisp) +" WHERE (C.CODIGO_PRODUCTO = '"+self.getCodProducto()+"');" 
		conex.cur.execute(query)
		conex.con.commit()
		conex.cerrarConexion()
		print "Se ha actualizado correctamente el saldo del producto."

	def getListaPaquetes(self):
		return self._listaPaquetes

	def setListaPaquetes(self):
		if(self._listaPaquetes is None):
			conex = conexiondb.ConexionMOCEL()
			query = "SELECT P.* FROM ASOCIA A, PAQUETE P  WHERE A.CODIGO_PRODUCTO = '"+self.getCodProducto()+"' AND A.CODIGO_PAQUETE = P.CODIGO_PAQUETE;"
			conex.cur.execute(query)
			self._listaPaquetes = []
			for elem in conex.cur.fetchall():
				paquete = Paquete.Paquete(elem[0],elem[1],elem[2],elem[3])
				self._listaPaquetes.append(paquete)
			conex.cerrarConexion()
		else:
			return False
		return True
	

	def getListaConsumos(self):
		return self._listaConsumos

	def setListaConsumos(self):
		if(self._listaConsumos is None):
			conex = conexiondb.ConexionMOCEL()
			query = "SELECT * FROM CONSUME C WHERE C.CODIGO_PRODUCTO = '"+self.getCodProducto()+"';"
			conex.cur.execute(query)
			self._listaConsumos = []
			for elem in conex.cur.fetchall():
				consumo = Consumo.Consumo(elem[0],elem[1],elem[2])
				self._listaConsumos.append(consumo)
			conex.cerrarConexion()
		else:
			return False
		return True

	# Imprime por pantalla la inforacion de un producto. 
	def imprimir(self):
	    print "\t" + self.getCodProducto()
	    print "\t" + self.getID()
	    print "\t" + self.getCodPlan()
	    print "\t" + self.getNombre()
	    print "\t" + self.getDescripcion()
	    print "\t" + self.getTipoTarjeta()
	    print "\t" + self.getNumeroTarjeta()
	    print "\t" + self.getFechaVencTarjeta()
	    print "\t" + self.getBancoTarjeta()
	    print "\t" + self.getDiaFacturacion()
	    print "\t" + self.getFechaAfil()
	    print "\t" + self.getTipoPlan()
	    print "\t" + str(self.getMontoDisp())

	    if (self.getListaPaquetes() != None):
		for indice in range(len(self.getListaPaquetes())):
			print "Paquete:\n"
			self._listaPaquetes[indice].imprimir()
	    else:
		print "El Producto no tiene paquetes asociados" 

	    if (self.getListaConsumos() != None):
		for indice in range(len(self.getListaConsumos())):
			print "Consumo:\n"
			self._listaConsumos[indice].imprimir()
	    else:
		print "El Producto no tiene consumos de servicios asociados"
		
	# Agrega a un producto en la tabla PRODUCTO.
	def registrarProducto(self):
		busq = busquedasdb.busquedadb()
		clienteValido = busq.buscarCliente(self.getID())
		if clienteValido:
			planValido = busq.buscarPlan(self.getCodPlan())
			if planValido:
				productoExistente = busq.buscarProducto(self.getCodProducto())
				if productoExistente:
					print "El producto ya ha sido registrado en el sistema"
				else:
					conex = conexiondb.ConexionMOCEL()
					query = "INSERT INTO PRODUCTO(CODIGO_PRODUCTO, IDENTIFICADOR, CODIGO_PLAN, NOMBRE_PRODUCTO, DESCRIPCION, TIPO_TARJETA, NUMERO_TARJETA, FECHA_VENC, NOMBRE_BANCO, DIA_FACTURACION, FECHA_AFIL, TIPO_PLAN, MD_O_PU) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" 
					data = (self.getCodProducto(), self.getID(), self.getCodPlan(), self.getNombre(), self.getDescripcion(), self.getTipoTarjeta(), self.getNumeroTarjeta(), self.getFechaVencTarjeta(), self.getBancoTarjeta(), self.getDiaFacturacion(), self.getFechaAfil(), self.getTipoPlan(), self.getMontoDisp())	
					conex.cur.execute(query, data)
					conex.con.commit()
					conex.cerrarConexion()
					print "Se ha registrado correctamente al producto en el sistema"
			else:
				print "El plan no existe en el sistema"
		else:
			print "El cliente no ha sido registrado en el sistema"


	# Devuelve de la tabla PRODUCTO a un producto previamente buscado. 
	def consultarProducto(self):
		busq = busquedasdb.busquedadb()
		productoValido = busq.buscarProducto(self.getCodProducto())
		if productoValido:
			conex = conexiondb.ConexionMOCEL()
			query = "SELECT * FROM PRODUCTO P WHERE (P.CODIGO_PRODUCTO = '"+self.getCodProducto()+"');"	
			conex.cur.execute(query)
			self.imprimir()
			conex.cerrarConexion()
		else:
			print "El priducto no ha sido registrado en el sistema"
	    
				
# Principal    
if __name__== "__main__":
	prod = Producto('5000', '20410084', '001', 'BB310', 'AABBCC', 'd', '5050505084848484', '11-08-2018', 'Mercantil', '11', '11-08-2012', 'E', 200.00)
	prod1 = Producto('5019', '20410085', '001', 'BB310', 'AABBCC', 'd', '7777777777777777', '11-08-2018', 'Mercantil', '15', '15-08-2012', 'E', 50.00)
	prod2 = Producto('5000', '20410084', '001', 'BB310', 'AABBCC', 'd', '5050505084848484', '11-08-2018', 'Mercantil', '11', '11-08-2012', 'E', 200.00)
	print "********************************************************************"
	if prod.setListaPaquetes() and prod.setListaConsumos():
		prod.consultarProducto()
	print "********************************************************************"
	prod1.registrarProducto()
	prod1.consultarProducto()
	print "********************************************************************"
	prod2.registrarProducto()
	print "********************************************************************"



