#Domain to IP
from termcolor import colored
print(colored("************** Domain To IP Converter***************",'green'))
print(colored("************** Create By N00b_Hac3r******************",'red'))

import socket
import pyfiglet #banner package
banner = colored(pyfiglet.figlet_format("IP Converter"), 'green') # use for banner

print(banner)


domain_name = input(" Please, Enter target domain: ")
ip = socket.gethostbyname(domain_name)
print("IP For {} : {}".format(domain_name,ip))
