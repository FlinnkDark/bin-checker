import requests
import sys,os
from time import sleep
from bs4 import BeautifulSoup
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
try:
	os.system("del temp.txt")
	os.system("cls")
except:
	pass


def goto(linenum):
    global line
    line = linenum


class SL():
	def gimmeThat(self,k):
		proxies = []
		proxies.addpend(k)
class Scrap():
	def https(self,siono):
		req = requests.session()
		Connect = req.get("https://www.proxy-list.download/api/v1/get?type=https")
		proxy_list = Connect.text
		
		print(proxy_list)
		
		
		if siono == "1":
			a = open("https.txt","a")
			print(proxy_list,file=a)
			a.close()
		else:
			x = open("temp.txt","a+")
			print(proxy_list,file=x)			
		return proxy_list
	def http(self,siono):
		req = requests.session()
		Connect = req.get("https://www.proxy-list.download/api/v1/get?type=http")
		proxy_list = Connect.text
		
		if siono == "1":
			a = open("http.txt","a")
			print(f"{proxy_list}",file=a)
			a.close()
		else:
			x = open("temp.txt","a+")
			print(proxy_list,file=x)
		return proxy_list
	def socks4(self,siono):
		req = requests.session()
		Connect = req.get("https://www.proxy-list.download/api/v1/get?type=socks4")
		proxy_list = Connect.text
		
		if siono == "1":
			a = open("socks4.txt","a")
			print(f"{proxy_list}",file=a)
			a.close()
		else:
			x = open("temp.txt","a+")
			print(proxy_list,file=x)
		return proxy_list
	def socks5(self,siono):
		req = requests.session()
		Connect = req.get("https://www.proxy-list.download/api/v1/get?type=socks5")
		proxy_list = Connect.text
		
		if siono == "1":
			a = open("socks5","a")
			print(f"{proxy_list}",file=a)
			a.close()
		else:
			x = open("temp.txt","a+")
			print(proxy_list,file=x)
		
		return proxy_list
	def all(self,siono):
		if siono == "1" or siono == "01":
			a = open("PROXIES.txt","a")
			print(f"{self.http(2)+self.https(2)+self.socks4(2)+self.socks5(2)}",file=a)
			a.close()
		else:
			return("HTTP"+self.http(2)+"HTTPS"+self.https(2)+"SOCKS4"+self.socks4(2)+"SOCKS5"+self.socks5(2))
class Check():
	def http(self,f,nombre):
		Scrap().http("2")
		if f == "01" or f == "1":
			
			if ".txt" in nombre:
				file = open(nombre,"r+")
				file =[a.rstrip() for a in file]
				
				for lines in file:
					proxies = {"https":f"http://{lines}"}
					try:
						a = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
						if a.text in lines:
							print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
							print(lines,file=open("proxy_lives.txt","a"))
						else:
							print(Fore.RED+"PROXIE DIE : {}".format(lines))

					except KeyboardInterrupt as e:
						print("saliendo.....")
						sleep(2)
						os.system("cls")
						print(Fore.GREEN+Back.BLACK+" ")
						sleep(1)
						break
					except:
						print(Fore.RED+"PROXIE DIE : {}".format(lines))
						pass
					
			else:
				file = open(nombre+".txt","r+")
				file =[a.rstrip() for a in file]
				
				for lines in file:
					proxies = {"https":f"http://{lines}"}
					try:
						a = requests.session()
						a = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
						if a.text in lines:
							print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
							print(lines,file=open("proxy_lives.txt","a"))
						

					except KeyboardInterrupt as e:
						print("saliendo.....")
						sleep(2)
						os.system("cls")
						sleep(1)
						print(Fore.GREEN+Back.BLACK+" ")
						break
					except:
						print(Fore.RED+"PROXIE DIE : {}".format(lines))
						pass
							
		if f == "02" or f == "2":
			x = open("temp.txt","r")
			x = [a.rstrip() for a in x]
			for lines in x:
				proxies = {"https":f"http://{lines}"}
				try:
					
					x = requests.session()
					x = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
					if x.text in lines:
						print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
						print(lines,file=open("proxy_lives.txt","a"))
					
				except KeyboardInterrupt as e:
					print("saliendo.....")
					sleep(2)
					os.system("cls")
					sleep(1)
					print(Fore.GREEN+Back.BLACK+" ")
					break				

				except:
					print(Fore.RED+"PROXIE DIE : {}".format(lines))
					pass
	
	def socks4(self,f,nombre):
		Scrap().socks4("2")
		if f == "01" or f == "1":
			
			if ".txt" in nombre:
				file = open(nombre,"r+")
				file =[a.rstrip() for a in file]
				
				for lines in file:
					proxies = {"https":f"socks4://{lines}"}
					try:
						a = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
						if a.text in lines:
							print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
							print(lines,file=open("socks4_lives.txt","a"))
						else:
							print(Fore.RED+"PROXIE DIE : {}".format(lines))

					except KeyboardInterrupt as e:
						print("saliendo.....")
						sleep(2)
						os.system("cls")
						print(Fore.GREEN+Back.BLACK+" ")
						sleep(1)
						break
					except:
						print(Fore.RED+"PROXIE DIE : {}".format(lines))
						pass
					
			else:
				file = open(nombre+".txt","r+")
				file =[a.rstrip() for a in file]
				
				for lines in file:
					proxies = {"https":f"socks4://{lines}"}
					try:
						a = requests.session()
						a = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
						if a.text in lines:
							print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
							print(lines,file=open("socks4_lives.txt","a"))
						

					except KeyboardInterrupt as e:
						print("saliendo.....")
						sleep(2)
						os.system("cls")
						sleep(1)
						print(Fore.GREEN+Back.BLACK+" ")
						break
					except:
						print(Fore.RED+"PROXIE DIE : {}".format(lines))
						pass
							
		if f == "02" or f == "2":
			x = open("temp.txt","r")
			x = [a.rstrip() for a in x]
			for lines in x:
				proxies = {"https":f"socks4://{lines}"}
				try:
					
					x = requests.session()
					x = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
					if x.text in lines:
						print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
						print(lines,file=open("socks4_lives.txt","a"))
					
				except KeyboardInterrupt as e:
					print("saliendo.....")
					sleep(2)
					os.system("cls")
					sleep(1)
					print(Fore.GREEN+Back.BLACK+" ")
					break				

				except:
					print(Fore.RED+"PROXIE DIE : {}".format(lines))
					pass

	def socks5(self,f,nombre):
		Scrap().socks5("2")
		if f == "01" or f == "1":
			
			if ".txt" in nombre:
				file = open(nombre,"r+")
				file =[a.rstrip() for a in file]
				
				for lines in file:
					proxies = {"http":f"socks5://{lines}"}
					try:
						a = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
						if a.text in lines:
							print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
							print(lines,file=open("socks5_lives.txt","a"))
						else:
							print(Fore.RED+"PROXIE DIE : {}".format(lines))

					except KeyboardInterrupt as e:
						print("saliendo.....")
						sleep(2)
						os.system("cls")
						print(Fore.GREEN+Back.BLACK+" ")
						sleep(1)
						break
					except:
						print(Fore.RED+"PROXIE DIE : {}".format(lines))
						pass
					
			else:
				file = open(nombre+".txt","r+")
				file =[a.rstrip() for a in file]
				
				for lines in file:
					proxies = {"http":f"socks5://{lines}"}
					try:
						a = requests.session()
						a = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
						if a.text in lines:
							print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
							print(lines,file=open("socks5_lives.txt","a"))
						

					except KeyboardInterrupt as e:
						print("saliendo.....")
						sleep(2)
						os.system("cls")
						sleep(1)
						print(Fore.GREEN+Back.BLACK+" ")
						break
					except:
						print(Fore.RED+"PROXIE DIE : {}".format(lines))
						pass
							
		if f == "02" or f == "2":
			x = open("temp.txt","r")
			x = [a.rstrip() for a in x]
			for lines in x:
				proxies = {"http":f"socks5://{lines}"}
				try:
					
					x = requests.session()
					x = requests.get("https://canihazip.com/s",proxies=proxies,timeout=3)
					if x.text in lines:
						print(Fore.BLUE + Back.GREEN + "PROXIE LIVE : {}".format(lines))
						print(lines,file=open("socks5_lives.txt","a"))
					
				except KeyboardInterrupt as e:
					print("saliendo.....")
					sleep(2)
					os.system("cls")
					sleep(1)
					print(Fore.GREEN+Back.BLACK+" ")
					break				

				except:
					print(Fore.RED+"PROXIE DIE : {}".format(lines))
					pass

		

		
			

				
			

			

		pass




banner = """
.########.########..#######.##.....#.##....#...########.########.##.....#..######..
.##.....#.##.....#.##.....#..##...##..##..##...##.....#.##.....#.##.....#.##....##.
.##.....#.##.....#.##.....#...##.##....####....##.....#.##.....#.##.....#.##.......
.########.########.##.....#....###......##.....########.########.########.##...####
.##.......##...##..##.....#...##.##.....##.....##.......##.....#.##.....#.##....##.
.##.......##....##.##.....#..##...##....##.....##.......##.....#.##.....#.##....##.
.##.......##.....#..#######.##.....#....##.....##.......########.##.....#..######..
"""
INTRO="""____________________________________________________________________________________
=========================PROXY CHECK/SCRAPER BY HOLLOWKAT PBHG======================
------------------------------------------------------------------------------------

			+[01] CHECK PROXIES 
			+[02] EXTRAER PROXIES
			-[03] SALIR

"""

check = """--------------------------------------------------------------------------------------
+++++++++++++++++++++++++++++PROXY CHECKER BY HOLLOWKAT PBHG++++++++++++++++++++++++++
______________________________________________________________________________________

				+[01] HTTP/HTTPS
				+[02] SOCKS4
				+[03] SOCKS5
				+[04] TODOS
				-[05] ATRAS
				-[06] SALIR
"""
scrap = """**************************************************************************************
++++++++++++++++++++++++++++PROXY SCRAPER BY HOLLOWKAT PBHG+++++++++++++++++++++++++++
______________________________________________________________________________________

				+[01] HTTP/HTTPS
				+[02] SOCKS4
				+[03] SOCKS5
				-[04] ATRAS
				-[05] SALIR
"""




if __name__ == '__main__':
    line = 1
    os.system("cls")
    while line == 1:

        print(Fore.WHITE+Back.MAGENTA+banner)
        print(Fore.GREEN+Back.BLACK+INTRO)
        
        aa = input("[PBHG]$")
        if aa == "02" or aa == "2":
            line = 2
            while line == 2:
                os.system("cls")
                print(check)
                a = input("[PBHG]$")
                if a == "01" or a == "1":
                    print("DESEA GUARDAR LOS PROXIES EN UN ARCHIVO ?")
                    print("[1]SI          [2]NO")
                    b = input("[PBHG]$")
                    if b == "1" or b == "01":
                        Scrap().https("1")

                    elif b == "2" or b == "02":
                        Scrap().https("non")
                    else:
                        print(Fore.RED+Back.YELLOW+"Error....")
                    os.system("cls")
                    print("TAREA REALIZADA")
                    sleep(1)
                    goto(2)
                    
                    
                if a == "02" or a == "2":
                    print("DESEA GUARDAR LOS PROXIES EN UN ARCHIVO ?")
                    print("[1]SI          [2]NO")
                    b = input("[PBHG]$")
                    if b == "1" or b == "01":
                        Scrap().https("1")
                    elif b == "2" or b == "02":
                        Scrap().https("non")
                    else:
                            print(Fore.RED+Back.YELLOW+"Error....")
                    os.system("cls")
                    print("TAREA REALIZADA")
                    sleep(1)
                    goto(2)
                if a == "03" or a== "3":
                    print("DESEA GUARDAR LOS PROXIES EN UN ARCHIVO ?")
                    print("[1]SI          [2]NO")
                    b = input("[PBHG]$")
                    if b == "1" or b == "01":
                        Scrap().https("1")
                    elif b == "2" or b == "02":
                            Scrap().https("non")
                    else:
                        print(Fore.RED+Back.YELLOW+"Error....")
                    os.system("cls")
                    print("TAREA REALIZADA")
                    sleep(1)
                    goto(2)
                if a == "04" or a== "4":
                    print("DESEA GUARDAR LOS PROXIES EN UN ARCHIVO ?")
                    print("[1]SI          [2]NO")
                    b = input("[PBHG]$")
                    if b == "1" or b == "01":
                        Scrap().all("1")
                    elif b == "2" or b == "02":
                        Scrap().all("non")
                    else:
                        print(Fore.RED+Back.YELLOW+"Error....")
                    os.system("cls")
                    print("TAREA REALIZADA")
                    sleep(1)
                    goto(2)
                if aa == "05" or a == "5":
                    print("espere...")
                    sleep(2)
                    goto(1)
                    os.system("cls")

                if a == "06" or a== "6":
                    break
                    exit()
            

            


        elif aa == "01" or aa == "1":
            os.system("cls")
            line = 5
            while line == 5:

            	print(scrap)
            	a = input("[PBHG]$")
            	if a == "01" or a== "1":
            		print("DESEA IMPORTAR LOS PROXIES DESDE UN ARCHIVO?")
            		print("[1]SI          [2]NO")
            		b = input("[PBHG]$")
            		if b == "1" or b == "01":
            			print("ESCRIBA EL NOMBRE DEL ARCHIVO DE DONDE SE VA A IMPORTAR")
            			c = input("[PBHG]$")
            			print("TESTEANDO LOS PROXIES...")
            			sleep(2)
            			print("CTR+C para detener.")
            			Check().http("1",c)

            		elif b == "02" or b == "2":
            			print("SE USARAN LOS PROXIES ALMACENADOS DE LA ULTIMA EXTRACCION.")
            			print("TENGA EN CUENTA QUE CUANDO SE CIERRA EL PROGRAMA LOS PROXIES ALMACENADOS SE ELIMINAN.")
            			print(" DEBE EXTRAER PROXIES ANTES DE USAR ESTA OPCION.")
            			print("precione cualquier tecla para continuar.")
            			c = input("[PBHG]$")
            			c = "21"
            			print("TESTEANDO LOS PROXIES...")
            			sleep(2)
            			print("CTR+C para detener.")
            			Check().http("2",c)
            		else:
                		os.system("cls")

                		print(Fore.RED+Back.YELLOW+"DEBE ELEGIR UNA DE ESTAS OPCIONES")
                		print(Fore.GREEN+Back.BLACK+"")
                		goto(5)
            	elif a == "02" or a== "2":
                	print("DESEA IMPORTAR LOS PROXIES DESDE UN ARCHIVO?")
                	print("[1]SI          [2]NO")
                	b = input("[PBHG]$")
                	if b == "1" or b == "01":
                		print("ESCRIBA EL NOMBRE DEL ARCHIVO DE DONDE SE VA A IMPORTAR")
                		c = input("[PBHG]$")
                		print("TESTEANDO LOS PROXIES...")
                		sleep(2)
                		print("CTR+C para detener.")
                		Check().socks4("1",c)


                	elif b == "02" or b == "2":
                		print("SE USARAN LOS PROXIES ALMACENADOS DE LA ULTIMA EXTRACCION.")
                		print("TENGA EN CUENTA QUE CUANDO SE CIERRA EL PROGRAMA LOS PROXIES ALMACENADOS SE ELIMINAN.")
                		print(" DEBE EXTRAER PROXIES ANTES DE USAR ESTA OPCION.")
                		print("precione cualquier tecla para continuar.")
                		c = input("[PBHG]$")
                		c = "21"
                		print("TESTEANDO LOS PROXIES...")
                		sleep(2)
                		print("CTR+C para detener.")
                		Check().socks4("2",c)

                	else:
                		os.system("cls")

                		print(Fore.RED+Back.YELLOW+"DEBE ELEGIR UNA DE ESTAS OPCIONES")
                		print(Fore.GREEN+Back.BLACK+"")
                		goto(5)
            	elif a == "03" or a== "3":
            		print("DESEA IMPORTAR LOS PROXIES DESDE UN ARCHIVO?")
            		print("[1]SI          [2]NO")
            		b = input("[PBHG]$")

            		if b == "1" or b == "01":
            			print("ESCRIBA EL NOMBRE DEL ARCHIVO DE DONDE SE VA A IMPORTAR")
            			c = input("[PBHG]$")
            			print("TESTEANDO LOS PROXIES...")
            			sleep(2)
            			print("CTR+C para detener.")
            			Check().socks5("1",c)


            		elif b == "02" or b == "2":
            			print("SE USARAN LOS PROXIES ALMACENADOS DE LA ULTIMA EXTRACCION.")
            			print("TENGA EN CUENTA QUE CUANDO SE CIERRA EL PROGRAMA LOS PROXIES ALMACENADOS SE ELIMINAN.")
            			print(" DEBE EXTRAER PROXIES ANTES DE USAR ESTA OPCION.")
            			print("precione cualquier tecla para continuar.")
            			c = input("[PBHG]$")
            			c = "21"
            			print("TESTEANDO LOS PROXIES...")
            			sleep(2)
            			print("CTR+C para detener.")
            			Check().socks5("2",c)
            		else:
                		os.system("cls")

                		print(Fore.RED+Back.YELLOW+"DEBE ELEGIR UNA DE ESTAS OPCIONES")
                		print(Fore.GREEN+Back.BLACK+"")
                		goto(5)
            	elif a == "04" or a== "4":
            		print("espere...")
            		sleep(2)
            		goto(1)
            		os.system("cls")
            	elif a == "05" or a== "5":
            		os.system("cls")
            		break
            		exit()

            	else:
                	os.system("cls")
                	print(Fore.RED+Back.YELLOW+"DEBE ELEGIR UNA DE ESTAS OPCIONES")
                	print(Fore.GREEN+Back.BLACK+"")
                	goto(5)
                	


        elif aa == "03" or aa == "3":
        	os.system("cls")
        	break
        	exit()
        else:
            os.system("cls")
            print(Fore.RED+Back.YELLOW+"DEBE ELEGIR UNA DE ESTAS OPCIONES")
            print(Fore.GREEN+Back.BLACK+"")
