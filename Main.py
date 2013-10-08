#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase ProgramaPrincipal
#	Integrantes: Andreina Marcano 09-10478
#		     Luis Manuel Garcia 09-10963
#		     Vanessa Ballestes 08-10091
#		     Franco Nori 08-10801
#		     Bernardo Morales 08-10770
#	Tarea III
# 

import Factura_Estrategia
import Producto

class Main():
	def __init__(self):
		pass

	def menu(self):
		print ""
		print ""
		print "*************************************************************************"
		print " Bienvenido al sistema electronico de la empresa MOCEL "
		print " Las opciones que puede realizar son: "
		print "  1 - Generar factura del cliente."
		print "  2 - Contratar servicios adicionales
		print "  Ingrese una opcion valida:"
		print ""
	
	def cicloMenu(self):
		self.menu()
		a = input()
		while (a != 3):
			if a == 1:
				self.probarGeneracionFactura()
			elif a == 2:
				self.contratarServiciosAdicionales()
			else:
				print "  Opcion Invalida. Intente nuevamente: "
			self.menu()
			a = input()
		print " Gracias por usar el sistema electronico de MOCEL. "
			
	def probarGeneracionFactura(self):
		print " *** Generando Facturas por cliente: "	
		Factura = Factura_Estrategia.FacturaEstrategia('J777788888', strategy= Factura_Estrategia.FacturaPostpago)
		Factura1 = Factura_Estrategia.FacturaEstrategia('J777788888', strategy= Factura_Estrategia.FacturaPrepago)
		Factura2 = Factura_Estrategia.FacturaEstrategia('15914863', strategy= Factura_Estrategia.FacturaPostpago)
		Factura3 = Factura_Estrategia.FacturaEstrategia('11123456', strategy= Factura_Estrategia.FacturaPostpago)
		Factura4 = Factura_Estrategia.FacturaEstrategia('E470782', strategy= Factura_Estrategia.FacturaPrepago)
		Factura5 = Factura_Estrategia.FacturaEstrategia('E470782', strategy= Factura_Estrategia.FacturaPostpago)
		Factura6 = Factura_Estrategia.FacturaEstrategia('11123456', strategy= Factura_Estrategia.FacturaPrepago)
		Factura7 = Factura_Estrategia.FacturaEstrategia('12121212', strategy= Factura_Estrategia.FacturaPrepago)
		print "*******************************************************************"
		f = Factura.generarFactura()
		print "*******************************************************************"
		f1 = Factura1.generarFactura()
		print "*******************************************************************"
		f2 = Factura2.generarFactura()
		print "*******************************************************************"
		f3 = Factura3.generarFactura()
		print "*******************************************************************"
		f4 = Factura4.generarFactura()
		print "*******************************************************************"
		f5 = Factura5.generarFactura()
		print "*******************************************************************"
		f6 = Factura6.generarFactura()
		print "*******************************************************************"
		f7 = Factura7.generarFactura()
		print "*******************************************************************"	
		print ""
		print " *** Primera Factura de prueba "
		print "*******************************************************************"
		f1 = Factura.generarFactura()
		print "*******************************************************************"
		print ""
		print " *** Segunda Factura de prueba "			
		print "*******************************************************************"
		f2 = Factura1.generarFactura()
		print "*******************************************************************"
		print ""
		print " *** Tercera Factura de prueba "
		print "*******************************************************************"
		f3 = Factura2.generarFactura()
		print "*******************************************************************"
		print ""
		print " *** Cuarta Factura de prueba "
		print "*******************************************************************"
		f4 = Factura3.generarFactura()
		print "*******************************************************************"
		print ""
		print " *** Quinta Factura de prueba "
		print "*******************************************************************"
		f5 = Factura4.generarFactura()
		print "*******************************************************************"
		print ""
		print " *** Sexta Factura de prueba (CLiente no tiene producto postpago) "
		print "*******************************************************************"
		f6 = Factura5.generarFactura()
		print "*******************************************************************"
		print ""
		print " *** Septima Factura de prueba (CLiente no tiene producto prepago) "
		print "*******************************************************************"
		f7 = Factura6.generarFactura()
		print "*******************************************************************"
		print ""
		print " *** Octava Factura de prueba (CLiente no esta en base de datos) "
		print "*******************************************************************"
		f8 = Factura7.generarFactura()
		print "*******************************************************************"
		

	# OJO NO IMPLEMENTE NINGUNO DE ESTOS METODOS NI SUS LLAMADAS
	def contratarServiciosAdicionales(self):
		print " *** Generando Contrataciones de Servicios Adicionales por Producto"
		prod = Producto('5000', '20410084', '001', 'BB310', 'AABBCC', 'd', '5050505084848484', '11-08-2018', 'Mercantil', '11', '11-08-2012', 'E', 200.00)
		prod1 = Producto('5019', '20410085', '001', 'BB310', 'AABBCC', 'd', '7777777777777777', '11-08-2018', 'Mercantil', '15', '15-08-2012', 'E', 50.00)
		prod2 = Producto('5000', '20410084', '001', 'BB310', 'AABBCC', 'd', '5050505084848484', '11-08-2018', 'Mercantil', '11', '11-08-2012', 'E', 200.00)
		print "*******************************************************************"
		dec1 =
		dec2 = 
		dec3 = 
	
if __name__== "__main__":
	main = Main()
	main.cicloMenu()
