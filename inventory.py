import shutil
import psutil
import subprocess
import platform
import uuid
import socket
from datetime import datetime

def scan_system():
   hostname = socket.gethostname()

   ip_address = socket.gethostbyname(hostname)

   mac_address = ':'.join(f'{(uuid.getnode() >> i) & 0xff:02x}'
                       for i in range (0, 48, 8) ) [::-1]

   os_name = platform.system()
   os_version = platform.release()
   interfaces = subprocess.check_output(
       ["ip","-br", "addr"],
       text=True
   )

   cpu_count = psutil.cpu_count()
   memory = psutil.virtual_memory()
   disk = shutil.disk_usage("/")

   python_version = platform.python_version()

   architecture = platform.machine()



   report = f"""
SECURE NETWORK ASSET INVENTORY
==============================

Scan Time: {datetime.now()}

Hostname : {hostname}
IP Address: {ip_address}
MAC Address: {mac_address}

Operating System: {os_name}
Operating Systeem Version: {os_version}

Network Interfaces: {interfaces}

CPU Cores: {cpu_count}
Memory : {memory.total /(1024**3): .2f} GB

Disk Total : {disk.total / (1024**3): .2f} GB
Disk Used : {disk.used /(1024**3): .2f} GB
Disk Free : {disk.free /(1024**3): .2f} GB
Python Version: {python_version}

Architecture : {architecture}
"""
   print (report)


   with open("inventory_report.txt","w") as file:
        file.write (report)
 
   print("Report saved as inventory_report.txt")


def main():
    while True: 

       print("\n ======================================")
       print(" SECURE NETWORK ASSET INVENTORY")
       print("=======================================")
       print("1. Scan System")
       print("2. View saved reports")
       print("3. Exit")


       choice = input("\nEnter choice number:  ")

       if choice =="1":
         scan_system()

       elif choice =="2":
         try:
            with open("inventory_report.txt","r") as file:
                 print("\n"+file.read())
         except FileNotFoundError:
            print("Report does not exists. Run the scan first.")

       elif choice =="3":
           print("Exiting....")
           break
      
       else:
            print("Invalid Choice. Please try again.")

main()
