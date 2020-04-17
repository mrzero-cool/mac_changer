#!/usr/bin/env python

import subprocess
import optparse

def _arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface" , help= "specify interface to change the mac")
    parser.add_option("-m","--mac", dest="mac", help="Change macaddress")
    (options,arguments)=parser.parse_args()
   
    if not options.interface:
        parser.error("[-] please specify the interface usage:--help for more info ")
    elif not options.mac:
        parser.error("[-] please specify the mac usage:--help for more info ")
    return options 

def Change_mac(interface,mac):
    print("[+] Changing Mac address for " + interface + " to " + mac)
    subprocess.call(["ifconfig", interface,"down"]) 
    subprocess.call(["ifconfig", interface , "hw","ether", mac])
    subprocess.call(["ifconfig", interface,"up"])    


options = _arguments()
Change_mac(options.interface, options.mac)

