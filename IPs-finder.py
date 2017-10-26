#!/usr/bin/python
"""
By: Oseid Aldary:)

"""
#I LOVE PYTHON(^-^)
#================ Import libraries ==============================#
try:								 #
   import dns.resolver,socket,urllib				 #
   from os import system				         #
   from time import sleep				         #
   import random						 #
except:							         ################################################
      print("\n[!]the [ dnspython lib ] is not found!\n[*]Please run this command [ pip install dnspython ]\n") #
      exit()						         ################################################
#================================================================#

#===============================Check internet connection!!==================================#

server = "www.google.com"
def check():
  try:
	ip = socket.gethostbyname(server)
	ss = socket.create_connection((ip, 80), 2)
	return True
  except:
	pass
  return False

def web():
	if check() == True:
		target = raw_input("[+]:Enter target WebSite:> ")
		sleep(1.5)
		if target == '' or target is None:
			print("\n[!]:Please Enter website: e.g:- www.facebook.com!\n")
			web()
		else:
		     def checker():
			try:
			   if target[:8] == "https://":
				host = target[8:]
			   elif target[:7] == "http://":
				host = target[7:]
			   else:
				host = target

			   ip = socket.gethostbyname(host)
			   run = socket.create_connection((ip, 80), 2)
			   return True
		        except:
			      pass
		        return False

		     if checker() == True:
                        if target[:8] == "https://":
                                host = target[8:]
                        elif target[:7] == "http://":
                                host = target[7:]
                        else:
                                host = target
			loob = 1
			print("\n\n[*]:Finding IPaddresses TARGET[ {} ]\n".format(target))
			sleep(2.1)
			print("\n[+]:Found\n------------------------------")
			for address_type in ['A', 'AAAA']:
	 			try:
		    		   answers = dns.resolver.query(host, address_type)
		    		   for rdata in answers:
				       print("WebServer:[{}] : {}".format(loob,rdata))
				       loob +=1
				except dns.resolver.NoAnswer:
				     pass
			resulit = loob -1
			print("\n\n[+]:This Target WebSite Has [{}] WebServer![:status:[UP]".format(resulit))
			print("")
			ask = raw_input("\n[?]:[b]ack [a]gain [e]xit\n\n[IPs-F]=> ")
			if ask =="b" or ask =="B":
				  system("clear || cls")
				  main()

			elif ask =="a" or ask =="A":
				 print("")
				 web()
			else:
			    print("\nExiting.......")
                            sleep(2)
			    exit(1)

		     elif checker() == False:
				print("\n[x]Error:404 Server Not Found!\n[x]:This Target[> {} <]Website not Found ".format(target))
				print("\n")
				web()

	elif check() == False:
		print("\n[!]:Ops Your Not Connected To The Internet\n[*]:Please Connected To The Internet and Try Agian")
		exit(1)

def ppip():
	if check() == True:
		print("\n[*]Finding Your Public IP...... ")
		sleep(2)
		ppip = urllib.urlopen('http://wtfismyip.com/text').read().rstrip()
		print("[#]:Found\n------------------")
		print("[+]:YOUR Public IP: {}".format(ppip))
	        press = raw_input("\nPress Enter To back to Main Menu")
		system("clear || cls")
		main()
	else:
	    print("\n[!]:Ops Your Not Connected To The Internet\n[*]:Please Connected To The Internet and Try Agian")
            exit()

def locip():
	if check() == True:

	   print("\n[*]Finding Your Local IP...... ")
	   sleep(2)
	   locip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
	   print("[#]:Found\n------------------")
	   print("[+]:YOUR Local IP: {}".format(locip))
	   press = raw_input("\nPress Enter To back to Main Menu")
	   system("clear || cls")
	   main()

	else:
	    print("\n[!]:Ops Your Not Connected To Any Network\n[*]:Please Connected To Some Network and Try Agian")
            exit()

def randomsay():
     say = ["GoodBye","See you later","Have a naice day"]
     rsay = random.choice(say)
     return rsay
rsay = randomsay()

def main():
	try:
	   menu = raw_input("""
 /$$$$$$ /$$$$$$$                  /$$$$$$$$ /$$                 /$$                     /$$
 |_  $$_/| $$__  $$                | $$_____/|__/                | $$                    | $$
 | $$  | $$  \ $$ /$$$$$$$       | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ | $$
 | $$  | $$$$$$$//$$_____//$$$$$$| $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$
 | $$  | $$____/|  $$$$$$|______/| $$__/   | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/|__/
 | $$  | $$      \____  $$       | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$          
/$$$$$$| $$      /$$$$$$$/       | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$       /$$
|______/|__/     |_______/        |__/      |__/|__/  |__/ \_______/ \_______/|__/      |__/
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[---]        By: Oseid Aldary        [---]
[---]	     ve:    2.0		     [---]
==========================================
[#]:WELCOME(^-^)

[+] Select Choice [+]

1 ---> Find WebSite IPADDRESSES
2 ---> Find Your Public IP Addr
3 ---> Find Your Local IP Addr

4 ---> exit

[IPs-F]--> """)
	   if menu == "1":
	      web()
	   elif menu =="2":
	        ppip()
	   elif menu =="3":
		locip()
	   elif menu =="4":
	        print("\nThanks For using IPs-Finder Script\n{}".format(rsay))
	        exit()
	   else:
	        system("clear || cls")
	        main()
	except KeyboardInterrupt:
		system("clear || cls")
		main()

if __name__=='__main__':
	main()

##############################################################
##################### 		     #########################
#####################  END OF SCRIPT #########################
#####################                #########################
##############################################################
#This Script by Oseid Aldary
#Have a nice day :)
#GoodBye



