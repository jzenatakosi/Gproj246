#!/usr/bin/env/python
import subprocess
import optparse


#subprocess.call("ifconfig",shell=True)
#subprocess.call("sudo ifconfig eth0 down",shell=True)
#subprocess.call(" sudo ifconfig eth0 hw ether 07:12:18:67:80",shell=True)
#subprocess.call("sudo fconfig eth0 up",shell=True)
pas=optparse.OptionParser()
pas.add_option("-i","--interface",dest="interface",help="helps to change mac-address")
pas.add_option("-m","--mac", dest="new_mac",help="new_mac")
(options,arguments)=pas.parse_args()

interface=options.interface
new_mac=options.new_mac

print("[+] change mac for "+ interface+" to "+ new_mac)

subprocess.call(["sudo ifconfig",interface,"down"])
subprocess.call(["sudo ifconfig",interface,"hw","eth0",new_mac])
subprocess.call(["sudo ifconfig",interface,"up"])
