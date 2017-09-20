#!/usr/bin/python
"""
By: Oseid Aldary:)

"""
#I LOVE PYTHON 3>(^-^)
#================ Import libraries ==============================#
try:								 #
   import dns.resolver,socket  					 #
   from os import system				         #
   from time import sleep				         #
except:							         ################################################
      print("\n[!]the [ dnspython lib ] is not found!\n[*]Please run this command [ pip install dnspython ]\n") #
      exit(0)						         ################################################
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

if check() == True:
 	system("clear || cls")
	target = raw_input("""\n
 /$$$$$$ /$$$$$$$                  /$$$$$$$$ /$$                 /$$                     /$$
|_  $$_/| $$__  $$                | $$_____/|__/                | $$                    | $$
  | $$  | $$  \ $$ /$$$$$$$       | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ | $$
  | $$  | $$$$$$$//$$_____//$$$$$$| $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$
  | $$  | $$____/|  $$$$$$|______/| $$__/   | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/|__/
  | $$  | $$      \____  $$       | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$          
 /$$$$$$| $$      /$$$$$$$/       | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$       /$$
|______/|__/     |_______/        |__/      |__/|__/  |__/ \_______/ \_______/|__/      |__/

=================

Enter target Site:> """)
	sleep(1.5)
	if target == '' or target is None:
		print("\n[!]Please Enter website: e.g:- www.facebook.com!")
		exit(0)
	else:
	     def checker():
	       try:
		   host = socket.gethostbyname(target)
		   run = socket.create_connection((host, 80), 2)
		   return True
	       except:
		     pass
	       return False

	     if checker() == True:
		print("\n\n[*]Finding All [> %s <] Site IP Addresses......... \n" %(target))
		sleep(2.1)
		print("\n:::>Found<:::\n")
		for address_type in ['A', 'AAAA']:
 			try:
            			answers = dns.resolver.query(target, address_type)
            			for rdata in answers:
                			print(rdata)
        		except dns.resolver.NoAnswer:
			     pass
		print("")
	     elif checker() == False:
			print("\n[!>] %s [<!>]Error:404 Server Not Found!"%(target))
			exit()
elif check() == False:
	print("\n[!]Please Connect to the internet and try again :)")
	exit(0)

##############################################################
##################### 		     #########################
#####################  END OF SCRIPT #########################
#####################                #########################
##############################################################
#This Script by Oseid Aldary
#Have a nice day :)
#GoodBye

