#!/usr/bin/python

import os
import urllib.request
import json
from urllib import *
from platform import system
import sys
from datetime import datetime
import time


def slowprint(s):

    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 1000)


def ipinfo():
       ip=input(" Enter IP Address : \033[1;32m ")
       url = ("http://ip-api.com/json/")
       response = urllib.request.urlopen(url + ip)
       data = response.read()
       values = json.loads(data)
       os.system("clear")

       print ("\033[1;32m\007\n")
       os.system("figlet IP-Info | lolcat")
       slowprint("\033[1;36m =====================================")
       slowprint("\033[1;33m|            IP Information           |")
       slowprint("\033[1;36m =====================================")
       slowprint("\033[1;36m" + "\n IP          : \033[1;32m " + values['query'])
       slowprint("\033[1;36m" + " Status      : \033[1;32m " + values['status'])
       slowprint("\033[1;36m" + " Region      : \033[1;32m " + values['regionName'])
       slowprint("\033[1;36m" + " Country     : \033[1;32m " + values['country'])
       slowprint("\033[1;36m" + " Date & Time : \033[1;32m " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
       slowprint("\033[1;36m" + " City        : \033[1;32m " + values['city'])
       slowprint("\033[1;36m" + " ISP         : \033[1;32m " + values['isp'])
       slowprint("\033[1;36m" + " Lat,Lon     : \033[1;32m " + str(values['lat']) + "," + str(values['lon']))
       slowprint("\033[1;36m" + " ZIPCODE     : \033[1;32m " + values['zip'])
       slowprint("\033[1;36m" + " TimeZone    : \033[1;32m " + values['timezone'])
       slowprint("\033[1;36m" + " AS          : \033[1;32m " + values['as'] + "\n")
       print (" ")
       slowprint("\033[1;36m =====================================")
       slowprint("\033[1;33m|        Coded By VPPHacker           |")
       slowprint("\033[1;36m =====================================")
       slowprint("\033[1;91m|          www.vpphacker.com           |")
       slowprint("\033[1;36m =====================================")
       print (" ")
       slowprint("\033[1;91mPress\033[1;36m ENTER\033[1;91m To Continue")
       print (" ")
       vpp = input("\033[1;33m[+] IPInformation >>\033[1;32m")
       if vpp == " ":
                os.system("clear")
                return main()

       else:
            os.system("clear")
            return main()


def about():
       os.system("clear")
       print ("\033[1;32m\007\n")
       os.system("figlet IP-Info | lolcat")
       time.sleep(2)
       slowprint ("\033[1;91m -----------------------------------------------")
       slowprint ("\033[1;33m" + "         [+] Tool Name     =>\033[1;36m" + " IP-Info")
       slowprint ("\033[1;33m" + "         [+] Autor         =>\033[1;36m" + " VPPHacker")
       slowprint ("\033[1;33m" + "         [+] Latest Update =>\033[1;36m" + " 17/3/2019")
       slowprint ("\033[1;33m" + "         [+] YouTube       =>\033[1;36m" + " VPPHacker")
       slowprint ("\033[1;33m" + "         [+] Github        =>\033[1;36m" + " VPPHacker")
       slowprint ("\033[1;91m -----------------------------------------------")
       slowprint ("\033[1;95m" + "          [+] www.vpphacker.com [+]          ")
       slowprint ("\033[1;91m -----------------------------------------------")
       magas = input("\033[1;33m [+] Press Enter To Continue [+]")
       if magas == " ":
           os.system("clear")
           return main()

       else:
           os.system("clear")
           return main()


def ext():
      slowprint ("\033[1;36m ==============================================")
      slowprint ("\033[1;33m|      Thanks For Using IP-Information         |")
      slowprint ("\033[1;36m ==============================================")
      time.sleep(1)
      exit()


def main():
      os.system("clear")
      print("\033[1;36m")
      os.system("figlet IPInfo | lolcat")
      slowprint(" ")
      slowprint ("\033[1;33m [ 1 ]\033[1;91m Scan IP Address")
      slowprint ("\033[1;33m [ 2 ]\033[1;91m About This Tool")
      slowprint ("\033[1;33m [ 0 ]\033[1;91m Exit")
      print("     ")
      option = input("\033[1;36m [+] IPInformation >> \033[1;32m")
      if option == "1":
          os.system("clear")
          ipinfo()
          exit()

      elif option == "0":
          os.system("clear")
          ext()
          exit()

      elif option == "2":
          os.system("clear")
          about()
          exit()

      else:
          os.system("clear")
          slowprint ("\033[1;91m Enter Corret Number!!!")
          time.sleep(2)
          os.system("clear")
          return main()

main()
