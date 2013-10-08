#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#	Ingenieria de software I 
#	Clase FACTURA
#	Integrantes: Andreina Marcano 09-10478
#		     Luis Manuel Garcia 09-10963
#		     Vanessa Ballestes 08-10091
#		     Franco Nori 08-10801
#		     Bernardo Morales 08-10770
#	Tarea IV
# 
import datetime
import conexiondb
import Cliente
import Producto
import Paquete
import Consumo

class FacturaEstrategia(object):
  
	def __init__(self, ID, strategy=None):
		self.action = None
		
		if strategy:
		      self.action = strategy(ID)
	
	def generarFactura(self):   
		if(self.action):
			return self.action.generarFactura()
		else: 
			raise UnboundLocalError('Excepcion: No se ha suministrado una clase estrategia a FacturaEstrategia')
	
	
class FacturaPostpago(object):

	def __init__(self, ID):
		self.ID = ID

	# Calcula la fecha actual
	def calcularFechaActual(self):
 		today = datetime.datetime.now()
		dateFormat = today.strftime("%d-%m-%Y")
		timeFormat = today.strftime("%H:%M")
		return dateFormat, timeFormat
	
	# Obtiene los datos del cliente
	def obtenerDatosCliente(self):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT * FROM CLIENTE C WHERE C.IDENTIFICADOR = '"+self.ID+"';"
		conex.cur.execute(query)
		elem = conex.cur.fetchone()
		if (elem is None):
			return None
		else:
			cliente = Cliente.Cliente(elem[0],elem[1],elem[2],elem[3], elem[4])
			return cliente
		
	# Valida en imprime por pantalla las facturas postpago del cliente solicitado. 
	def generarFactura(self):
		hoy = self.calcularFechaActual()
		cliente = self.obtenerDatosCliente()
		if cliente is None:
			print "La factura no pudo ser generada. El cliente no esta registrado"
			return False

		hayProd = cliente.setListaProductos()
		if hayProd == False:
			print "La factura no pudo ser generada. No hay productos registrados"
			return False
		else:
			productos = cliente.getListaProductos()
				
			listaInclusiones = []
			listaConsumos = []
			for p in range(len(productos)):
				serviciosTotales = []
				hayPaquetes = productos[p].setListaPaquetes()
				if hayPaquetes == False:
					print "La factura no pudo ser generada. No hay paquetes registrados"
					return False	
				else:
					paquetes = productos[p].getListaPaquetes()
					for s in range(len(paquetes)):			
						hayServ = paquetes[s].setListaServiciosConInclusiones()
						if hayServ == False:
							print "La factura no pudo ser generada. No hay servicios asociados"
							return False	
						else:
							servicios = paquetes[s].getListaServiciosConInclusiones()
							for t in range(len(servicios)):
								estaEnLista = False
								for x in range(len(serviciosTotales)):
									if serviciosTotales[x][0].getCodServicio() == servicios[t][0].getCodServicio():
										serviciosTotales[x] =(serviciosTotales[x][0], serviciosTotales[x][1] + servicios[t][1])
										estaEnLista = True
										break
								if not estaEnLista:
									serviciosTotales.append(servicios[t])				
		
				hayConsumos = productos[p].setListaConsumos()
				consumosTotales = []
				if hayConsumos == False:
					print "La factura no pudo ser generada. No hay consumos asociados al producto"
					return False	
				else:
					consumosTotales = productos[p].getListaConsumos()
				listaInclusiones.append(serviciosTotales)
				listaConsumos.append(consumosTotales)
	
		print "Fecha: " + hoy[0] + ", Hora: " + hoy[1]
		print "Cliente: " + cliente.getNombre()
		print cliente.getTipoID() + ": " + cliente.getID()
		print "Direccion: " + cliente.getDireccion()
		monto = 0
		montoTotalCliente = 0
		for ind in range(len(productos)):
			if productos[ind].getTipoPlan() == 'O':
				print " Producto " + str(ind+1) + ": " + productos[ind].getCodProducto() + ", " + productos[ind].getNombre()
				print "   Afiliacion: Postpago, " + "Factuacion dia: " + productos[ind].getDiaFacturacion()				
				print "   Planes y Paquetes Contratados:	"
				paquetes = productos[ind].getListaPaquetes()
				for inde in range(len(paquetes)):
					print "    * " + paquetes[inde].getCodPaquete() + ": " + paquetes[inde].getNombre()
					print "       Monto: " + str(paquetes[inde].getMonto())
					monto = monto + float(paquetes[inde].getMonto())
			
				excesos = 0
				inclusionesProd = listaInclusiones.pop(0)
				consumosProd = listaConsumos.pop(0)
				primeraVez = 0
				for i in range(len(inclusionesProd)):
					if inclusionesProd[i][0].getCodServicio() == consumosProd[i].getCodServicio():
						excesos = consumosProd[i].getCantConsumida() - inclusionesProd[i][1]
						if excesos > 0:
							if primeraVez == 0:
								print "        Servicios consumidos en exceso:"
								primeraVez += 1
							print "         * " + inclusionesProd[i][0].getNombre() + ": " 
							print "           cantidad excedida: " + str(excesos) + " por: " + str(inclusionesProd[i][0].getTarifaBasica())
							monto = monto + float(excesos)*float(inclusionesProd[i][0].getTarifaBasica())
				print "  Monto total a pagar por producto:"	
				print "   " + str(monto) + " Bs."
				montoTotalCliente = montoTotalCliente + monto
				monto = 0
			else:
				listaInclusiones.pop(0)
				listaConsumos.pop(0)
		if montoTotalCliente == 0:
			print "+++ Este Cliente no posee productos postpago +++"
		else:
			print " El monto total a pagar por todos sus productos postpago es: " + str(montoTotalCliente) + " Bs."
			
				
class FacturaPrepago(object):

	def __init__(self, ID):
		self.ID = ID

	# Calcula la fecha actual.
	def calcularFechaActual(self):
 		today = datetime.datetime.now()
		dateFormat = today.strftime("%d-%m-%Y")
		timeFormat = today.strftime("%H:%M")
		return dateFormat, timeFormat
	
	# Obtiene los datos del cliente.
	def obtenerDatosCliente(self):
		conex = conexiondb.ConexionMOCEL()
		query = "SELECT * FROM CLIENTE C WHERE C.IDENTIFICADOR = '"+self.ID+"';"
		conex.cur.execute(query)
		elem = conex.cur.fetchone()

		if(elem is None):
			return None
		else:
			cliente = Cliente.Cliente(elem[0],elem[1],elem[2],elem[3], elem[4])
			return cliente
		
	# Valida en imprime por pantalla las facturas prepago del cliente solicitado. 
	def generarFactura(self):
		hoy = self.calcularFechaActual()
		cliente = self.obtenerDatosCliente()
		if cliente is None:
			print "La factura no pudo ser generada. El cliente no esta registrado"
			return False

		hayProd = cliente.setListaProductos()
		if hayProd == False:
			print "La factura no pudo ser generada. No hay productos registrados"
			return False
		else:
			productos = cliente.getListaProductos()
				
			listaInclusiones = []
			listaConsumos = []
			for p in range(len(productos)):
				serviciosTotales = []
				hayPaquetes = productos[p].setListaPaquetes()
				if hayPaquetes == False:
					print "La factura no pudo ser generada. No hay paquetes registrados"
					return False	
				else:
					paquetes = productos[p].getListaPaquetes()
					for s in range(len(paquetes)):			
						hayServ = paquetes[s].setListaServiciosConInclusiones()
						if hayServ == False:
							print "La factura no pudo ser generada. No hay servicios asociados"
							return False	
						else:
							servicios = paquetes[s].getListaServiciosConInclusiones()
							for t in range(len(servicios)):
								estaEnLista = False
								for x in range(len(serviciosTotales)):
									if serviciosTotales[x][0].getCodServicio() == servicios[t][0].getCodServicio():
										serviciosTotales[x] =(serviciosTotales[x][0], serviciosTotales[x][1] + servicios[t][1])
										estaEnLista = True
										break
								if not estaEnLista:
									serviciosTotales.append(servicios[t])				
		
				hayConsumos = productos[p].setListaConsumos()
				consumosTotales = []
				if hayConsumos == False:
					print "La factura no pudo ser generada. No hay consumos asociados al producto"
					return False	
				else:
					consumosTotales = productos[p].getListaConsumos()
				listaInclusiones.append(serviciosTotales)
				listaConsumos.append(consumosTotales)
	
		print "Fecha: " + hoy[0] + ", Hora: " + hoy[1]
		print "Cliente: " + cliente.getNombre()
		print cliente.getTipoID() + ": " + cliente.getID()
		print "Direccion: " + cliente.getDireccion()
		monto = 0
		montoTotalCliente = 0
		for ind in range(len(productos)):
			if productos[ind].getTipoPlan() == 'E':
				print " Producto " + str(ind+1) + ": " + productos[ind].getCodProducto() + ", " + productos[ind].getNombre()
				print "   Afiliacion: Prepago, " + "Factuacion dia: " + productos[ind].getDiaFacturacion()				
				print "   Planes y Paquetes Contratados:	"
				paquetes = productos[ind].getListaPaquetes()
				for inde in range(len(paquetes)):
					print "    * " + paquetes[inde].getCodPaquete() + ": " + paquetes[inde].getNombre()
					print "       Monto: " + str(paquetes[inde].getMonto())
					monto = monto + float(paquetes[inde].getMonto())
			
				excesos = 0
				inclusionesProd = listaInclusiones.pop(0)
				consumosProd = listaConsumos.pop(0)
				primeraVez = 0
				for i in range(len(inclusionesProd)):
					if inclusionesProd[i][0].getCodServicio() == consumosProd[i].getCodServicio():
						excesos = consumosProd[i].getCantConsumida() - inclusionesProd[i][1]
						if excesos > 0:
							if primeraVez == 0:
								print "        Servicios consumidos en exceso:"
								primeraVez += 1
							print "         * " + inclusionesProd[i][0].getNombre() + ": " 
							print "           cantidad excedida: " + str(excesos) + " por: " + str(inclusionesProd[i][0].getTarifaBasica())
							monto = monto + float(excesos)*float(inclusionesProd[i][0].getTarifaBasica())
				print "  Monto total a pagar por producto:"	
				print "   " + str(monto) + " Bs."
				montoTotalCliente = montoTotalCliente + monto
				print "  Su saldo disponible es: " + str(productos[ind].getMontoDisp()) + " Bs."
				if float(productos[ind].getMontoDisp()) >= float(monto):
					pagado = 0
					for index in range(len(consumosProd)):
						c = Consumo.Consumo(consumosProd[index].getCodProducto(), consumosProd[index].getCodServicio(), 0)
						c.actualizarACero()
					p = Producto.Producto(productos[ind].getCodProducto(), productos[ind].getID(), productos[ind].getCodPlan(), productos[ind].getNombre(), productos[ind].getDescripcion(), productos[ind].getTipoTarjeta(), productos[ind].getNumeroTarjeta(), productos[ind].getFechaVencTarjeta(), productos[ind].getBancoTarjeta(), productos[ind].getDiaFacturacion(), productos[ind].getFechaAfil(), productos[ind].getTipoPlan() , productos[ind].getMontoDisp())
					a = float(productos[ind].getMontoDisp())-float(monto)
					p.setMontoDisp(str(a))
					print "   Factura cancelada satisfactoriamente. Su nuevo saldo es: " + str(a)
					
				else:
					pagado = 1
					print "   ATENCION: Su saldo es INSUFICIENTE, Sus servicios seran suspendidos"
					print "   hasta su proxima recarga mayor a " + str(float(monto)-float(productos[ind].getMontoDisp())) + " Bs."
				monto = 0
			else:
				listaInclusiones.pop(0)
				listaConsumos.pop(0)
		if montoTotalCliente == 0:
			print "+++ Este Cliente no posee productos prepago +++"
		else:
			if pagado == 0:
				print " El monto total cancelado por todos sus productos prepago fue: " + str(montoTotalCliente) + " Bs."
			else:
				print " El monto total a cancelar por todos sus productos prepago es: " + str(montoTotalCliente) + " Bs."				
							
if __name__== "__main__":
	Factura = FacturaEstrategia('J777788888', strategy=FacturaPostpago)
	Factura1 = FacturaEstrategia('J777788888', strategy=FacturaPrepago)
	Factura2 = FacturaEstrategia('15914863', strategy=FacturaPostpago)
	Factura3 = FacturaEstrategia('11123456', strategy=FacturaPostpago)
	Factura4 = FacturaEstrategia('E470782', strategy=FacturaPrepago)
	Factura5 = FacturaEstrategia('E470782', strategy=FacturaPostpago)
	Factura6 = FacturaEstrategia('11123456', strategy=FacturaPrepago)
	Factura7 = FacturaEstrategia('12121212', strategy=FacturaPrepago)
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
	
