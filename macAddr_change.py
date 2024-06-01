#!usr/bin/env python

import subprocess
import optparse
def macAdreschange(interface, newMac):
    print("[+] Make the changes in the Mac for "+ interface+ " To"+ newMac)

    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface, "hw","ether",newMac])
    subprocess.call(["ifconfig",interface,"up"])



parser=optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface", help="Inteface to change its Mac")
parser.add_option("-m","--mac",dest="newMac",help="This is newMac")
(options,arguments)=parser.parse_args()
interface=options.interface
newMac=options.newMac
print("Everything is working:::")