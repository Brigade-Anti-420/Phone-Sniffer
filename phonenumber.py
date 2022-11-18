import os
import pystyle
from pystyle import *
import numbers
import phonenumbers
from time import *
from phonenumbers import geocoder
from phonenumbers import carrier


##   MADE BY Brigade Anti-420 !!#1418  ##

##   Using the module/api of phonenumbers  ##

## I'm a Beginner so if you find a bug it's normal just be patient ...##


banner="""


   ___ _                        __       _  __  __           
  / _ \ |__   ___  _ __   ___  / _\_ __ (_)/ _|/ _| ___ _ __ 
 / /_)/ '_ \ / _ \| '_ \ / _ \ \ \| '_ \| | |_| |_ / _ \ '__|
/ ___/| | | | (_) | | | |  __/ _\ \ | | | |  _|  _|  __/ |   
\/    |_| |_|\___/|_| |_|\___| \__/_| |_|_|_| |_|  \___|_|   
                                                                                                  


"""

method="""

lcnum     ------->    Localise the country of the phone Number that you want
vfnum     ------->    Verify if the number is availabale or not.
timezone  ------->    Allow you to know in which time zone the phone Number is.
ccode     ------->    Show you the country code of the Phone Number.
citynum   ------->    Show you the city of the number.




"""

bannerpn = Center.XCenter(banner)



def init ():
    System.Size(100,25)
init()


def localisenumber():
    os.system("cls")
    System.Title("Localise Number [+33...]")
    number = input("Type the phone number to localise : ") #put the phone number that you want to localise
    ch_nmber = phonenumbers.parse(number, "CH")
    service_nmber = phonenumbers.parse(number, "RO")
    print(geocoder.description_for_number(ch_nmber, "en"))
    print(carrier.name_for_number(service_nmber, "en"))
    rl = input("Retry? \n (y/n)")
    if rl == "y":
        verifynumber()
    else:
        main()


def verifynumber():
    System.Title("Verify Number [+33...]")
    os.system("cls")
    pn = input("Enter the phone number : ")
    phone_number = phonenumbers.parse(pn)
    valid = phonenumbers.is_valid_number(phone_number)
    print("The Phone Number is valid : ")
    rt = input("Retry? \n (y/n)")
    if rt == "y":
        verifynumber()
    else:
        main()


from phonenumbers import timezone

def timexzone():
    System.Title("Time zone Number [+33...]")
    os.system("cls")
    timezoneinput = input("Put a Phone number to get time zone")
    phoneNumber = phonenumbers.parse(timezoneinput)
    timeZone = timezone.time_zones_for_number(phoneNumber)
    print(timeZone)
    rt = input("Retry? \n (y/n)")
    if rt == "y":
        timexzone()
    else:
        main()

from phonenumbers.timezone import time_zones_for_number

        
def citynum():
    os.system("cls")
    a = input("Mettre Num")
    ro_number = phonenumbers.parse(a, "RO")
    tzlist = time_zones_for_number(ro_number)
    print(tzlist)
    retr = input("Retry? \n (y/n)")
    if retr == ("y"):
        citynum()
    else:
        main()
  
  
def countrycode():
    System.Title("Country Code Number [+33...]")
    os.system("cls")
    a = input("Enter a number : ")
    phoneNumber = phonenumbers.parse(a)
    print(phoneNumber)
    rt = input("Retry? \n (y/n)")
    if rt == "y":
        countrycode()
    else:
        main()
        
    
def main():
    os.system("cls")
    print(Colorate.Horizontal(Colors.rainbow, bannerpn))
    print(method)
    askpn = input("Type the method you want to use : ")
    if askpn == ("lcnumber"):
        localisenumber()
    elif askpn == ("citynum"):
        citynum()
    elif askpn == ("lcnum"):
        localisenumber()
    elif askpn == ("vfnum"):
        verifynumber()
    elif askpn == ("timezone"):
        timexzone()
    elif askpn == ("ccode"):
        countrycode()
    else:
        print(Colors.red, "Error put method availbale")
        sleep(2)
        main()
main()