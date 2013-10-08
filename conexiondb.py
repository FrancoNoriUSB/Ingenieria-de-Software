#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase CONEXIONES
#	Integrantes: Andreina Marcano 09-10478
#		     Luis Manuel Garcia 09-10963
#		     Vanessa Ballestes 08-10091
#		     Franco Nori 08-10801
#		     Bernardo Morales 08-10770
#	Tarea III
# 
 
import psycopg2
import unittest

class ConexionMOCEL():

	# Abre la conexion a la base de datos MOCEL. 
	def __init__(self):
		self.DSN = "dbname='mocel' user='postgres' host='localhost' password='postgres'"
		self.con = psycopg2.connect(self.DSN)
		self.cur = self.con.cursor()

	# Cierra la conexion a la base de datos MOCEL.
	def cerrarConexion(self):
		self.cur.close()
		self.con.close()


