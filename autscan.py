#!/usr/bin/python3

import nmap
import signal, time, sys

banner = """
 █████╗ ██╗   ██╗████████╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║
███████║██║   ██║   ██║   ███████╗██║     ███████║██╔██╗ ██║
██╔══██║██║   ██║   ██║   ╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║╚██████╔╝   ██║   ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
Author : Erick Garcia Mendez
Github : Github.com/Zackk03                                                            
"""
#=-=-=-=-=-=[banner]=-=-=-=-=-=-=-
print(banner)

#=-=-=-=-[handle function]=-=-=-=-=-=
def handle(sig, frame):
	print("\n\n[!] Saliendo...\n")
	sys.exit(1)

#=-=-=-=-[Control + C]=-=-=-=-=-=
signal.signal(signal.SIGINT, handle)

def mainfunction():
	host=input("Ingrese el objetivo >> ")
	nm = nmap.PortScanner()
	puertos_abiertos="-p "

	#=-=-=-=-=-[Primer Escaneo]=-=-=-=-=-=
	results1 = nm.scan(hosts=host,arguments="-T5 -n -Pn -v -oN FScan.txt")
	count = 0

	#=-=-=-=-=-[Resultados]=-=-=-=-=-=
	print("\nHost >> %s" % host)
	print("Estado >> %s" % nm[host].state())
	for proto in nm[host].all_protocols():
		print("Protocolo : %s" % proto)
		print()
		lport = nm[host][proto].keys()
		sorted(lport)
		for port in lport:
			print ("Puerto : %s\tEstado : %s" % (port, nm[host][proto][port]["state"]))
			if count == 0:
				puertos_abiertos=puertos_abiertos+str(port)
				count = 1 
			else:
				puertos_abiertos=puertos_abiertos+","+str(port)

	#=-=-=-=-==-=-=-=-=-=-=[Impresion de los resultado]=-=-=-=-=-=-=-=-=-=
	print("\nPuertos abiertos : "+ puertos_abiertos +" "+str(host))
	print("\n\n[!] Escaneo completado...\n[!] Iniciando escaneo de Puertos...\n\n")
	

	#=-=-=-=-=-==-=-=-=[Segundo Escaneo]=-=-=-=-==-=-=-=-=--=   
	results2 = nm.scan(hosts=host,arguments=f"{puertos_abiertos} -sC -sV -T5 -n -Pn -oN PortScan.txt")
	print("\n\n[!] Escaneo Finalizado...")
	time.sleep(2)

#=-=-=-=-[init]=-=-=-=-=-=
if __name__=="__main__":
	mainfunction()                       