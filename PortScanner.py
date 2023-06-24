##### LIBRARIES 
import sys
import socket
from datetime import datetime
import time
##### SALLVADORR'S INTERFACE USER
###############################
###############################
print(" _____       ___   _       _       _     _       ___   _____   _____   _____    _____   ")
print("/  ___/     /   | | |     | |     | |   / /     /   | |  _  \ /  _  \ |  _  \  |  _  \  ")
print("| |___     / /| | | |     | |     | |  / /     / /| | | | | | | | | | | |_| |  | |_| |  ")
print("\___  \   / / | | | |     | |     | | / /     / / | | | | | | | | | | |  _  /  |  _  /  ")
print(" ___| |  / /  | | | |___  | |___  | |/ /     / /  | | | |_| | | |_| | | | \ \  | | \ \  ")
print("/_____/ /_/   |_| |_____| |_____| |___/     /_/   |_| |_____/ \_____/ |_|  \_\ |_|  \_\ ")
print("                                                                                        ")
###############################
###############################

target = input(str("TARGET IP \n = "))

time.sleep(0.5)


print('_' * 50)
print("SCANNING TARGET: ", target)
print("SCANNING STARTED AT: ", str(datetime.now()))
print("_" * 50)

try:
    #SCCAN EVERY PORT ON THE TARGET IP
    for port in range(1,65535):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        # RETURN BACK OPEN PORT
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] PORT {} IS OPEN".format((port)))
            s.close()
except KeyboardInterrupt:
    print("\n EXITING :(")
    sys.exit()
except socket.error:
    print("\ HOST NOR RESPONDING :(")
    sys.exit()