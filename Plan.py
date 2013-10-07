#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase PLAN
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

class Plan():

	def __init__(self, codPlan, nombre, descripcion, rentaBasica, codPaquete):
		self._codPlan = codPlan
		self._nombre = nombre
		self._descripcion = descripcion
		self._rentaBasica = rentaBasica
		self._codPaquete = codPaquete
		
	# Los siguientes metodos obtienen y modifican los datos del plan.
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
		
	def getRentaBasica(self):
		return self._rentaBasica
		
	def setRentaBasica(self, rentaBasica):
		self._rentaBasica = rentaBasica

	def getCodPaquete(self):
		return self._codPaquete
	
	def setCodPaquete(self, codPaquete):
		self._codPaquete = codPaquete 
		
	# Imprime por pantalla la informacion de un plan.
	def imprimir(self):
	    print self.getCodPlan()
	    print self.getNombre()
	    print self.getDescripcion()
	    print self.getRentaBasica()
	    print self.getCodPaquete()
	

# Principal    
if __name__== "__main__":
	plan = Plan('001', 'MOCEL 2000', 'XXXXX1', 49.00, '0001')
	print "********************************************************************"
	plan.imprimir()
	print "********************************************************************"


